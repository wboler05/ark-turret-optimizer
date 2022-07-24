#!/usr/bin/env python3

import sys
from PyQt5.QtWidgets import QApplication
from src.turret_optimizer_window import TurretOptimizerWindow

def main():
    
    app = QApplication(sys.argv)

    window = TurretOptimizerWindow()
    window.show()

    app.exec()


if __name__ == '__main__':
    main()