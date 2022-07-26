#!/usr/bin/env python3

import numpy as np
from PyQt5.QtGui import QColor

class AbstractTurret(object):
    _count = 0
    _id_track = 0
    def __init__(self, x=0., y=0., direction=0., size=25, color=QColor(255, 255, 255), range_m=53.):
        AbstractTurret._count += 1
        AbstractTurret._id_track += 1
        self.id = AbstractTurret._id_track
        self.x = x
        self.y = y
        self.direction = direction
        self.size = size
        self.color = color

        self.range_m = range_m
        self.bullet_travel_speed_mps = 792.48

    def __del__(self):
        AbstractTurret._count -= 1

    def track_target(self, target):

        print(f'Turret Position: ({self.x}, {self.y})')
        print(f'Target Position: ({target.x}, {target.y})')
        print(f'Target Velocity: ({target.vx}, {target.vy})')

        dx = target.x - self.x
        dy = target.y - self.y

        print(f'dx, dy: ({dx}, {dy})')

        dist = np.sqrt(dx**2 + dy**2)

        print(f'Distance: {dist}')

        target_speed = np.sqrt(target.vx**2 + target.vy**2)
        target_angle = np.arctan2(target.vy, target.vx)

        print(f'Target Speed: {target_speed}')
        print(f'Target Position Angle: {np.arctan2(dy, dx) * 180. / np.pi}')
        print(f'Target Motion Angle: {target_angle * 180. / np.pi}')

        a = dy * np.cos(target_angle)
        b = dx * np.sin(target_angle)

        abs_angle_conj = np.arctan2(-dx, dy)

        print(f'Attack Aboslute Angle: {abs_angle_conj}')

        speed_ratio = target_speed / self.bullet_travel_speed_mps
        bias = 0.
        try:
            bias = np.arccos(speed_ratio * (a - b) / dist)
        except:
            print('Bias broke')
            pass
        print(f'Target Bias: {bias}')
        attack_angle = abs_angle_conj + bias

        print(f'Attack Angle: {attack_angle * 180. / np.pi}')

        self.direction = attack_angle * 180. / np.pi

        




if __name__ == '__main__':
    turret = AbstractTurret()
    print(AbstractTurret._count)

    def test_fun(a_list:list):
        a_list.append(AbstractTurret())
        print(AbstractTurret._count)

    a = list()
    test_fun(a)
    print(AbstractTurret._count)

    del turret
    print(AbstractTurret._count)

    del a
    print(AbstractTurret._count)

    def test_fun_2():
        a = AbstractTurret()

    print(AbstractTurret._count)
    print(AbstractTurret._id_track)

    turret = AbstractTurret()
    turret.x = 0.
    turret.y = 0.

    class Target(object):
        def __init__(self):
            self.x = 10.0
            self.y = -1.0
            self.vx = 0.
            self.vy = 10.

    target = Target()
    turret.track_target(target)

    