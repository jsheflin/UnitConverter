"""
temperatures between Kelvin, Celsius, Fahrenheit, and Rankine
volumes between l, tablespoons, cubic-inches, c, cf, and gallons
"""
from __future__ import division
import json
import math

# 1 (std unit) = these many units
MULTIPLIERS_TO_STD = {
    'volume': {
        'ci': 0.016,
        'cf': 28.317,
        'l': 1, # std unit
        'g':  3.78,
        'tb':  0.014,
        'c': 0.236
        },
    'temp': {
        'C': (lambda c: c + 273.15),
        'F': (lambda f: (f + 459.67) / 1.8),
        'R': (lambda r: r / 1.8),
        'K': (lambda k: k) 
        }
}

# These many units = 1 (std unit)
MULTIPLIERS_FROM_STD = {
    'volume': {
        'ci': 61.02,
        'cf': 0.035,
        'l': 1, # std unit
        'g': 0.26,
        'tb': 67.63,
        'c': 4.22
        }
}


def get_user_input(choice):
    units = ', '.join(MULTIPLIERS_TO_STD[choice].keys())
    while True:
       try:
         source_unit = input('\nEnter source unit (%s): ' % units)
       except ValueError:
         print ('invalid')
         continue
       if source_unit not in units:
         print("Sorry, I didn't understand that.")
         continue
       else:
            break
    try:
      source_val = float(input('How many %s? ' % source_unit))
    except ValueError:
      print ('invalid')
    while True:
       try:
         convert_to = input('Convert to? (%s): ' % units)
       except ValueError:
         print ('invalid')
         continue
       if convert_to not in units:
         print("Sorry, I didn't understand that.")
         continue
       else:
            break  
    try:
      answer = float(input('Answer?'))
    except ValueError:
      print ('incorrect')
    return source_unit, source_val, convert_to, answer

def get_correct_choice(prompt):

    print ("""Unit Converter
    1. Volume
    2. Temperature""")
    
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value < 1 or value > 2:
            print("Sorry, you must choose 1 or 2.")
            continue
        else:
            break
    return value

def convert(choice):
    if choice == 1:
        source_unit, source_val, convert_to,answer = get_user_input('volume')
        conversion = round(source_val * \
                               MULTIPLIERS_TO_STD['volume'][source_unit] * \
                               MULTIPLIERS_FROM_STD['volume'][convert_to], 1)
        are_close = math.isclose(answer, conversion)          
    elif choice == 2:
      source_unit, source_val, convert_to,answer = get_user_input('temp')
      k = MULTIPLIERS_TO_STD['temp'][source_unit](float(source_val))
      if convert_to == 'C':
        conversion = k - 273.15
      elif convert_to == 'F':
        conversion = k * 1.8 - 459.67
      elif convert_to == 'R':
        conversion = k * 1.8
      else: conversion = k
      are_close = math.isclose(answer, conversion)    
    if are_close:
          print('correct')
    elif answer != conversion: 
          print ('incorrect')        
    print(conversion)      

def main():

    choice = get_correct_choice('What do you want to convert: ')
    response = convert(choice)
    
    return response 
   
       
if __name__ == '__main__':
    main()