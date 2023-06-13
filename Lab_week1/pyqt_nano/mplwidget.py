# ------------------------------------------------------
# -------------------- mplwidget.py --------------------
# ------------------------------------------------------
from PyQt5.QtWidgets import *

from matplotlib.backends.backend_qt5agg import FigureCanvas

from matplotlib.figure import Figure

class MplWidget(QWidget):

    def __init__(self, parent=None):

        QWidget.__init__(self, parent)

        self.canvas = FigureCanvas(Figure())

        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)

        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.canvas.figure.suptitle("Gravitational forces on Arduino")
        self.canvas.axes.set_xlabel("Time (s)")
        self.canvas.axes.set_ylabel("Gravitational force (g)")
        self.canvas.axes.set_xlim(0, 8)
        self.canvas.axes.grid(visible=True)
        self.canvas.figure.set_tight_layout(True)
        self.setLayout(vertical_layout)
