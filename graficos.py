import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel, QPushButton
from matplotlib.backends.backend_qtaggs import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class VentanaInventario(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard de Inventario - Sucursales El Salvador")
        self.setGeometry(100, 100, 900, 650)
        
        # Cargar datos
        self.df = pd.read_csv('inventario_sucursales.csv')
        
        # Widget principal
        widget_central = QWidget()
        self.setCentralWidget(widget_central)
        layout = QVBoxLayout(widget_central)
        
        # Título
        titulo = QLabel("<b>Reporte Visual de Stock por Sucursal</b>")
        titulo.setStyleSheet("font-size: 16pt; color: #333; margin: 10px;")
        layout.addWidget(titulo)
        
        # Configurar Matplotlib Canvas
        self.figura = Figure(figsize=(8, 5))
        self.canvas = FigureCanvas(self.figura)
        layout.addWidget(self.canvas)
        
        # Botón para actualizar/generar gráfico
        btn_graficar = QPushButton("Actualizar Gráfico de Stock")
        btn_graficar.setStyleSheet("background-color: #007ACC; color: white; font-size: 11pt; padding: 8px;")
        btn_graficar.clicked.connect(self.generar_grafico)
        layout.addWidget(btn_graficar)
        
        # Generar gráfico al iniciar
        self.generar_grafico()

    def generar_grafico(self):
        self.figura.clear()
        ax = self.figura.add_subplot(111)
        
        # Agrupar stock por sucursal
        stock_sucursal = self.df.groupby('sucursal')['stock'].sum()
        
        colores = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
        barras = ax.bar(stock_sucursal.index, stock_sucursal.values, color=colores)
        
        ax.set_title("Stock Total de Unidades por Sucursal", fontsize=12, fontweight='bold')
        ax.set_xlabel("Sucursales", fontsize=10)
        ax.set_ylabel("Unidades en Stock", fontsize=10)
        ax.grid(axis='y', linestyle='--', alpha=0.7)
        
        # Añadir etiquetas de valor sobre las barras
        for barra in barras:
            altura = barra.get_height()
            ax.annotate(f'{altura}',
                        xy=(barra.get_x() + barra.get_width() / 2, altura),
                        xytext=(0, 3),  # 3 puntos de desplazamiento vertical
                        textcoords="offset points",
                        ha='center', va='bottom', fontsize=9, fontweight='bold')

        self.canvas.draw()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = VentanaInventario()
    ventana.show()
    sys.exit(app.exec_())