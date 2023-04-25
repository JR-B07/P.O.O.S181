import tkinter as tk
from tkinter import messagebox

romano_a_arabigo = {'i':1, 'iv':4, 'v':5, 'ix':9, 'x':10, 'xL':40, 'L':50}
arabigo_a_romano = {1:'i', 4:'iv', 5:'v', 9:'ix', 10:'x', 40:'xL', 50:'L'}

def romano_a_arabigo_convert(romano_numeral):
    arabigo_numeral = 0
    i = 0
    while i < len(romano_numeral):
        if i+1<len(romano_numeral) and romano_numeral[i:i+2] in romano_a_arabigo:
            arabigo_numeral += romano_a_arabigo[romano_numeral[i:i+2]]
            i += 2
        else:
            arabigo_numeral += romano_a_arabigo[romano_numeral[i]]
            i += 1
    return arabigo_numeral

def arabigo_a_romano_convert(arabigo_numeral):
    romano_numeral = ''
    for num, numeral in sorted(arabigo_a_romano.items(), reverse=True):
        while arabigo_numeral >= num:
            romano_numeral += numeral
            arabigo_numeral -= num
    return romano_numeral

def validar_number(num):
    try:
        int_num = int(num)
        if int_num < 1 or int_num > 50:
            return False
        else:
            return True
    except ValueError:
        return False

def validar_romano_numeral(numeral):
    for char in numeral:
        if char not in romano_a_arabigo.keys():
            return False
    return True


