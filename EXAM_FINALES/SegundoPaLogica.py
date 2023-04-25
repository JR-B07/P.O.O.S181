import tkinter as tk
from tkinter import messagebox

class ConvertidorArabicoRomano:
    def romano_arabigo(self, numeral):
        romano_arabigo_dict = {'I':1, 'IV':4, 'V':5, 'IX':9, 'X':10, 'XL':40, 'L':50}
        arabic = 0
        i = 0
        while i < len(numeral):
            if i+1 < len(numeral) and numeral[i:i+2] in romano_arabigo_dict:
                arabic += romano_arabigo_dict[numeral[i:i+2]]
                i += 2
            else:
                arabic += romano_arabigo_dict[numeral[i]]
                i += 1
        return arabic

    def arabigo_romano(self, number):
        arabigo_romano_dict = {50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        roman = ''
        for arabic, numeral in arabigo_romano_dict.items():
            while number >= arabic:
                roman += numeral
                number -= arabic
        return roman