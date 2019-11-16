#!/usr/bin/env python
# -*- coding: utf8 -*-


def btcSupplyAtBlock(b):
    reward = 50
    supply = 0
    y = 210000  # reward changes all y blocks
    while b > y:
        supply = supply + y * reward
        reward = reward / 2.0
        b = b - y
    supply = supply + b * reward
    return supply


block = 1000000  # you want the supply after which block?
print(btcSupplyAtBlock(block))
