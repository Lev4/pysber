#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 19:57:17 2019

@author: lev4
"""

def get_data():
    x = input('Введите длину')
    y = input('Введите ширину')
    x = int(x)
    y = int(y)
    

def area_calc(a,b):
    area = a * b
    return area


def main():
    a, b = get_data()
    area = area_calc(a,b)
    print(area)
    
    
if __name__ == '__main__':
    main()
