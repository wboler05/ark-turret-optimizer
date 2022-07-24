#!/usr/bin/env python3

from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtCore import QTimer
from src.turret_gl_window import TurretGLWindow

class TurretOptimizerWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle('Ark Turret Optimizer')

        window_layout = QVBoxLayout()
        self.turret_gl_window = TurretGLWindow()
        
        self.gui_timer = QTimer()
        self.gui_timer.timeout.connect(self.turret_gl_window.update)
        self.gui_timer.start(15)

        window_layout.addWidget(self.turret_gl_window)

        central_widget = QWidget()
        central_widget.setLayout(window_layout)

        self.setCentralWidget(central_widget)
        self.resize(800, 600)

        for i in range(5):
            turret = {
                'type':'tek',
                'x': i*25,
                'y': i*25,
                'id': i,
                'size': 25,
                'direction': 135,
            }
            self.turret_gl_window.add_turret(turret)

        self.dumb_timer = QTimer()
        self.dumb_timer.timeout.connect(self.dumb_movement)
        self.dumb_timer.start(250)

    def dumb_movement(self):
        #self.turret_gl_window.turret_list[2]['x'] += 25
        self.turret_gl_window.turret_list[2]['direction'] += 15

    