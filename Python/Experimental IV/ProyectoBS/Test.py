import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, levene, mannwhitneyu
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import cv2

# Configuración global de Seaborn
sns.set_theme(style="whitegrid", palette="Set2")

# --- Funciones auxiliares ---

def open_binaries(filename):
    """Carga archivos binarios (.bin) si existen."""
    if os.path.exists(filename):
        try:
            with open(filename, 'rb') as f:
                data = np.fromfile(f, dtype=np.uint8).reshape(614, 1092)
            return data
        except Exception as e:
            print(f"Error al cargar {filename}: {e}")
            return None
    else:
        print(f"Archivo {filename} no encontrado.")
        return None

def open_yaml(filename, key='MCo', log=False, a=255):
    """Carga archivos YAML si existen."""
    if os.path.exists(filename):
        try:
            fs = cv2.FileStorage(filename, cv2.FILE_STORAGE_READ)
            data = fs.getNode(key).mat()
            fs.release()
            if log:
                data = np.log1p(data) * (a / np.log1p(data.max()))
            return data
        except Exception as e:
            print(f"Error al cargar {filename}: {e}")
            return None
    else:
        print(f"Archivo {filename} no encontrado.")
        return None

def load_data(folder):
    """Carga archivos existentes de una carpeta."""
    data = {}
    folder_path = os.path.join(os.getcwd(), folder)
    if not os.path.exists(folder_path):
        print(f"Advertencia: La carpeta {folder_path} no existe.")
        return data

    # Lista de prefijos de archivos a cargar
    prefixes = [f"A{i}" for i in range(1, 15)] + ["AR", "avg", "av", "AVM"]
    for prefix in prefixes:
        # Generar nombres de archivo correctamente
        gd_bin = f'{folder}/{prefix}{folder}_GD.bin'      # Ej: LEP/A1LEP_GD.bin
        fujii_bin = f'{folder}/{prefix}{folder}_Fujii.bin' # Ej: LEP/A1LEP_Fujii.bin
        mco_yaml = f'{folder}/{prefix}{folder}_MCo.yaml'   # Ej: LEP/A1LEP_MCo.yaml
        thsp_yaml = f'{folder}/{prefix}{folder}_THSP.yaml' # Ej: LEP/A1LEP_THSP.yaml
        
        # Cargar los archivos (asumiendo que estas funciones ya existen)
        data[f"{prefix}GdBin"] = open_binaries(gd_bin)
        data[f"{prefix}FujiiBin"] = open_binaries(fujii_bin)
        data[f"{prefix}MCoyaml"] = open_yaml(mco_yaml, log=True)
        data[f"{prefix}THSPyaml"] = open_yaml(thsp_yaml, key='THSP')
    
    return data

def process_dataframe(df, data, folder):
    """Procesa el DataFrame añadiendo columnas calculadas y clases."""
    df['GdBin'] = df['nombre'].apply(lambda x: data.get(f"{x}GdBin"))
    df['FujiiBin'] = df['nombre'].apply(lambda x: data.get(f"{x}FujiiBin"))
    df['MCoyaml'] = df['nombre'].apply(lambda x: data.get(f"{x}MCoyaml"))
    df['THSPyaml'] = df['nombre'].apply(lambda x: data.get(f"{x}THSPyaml"))
    
    df['GdMean'] = df['GdBin'].apply(lambda x: np.mean(x) if x is not None else np.nan)
    df['GdStd'] = df['GdBin'].apply(lambda x: np.std(x) if x is not None else np.nan)
    df['FujiiMean'] = df['FujiiBin'].apply(lambda x: np.mean(x) if x is not None else np.nan)
    df['FujiiStd'] = df['FujiiBin'].apply(lambda x: np.std(x) if x is not None else np.nan)
    
    # Asignar clases: primeras 14 como 'óptimo', resto como 'no óptimo'
    df['clase'] = ['óptimo'] * 14 + ['no óptimo'] * (len(df) - 14)
    return df

def perform_statistical_tests(df, variables):
    """Realiza pruebas estadísticas si hay suficientes datos."""
    optimo = df[df['clase'] == 'óptimo']
    no_optimo = df[df['clase'] == 'no óptimo']
    
    for var in variables:
        optimo_data = optimo[var].dropna()
        no_optimo_data = no_optimo[var].dropna()
        
        if len(optimo_data) < 3 or len(no_optimo_data) < 3:
            print(f"No hay suficientes datos para {var} en ambos grupos.")
            continue
        
        # Prueba de normalidad (Shapiro-Wilk)
        _, p_opt = shapiro(optimo_data)
        _, p_no_opt = shapiro(no_optimo_data)
        print(f"Normalidad para {var}: óptimo p={p_opt:.2g}, no óptimo p={p_no_opt:.2g}")
        
        # Prueba de homogeneidad de varianzas (Levene)
        _, p_levene = levene(optimo_data, no_optimo_data)
        print(f"Homogeneidad de varianzas para {var}: p={p_levene:.2g}")
        
        # Prueba U de Mann-Whitney
        stat, p_mwu = mannwhitneyu(optimo_data, no_optimo_data, alternative='two-sided')
        print(f"Prueba U de Mann-Whitney para {var}: U={stat:.2g}, p={p_mwu:.2g}")
        if p_mwu < 0.05:
            print("Diferencia significativa (p < 0.05)")
        else:
            print("No hay diferencia significativa (p >= 0.05)")
        print()

def train_and_evaluate_model(df, variables):
    """Entrena y evalúa un modelo de regresión logística si hay suficientes datos."""
    X = df[variables].dropna()
    y = df.loc[X.index, 'clase']
    if len(X) < 5 or len(np.unique(y)) < 2:
        print("Datos insuficientes para entrenar el modelo.")
        return
    
    modelo = LogisticRegression(class_weight='balanced', random_state=42)
    scores = cross_val_score(modelo, X, y, cv=3, scoring='accuracy')
    print(f"Precisión media con validación cruzada: {scores.mean():.2f}")
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
    modelo.fit(X_train, y_train)
    predicciones = modelo.predict(X_test)
    print(f"Precisión en el conjunto de prueba: {accuracy_score(y_test, predicciones):.2f}")
    print("Matriz de confusión:")
    print(confusion_matrix(y_test, predicciones))
    print("Reporte de clasificación:")
    print(classification_report(y_test, predicciones))

# --- Función principal para analizar una carpeta ---

def analyze_folder(folder, output_dir='output'):
    """Analiza una carpeta específica (LEP o LE)."""
    print(f"\n--- Análisis de la carpeta {folder} ---")
    
    # Crear directorio de salida si no existe
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Cargar datos
    data = load_data(folder)
    if not data:
        print(f"No se encontraron datos en {folder}.")
        return None
    
    # Cargar CSV y filtrar según carpeta
    try:
        df = pd.read_csv('MIs.csv')
        if folder == "LEP":
            df_folder = df[27:45].reset_index(drop=True)
        elif folder == "LE":
            df_folder = df[0:18].reset_index(drop=True)
        else:
            print(f"Carpeta {folder} no soportada.")
            return None
    except Exception as e:
        print(f"Error al cargar CSV para {folder}: {e}")
        return None
    
    # Procesar DataFrame
    df_folder = process_dataframe(df_folder, data, folder)
    
    # Visualización inicial (MCo logarítmica)
    optimo = df_folder[df_folder['clase'] == 'óptimo']
    no_optimo = df_folder[df_folder['clase'] == 'no óptimo']
    
    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    if not optimo['MCoyaml'].isna().all():
        axs[0].imshow(np.log1p(optimo['MCoyaml'].mean()), cmap='jet')
    axs[0].axis('off')
    axs[0].set_title(f'MCo Logarítmica - Óptimo ({folder})')
    if not no_optimo['MCoyaml'].isna().all():
        axs[1].imshow(np.log1p(no_optimo['MCoyaml'].mean()), cmap='jet')
    axs[1].axis('off')
    axs[1].set_title(f'MCo Logarítmica - No Óptimo ({folder})')
    plt.savefig(os.path.join(output_dir, f'mco_{folder}.png'))
    plt.close()
    
    # Boxplot de MI
    plt.figure(figsize=(8, 6))
    sns.boxplot(x='clase', y='MI', data=df_folder, hue='clase', palette='Set2')
    plt.title(f"Comparación de MI: Óptimos vs No óptimos ({folder})")
    plt.savefig(os.path.join(output_dir, f'boxplot_mi_{folder}.png'))
    plt.close()
    
    # Pruebas estadísticas
    variables = ['MI', 'GdMean', 'GdStd', 'FujiiMean', 'FujiiStd']
    perform_statistical_tests(df_folder, variables)
    
    # Modelado
    train_and_evaluate_model(df_folder, ['GdMean', 'GdStd'])
    
    return df_folder

# --- Función para comparar LEP y LE ---

def compare_folders(df_lep, df_le, output_dir='output'):
    """Compara las clasificaciones entre LEP y LE."""
    print("\n--- Comparación entre LEP y LE ---")
    
    # Comparar distribuciones de MI
    plt.figure(figsize=(10, 6))
    sns.kdeplot(df_lep['MI'], label='LEP', fill=True)
    sns.kdeplot(df_le['MI'], label='LE', fill=True)
    plt.title("Comparación de MI entre LEP y LE")
    plt.xlabel("MI")
    plt.legend()
    plt.savefig(os.path.join(output_dir, 'comparacion_mi_lep_le.png'))
    plt.close()
    
    # Prueba de Mann-Whitney U para MI entre LEP y LE
    stat, p = mannwhitneyu(df_lep['MI'], df_le['MI'], alternative='two-sided')
    print(f"Prueba U de Mann-Whitney para MI (LEP vs LE): U={stat:.2g}, p={p:.2g}")
    if p < 0.05:
        print("Diferencia significativa en MI entre LEP y LE (p < 0.05)")
    else:
        print("No hay diferencia significativa en MI entre LEP y LE (p >= 0.05)")

# --- Ejecución automática ---

# Analizar LEP y LE
df_lep = analyze_folder("LEP")
df_le = analyze_folder("LE")

# Comparar resultados si ambos análisis son exitosos
if df_lep is not None and df_le is not None:
    compare_folders(df_lep, df_le)