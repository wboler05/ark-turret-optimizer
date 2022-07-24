#!/usr/bin/env python3

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor

import numpy as np

class TurretGLWindow(QOpenGLWidget):

    def __init__(self):
        super().__init__()

        self.turret_list = list()
        self.target_list = list()


    def initializeGL(self):
        pass

    def paintGL(self):
        pass

    def resizeGL(self, w:int, h:int):
        pass

    def paintEvent(self, event):

        painter = QPainter(self)

        bg_color = QColor(255, 255, 255)
        turret_color = {
            'auto': QColor(55, 191, 34),
            'heavy': QColor(12, 29, 179),
            'tek': QColor(118, 5, 153),
        }

        bg_brush = QBrush(bg_color)
        painter.setBrush(bg_brush)
        painter.drawRect(self.rect())

        for t in self.turret_list:
            brush = QBrush(turret_color[t['type']])
            brush.setStyle(Qt.SolidPattern)
            turret_gun_pen = QPen(turret_color[t['type']])

            x = t['x'] - t['size']/2
            y = t['y'] - t['size']/2

            gun_x = 35 * np.cos(t['direction'] * np.pi / 180.) + t['x']
            gun_y = 35 * np.sin(-t['direction'] * np.pi / 180.) + t['y']

            painter.setBrush(brush)
            #painter.setPen(turret_gun_pen)
            painter.drawEllipse(x, y, t['size'], t['size'])
            painter.drawLine(t['x'], t['y'], gun_x, gun_y)
            


    ###

    def add_turret(self, turret):
        self.turret_list.append(turret)

    def clear_turrets(self):
        self.turret_list = list()

    def destroy_turret(self, turret):
        turret_found = False
        for i,t in enumerate(self.turret_list):
            if turret['id'] == t['id']:
                turret_found = True
                del self.turret_list[i]
                break
        if not turret_found:
            raise Exception(f'Error deleting turret: {turret["id"]}')

    ###

    def add_target(self, target):
        self.target_list = list()

    def clear_turrets(self):
        self.target_list = list()

    def destroy_target(self, target):
        target_found = False
        for i,t in enumerate(self.target_list):
            if target['id'] == t['id']:
                target_found = True
                del self.target_list[i]
                break
        if not target_found:
            raise Exception(f'Error deleting target: {target["id"]}')