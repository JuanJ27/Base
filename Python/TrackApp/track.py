import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget,
    QVBoxLayout, QHBoxLayout, QLabel, QTextEdit,
    QGridLayout, QPushButton, QFrame
)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Registro de pases en fútbol (4-3-3)")

        # Diccionarios para mapear teclas a jugadores y zonas
        self.players = {
            'x': 'Arquero',
            'a': 'Lateral Izquierdo',
            's': 'Central Izquierdo',
            'd': 'Central Derecho',
            'f': 'Lateral Derecho',
            'w': 'Mediocampista Izquierdo',
            'e': 'Mediocampista Central',
            'r': 'Mediocampista Derecho',
            '3': 'Delantero Izquierdo',
            '4': 'Delantero Centro',
            '5': 'Delantero Derecho'
        }

        self.zones = {
            'b': 'Esquina inferior izquierda',
            'n': 'Mitad inferior central',
            'm': 'Esquina inferior derecha',
            'h': 'Mitad central izquierda',
            'j': 'Centro de la cancha',
            'k': 'Mitad central derecha',
            'u': 'Esquina superior izquierda',
            'i': 'Mitad superior central',
            'o': 'Esquina superior derecha'
        }

        # Variables para controlar la secuencia de selección
        self.selected_player = None
        self.receive_zone = None
        self.delivery_zone = None

        # Interfaz gráfica
        self.initUI()

    def initUI(self):
        # Widget contenedor principal
        main_widget = QWidget()
        main_layout = QHBoxLayout(main_widget)
        self.setCentralWidget(main_widget)

        # Sección Izquierda: Formación 4-3-3
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setAlignment(Qt.AlignTop)

        formation_layout = QVBoxLayout()

        # Fila 1: Delanteros
        row1 = QHBoxLayout()
        row1.addWidget(QPushButton("3"))
        row1.addWidget(QPushButton("4"))
        row1.addWidget(QPushButton("5"))
        formation_layout.addLayout(row1)

        # Fila 2: Mediocampistas
        row2 = QHBoxLayout()
        row2.addWidget(QPushButton("w"))
        row2.addWidget(QPushButton("e"))
        row2.addWidget(QPushButton("r"))
        formation_layout.addLayout(row2)

        # Fila 3: Defensas
        row3 = QHBoxLayout()
        row3.addWidget(QPushButton("a"))
        row3.addWidget(QPushButton("s"))
        row3.addWidget(QPushButton("d"))
        row3.addWidget(QPushButton("f"))
        formation_layout.addLayout(row3)

        # Fila 4: Arquero
        row4 = QHBoxLayout()
        row4.addWidget(QPushButton("x"))
        formation_layout.addLayout(row4)

        left_layout.addLayout(formation_layout)

        main_layout.addWidget(left_widget)

        # Sección Derecha: Cancha subdividida en 3x3
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)

        # Label de instrucción
        instruction_label = QLabel("Use las teclas para:\n"
                                   " - Seleccionar jugador (x, a, s, d, f, w, e, r, 3, 4, 5).\n"
                                   " - Seleccionar zona (b, n, m, h, j, k, u, i, o).")
        instruction_label.setStyleSheet("font-size: 12px;")
        right_layout.addWidget(instruction_label)

        # Zona de 'cancha' en una cuadrícula 3x3
        grid_frame = QFrame()
        grid_layout = QGridLayout(grid_frame)
        grid_layout.setSpacing(5)

        # Creamos 9 botones (o QFrame vacíos) que representen las 9 zonas:
        # b, n, m, h, j, k, u, i, o (en orden aproximado arriba -> abajo, izquierda -> derecha)
        # Aunque la letra no saldrá en el botón, se muestra a modo de ejemplo
        zone_keys = [['u', 'i', 'o'],
                     ['h', 'j', 'k'],
                     ['b', 'n', 'm']]

        for row in range(3):
            for col in range(3):
                btn = QPushButton(zone_keys[row][col].upper())
                btn.setFixedSize(70, 50)
                # Solo para una referencia visual
                # (En la práctica, se controlan con el teclado, no con clic)
                grid_layout.addWidget(btn, row, col)

        right_layout.addWidget(grid_frame)

        # Campo de texto para mostrar los registros
        self.log_textedit = QTextEdit()
        self.log_textedit.setReadOnly(True)
        right_layout.addWidget(self.log_textedit)

        main_layout.addWidget(right_widget)

    def keyPressEvent(self, event):
        key = event.text().lower()  # Convertimos a minúscula por si se presiona en mayúscula
        if key in self.players:
            # Si la tecla corresponde a un jugador
            self.selected_player = self.players[key]
            self.log_textedit.append(f"Jugador seleccionado: {self.selected_player}")
        elif key in self.zones:
            # Si la tecla corresponde a una zona
            if self.selected_player is None:
                # Si aún no se ha seleccionado un jugador, no hacemos nada
                self.log_textedit.append("Primero selecciona un jugador.")
                return

            if self.receive_zone is None:
                # Todavía no se ha seleccionado la zona de recepción
                self.receive_zone = self.zones[key]
                self.log_textedit.append(f"Zona de recepción: {self.receive_zone}")
            elif self.delivery_zone is None:
                # Todavía no se ha seleccionado la zona de entrega
                self.delivery_zone = self.zones[key]
                self.log_textedit.append(f"Zona de entrega: {self.delivery_zone}")

                # Ya tenemos las 3 partes: jugador, zona de recepción, zona de entrega
                self.save_pass_info()

                # Reseteamos para la próxima secuencia
                self.selected_player = None
                self.receive_zone = None
                self.delivery_zone = None

        super().keyPressEvent(event)

    def save_pass_info(self):
        """
        Guarda la información en el log_textedit o en donde se requiera.
        """
        resumen = (f"\n\n=== REGISTRO DE PASE ===\n"
                   f"Jugador: {self.selected_player}\n"
                   f"Recibe en: {self.receive_zone}\n"
                   f"Entrega en: {self.delivery_zone}\n"
                   f"=========================")
        self.log_textedit.append(resumen)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
