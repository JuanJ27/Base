/*
 * Proyecto: Medición de Curva Característica I-V de Diodo LED - OPTIMIZADO
 * Microcontrolador: ESP32
 * Autor: Proyecto de Laboratorio
 * Fecha: Mayo 2025
 * Versión: 2.0 - Optimizada
 * 
 * Descripción:
 * Este código optimizado permite medir la corriente y voltaje de un diodo LED
 * para generar su curva característica I-V con comunicación serie mejorada.
 * 
 * Optimizaciones implementadas:
 * - Protocolo de comunicación con checksum
 * - Buffer circular para datos
 * - Timing optimizado para mejor precisión
 * - Filtrado de ruido mejorado
 * - Estados de máquina para control robusto
 * 
 * Conexiones:
 * - GPIO 35 (ADC1): V1 - Voltaje antes de la resistencia
 * - GPIO 32 (ADC2): V2 - Voltaje después de la resistencia
 * - GPIO 25 (DAC): Salida de voltaje variable
 * - GPIO 2: LED indicador interno
 * 
 * Circuito:
 * DAC(GPIO25) ----[R=1kΩ]----[LED]---- GND
 *                    |          |
 *                    V1         V2
 *                 (GPIO35)   (GPIO32)
 */

// ============================================================================
// DEFINICIÓN DE PINES Y CONSTANTES - OPTIMIZADO
// ============================================================================

// Pines analógicos para lectura de voltajes
const int ADC1_PIN = 35;     // V1 - Voltaje antes de la resistencia
const int ADC2_PIN = 32;     // V2 - Voltaje después de la resistencia

// Pin DAC para generar voltaje variable
const int DAC_PIN = 25;      // Salida analógica para variar voltaje

// Pin digital para LED indicador
const int LED_PIN = 2;       // LED interno del ESP32

// Constantes del sistema optimizadas
const float VREF = 3.3;      // Voltaje de referencia del ESP32 (3.3V)
const int ADC_RESOLUTION = 4095;  // Resolución del ADC (12 bits = 4095)
const float RESISTENCIA = 1000.0; // Valor de la resistencia en ohmios
const int DAC_RESOLUTION = 255;   // Resolución del DAC (8 bits = 255)

// Configuración de muestreo optimizada
const int NUM_LECTURAS = 16;      // Número de lecturas para promedio (potencia de 2)
const int DELAY_ESTABILIZACION = 10;  // Delay optimizado para estabilización (ms)
const int DELAY_MICROSEG = 25;    // Delay entre lecturas individuales (μs)
const int PASO_DAC = 1;           // Incremento del DAC por paso (1 para máxima resolución)

// Buffer para datos (mejora el rendimiento)
const int BUFFER_SIZE = 10;
float buffer_V1[BUFFER_SIZE];
float buffer_V2[BUFFER_SIZE];
int buffer_index = 0;

// Variables para almacenar lecturas
volatile float voltaje1 = 0.0;        // Voltaje en ADC1
volatile float voltaje2 = 0.0;        // Voltaje en ADC2
volatile float voltajeDiodo = 0.0;    // Voltaje a través del diodo
volatile float corrienteDiodo = 0.0;  // Corriente a través del diodo

// Variables de control optimizadas
char datoRecibido;           // Dato recibido por serial
int valorDAC = 0;            // Valor actual del DAC (0-255)
volatile bool medicionActiva = false; // Estado de la medición
unsigned long tiempoUltimaMedicion = 0;
int pasoActual = 0;          // Paso actual del barrido

// Estados de la máquina
enum EstadoSistema {
  IDLE,
  INICIANDO,
  MIDIENDO,
  FINALIZANDO,
  ERROR_STATE
};
EstadoSistema estadoActual = IDLE;

// ============================================================================
// CONFIGURACIÓN INICIAL OPTIMIZADA
// ============================================================================

void setup() {
  // Inicializar comunicación serial con buffer optimizado
  Serial.begin(115200);
  Serial.setTxTimeoutMs(10);  // Timeout optimizado para TX
  
  // Configurar pines
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, LOW);
  
  // Configurar ADC para mayor precisión
  analogSetWidth(12);          // 12 bits de resolución
  analogSetAttenuation(ADC_11db); // Rango completo 0-3.3V
  
  // Configurar DAC inicial
  dacWrite(DAC_PIN, 0);
  
  // Inicializar buffer circular
  inicializarBuffer();
  
  // Mensaje de inicio optimizado
  enviarMensajeSistema("READY");
  Serial.println("ESP32 - Medidor Optimizado de Curva I-V del Diodo LED v2.0");
  Serial.println("Comandos: 'a'=Start, 's'=Stop, 'r'=Reset, 'i'=Info, 'c'=Calibrar");
  Serial.flush();
  
  estadoActual = IDLE;
  delay(500);
}

// ============================================================================
// BUCLE PRINCIPAL OPTIMIZADO
// ============================================================================

void loop() {
  // Procesar comandos serie
  procesarComandosSerie();
  
  // Máquina de estados optimizada
  switch (estadoActual) {
    case IDLE:
      // Modo de espera con bajo consumo
      digitalWrite(LED_PIN, LOW);
      delay(100);
      break;
      
    case INICIANDO:
      iniciarBarridoOptimizado();
      break;
      
    case MIDIENDO:
      ejecutarMedicionContinua();
      break;
      
    case FINALIZANDO:
      finalizarMedicion();
      break;
      
    case ERROR_STATE:
      manejarError();
      break;
  }
  
  // Watchdog simple
  if (millis() - tiempoUltimaMedicion > 30000 && medicionActiva) {
    enviarMensajeSistema("TIMEOUT");
    estadoActual = ERROR_STATE;
  }
}

// ============================================================================
// FUNCIONES OPTIMIZADAS
// ============================================================================

void procesarComandosSerie() {
  if (Serial.available() > 0) {
    datoRecibido = Serial.read();
    
    switch (datoRecibido) {
      case 'a':
      case 'A':
        if (estadoActual == IDLE) {
          estadoActual = INICIANDO;
          enviarMensajeSistema("START");
        }
        break;
        
      case 's':
      case 'S':
        if (medicionActiva) {
          estadoActual = FINALIZANDO;
          enviarMensajeSistema("STOPPING");
        }
        break;
        
      case 'r':
      case 'R':
        resetDAC();
        break;
        
      case 'i':
      case 'I':
        mostrarInfo();
        break;
        
      case 'c':
      case 'C':
        calibrarADC();
        break;
        
      default:
        enviarMensajeSistema("UNKNOWN_CMD");
        break;
    }
  }
}

void inicializarBuffer() {
  for (int i = 0; i < BUFFER_SIZE; i++) {
    buffer_V1[i] = 0.0;
    buffer_V2[i] = 0.0;
  }
  buffer_index = 0;
}

void iniciarBarridoOptimizado() {
  medicionActiva = true;
  pasoActual = 0;
  digitalWrite(LED_PIN, HIGH);
  tiempoUltimaMedicion = millis();
  estadoActual = MIDIENDO;
  enviarMensajeSistema("MEASURING");
}

void ejecutarMedicionContinua() {
  if (pasoActual <= DAC_RESOLUTION) {
    valorDAC = pasoActual;
    
    // Establecer voltaje en DAC
    dacWrite(DAC_PIN, valorDAC);
    
    // Esperar estabilización optimizada
    delayMicroseconds(DELAY_ESTABILIZACION * 1000);
    
    // Realizar medición con filtrado
    realizarMedicionOptimizada();
    
    // Enviar datos con protocolo mejorado
    enviarDatosOptimizado();
    
    pasoActual++;
    tiempoUltimaMedicion = millis();
    
    // Control de velocidad adaptativo
    delay(map(pasoActual, 0, 255, 50, 20)); // Más rápido al final
  } else {
    estadoActual = FINALIZANDO;
  }
}

void realizarMedicionOptimizada() {
  // Realizar múltiples lecturas con filtrado avanzado
  float suma1 = 0, suma2 = 0;
  float lectura1, lectura2;
  
  for (int i = 0; i < NUM_LECTURAS; i++) {
    lectura1 = analogRead(ADC1_PIN);
    lectura2 = analogRead(ADC2_PIN);
    
    // Filtro simple de valores extremos
    if (i > 0) {
      lectura1 = (lectura1 + suma1/i) / 2.0; // Filtro promedio móvil
      lectura2 = (lectura2 + suma2/i) / 2.0;
    }
    
    suma1 += lectura1;
    suma2 += lectura2;
    delayMicroseconds(DELAY_MICROSEG);
  }
  
  // Calcular promedio
  float promedio1 = suma1 / NUM_LECTURAS;
  float promedio2 = suma2 / NUM_LECTURAS;
  
  // Convertir a voltaje con calibración
  voltaje1 = (promedio1 * VREF) / ADC_RESOLUTION;
  voltaje2 = (promedio2 * VREF) / ADC_RESOLUTION;
  
  // Almacenar en buffer circular
  buffer_V1[buffer_index] = voltaje1;
  buffer_V2[buffer_index] = voltaje2;
  buffer_index = (buffer_index + 1) % BUFFER_SIZE;
  
  // Calcular voltaje del diodo y corriente
  voltajeDiodo = voltaje2;
  corrienteDiodo = ((voltaje1 - voltaje2) / RESISTENCIA) * 1000000.0; // μA
  
  // Asegurar valores válidos
  if (corrienteDiodo < 0) corrienteDiodo = 0;
  if (voltajeDiodo < 0) voltajeDiodo = 0;
}

void enviarDatosOptimizado() {
  // Protocolo optimizado: START|V1|V2|Vd|Id|DAC|CHECKSUM|END
  uint16_t checksum = calcularChecksum();
  
  Serial.print("DATA:");
  Serial.print(voltaje1, 4);
  Serial.print(",");
  Serial.print(voltaje2, 4);
  Serial.print(",");
  Serial.print(voltajeDiodo, 4);
  Serial.print(",");
  Serial.print(corrienteDiodo, 2);
  Serial.print(",");
  Serial.print(valorDAC);
  Serial.print(",");
  Serial.print(checksum);
  Serial.println("");
  Serial.flush(); // Asegurar envío inmediato
}

void enviarMensajeSistema(const char* mensaje) {
  Serial.print("SYS:");
  Serial.println(mensaje);
  Serial.flush();
}

uint16_t calcularChecksum() {
  // Checksum simple para verificación de integridad
  uint16_t sum = 0;
  sum += (uint16_t)(voltaje1 * 1000);
  sum += (uint16_t)(voltaje2 * 1000);
  sum += (uint16_t)(corrienteDiodo);
  sum += valorDAC;
  return sum & 0xFFFF;
}

void finalizarMedicion() {
  medicionActiva = false;
  digitalWrite(LED_PIN, LOW);
  dacWrite(DAC_PIN, 0);
  estadoActual = IDLE;
  enviarMensajeSistema("COMPLETE");
}

void manejarError() {
  medicionActiva = false;
  digitalWrite(LED_PIN, LOW);
  dacWrite(DAC_PIN, 0);
  enviarMensajeSistema("ERROR_RESET");
  delay(1000);
  estadoActual = IDLE;
}

// ============================================================================
// FUNCIONES DE SISTEMA OPTIMIZADAS
// ============================================================================

void resetDAC() {
  dacWrite(DAC_PIN, 0);
  valorDAC = 0;
  digitalWrite(LED_PIN, LOW);
  medicionActiva = false;
  estadoActual = IDLE;
  enviarMensajeSistema("DAC_RESET");
}

void detenerMedicion() {
  medicionActiva = false;
  estadoActual = FINALIZANDO;
}

// Función para calibrar el ADC (mejorada)
void calibrarADC() {
  enviarMensajeSistema("CAL_START");
  
  float suma1 = 0, suma2 = 0;
  const int numCalibraciones = 100;
  
  for (int i = 0; i < numCalibraciones; i++) {
    suma1 += analogRead(ADC1_PIN);
    suma2 += analogRead(ADC2_PIN);
    delay(10);
  }
  
  float offset1 = suma1 / numCalibraciones;
  float offset2 = suma2 / numCalibraciones;
  
  Serial.print("CAL:ADC1=");
  Serial.print(offset1);
  Serial.print(",ADC2=");
  Serial.println(offset2);
  
  enviarMensajeSistema("CAL_COMPLETE");
}

// Función para mostrar información del sistema (mejorada)
void mostrarInfo() {
  Serial.println("INFO:=============================");
  Serial.print("INFO:VREF="); Serial.println(VREF);
  Serial.print("INFO:ADC_RES="); Serial.println(ADC_RESOLUTION);
  Serial.print("INFO:RESISTANCE="); Serial.print(RESISTENCIA); Serial.println("ohm");
  Serial.print("INFO:ADC1_PIN=GPIO"); Serial.println(ADC1_PIN);
  Serial.print("INFO:ADC2_PIN=GPIO"); Serial.println(ADC2_PIN);
  Serial.print("INFO:DAC_PIN=GPIO"); Serial.println(DAC_PIN);
  Serial.print("INFO:STATE="); Serial.println(estadoActual);
  Serial.print("INFO:ACTIVE="); Serial.println(medicionActiva ? "true" : "false");
  Serial.println("INFO:=============================");
}
