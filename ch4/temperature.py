#! /usr/bin/env python3

#module file containing functions for temperature conversisons

def to_celcius(fahrenheit):
    celcius = (fahrenheit-32)*(5/9)
    return celcius

def to_fahrenheit(celcius):
    fahrenheit = celcius*(9/5) + 32
    return fahrenheit

#test funtions using main module
def main():
    for temp in range (0, 212, 1):
        print(temp, "Fahrenheit = ", round(to_celcius(temp)), "Celcius")

    for temp in range (0, 100, 1):
        print(temp, "Celcius= ", round(to_fahrenheit(temp)), "Fahrenheit")

if __name__ == "__main__":
    main()
