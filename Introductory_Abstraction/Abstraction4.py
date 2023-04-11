"""
Factor:  Calculate temperature that a person feels because of the wind (Python3)
"""
import math

def calculate_wind_chill_factor(wind_speed, temperature):
    # formula to calculate wind chill factor
    factor = 35.74 + 0.6215*temperature - 35.75*math.pow(wind_speed, 0.16) + 0.4275*temperature*math.pow(wind_speed, 0.16)

    return f"The wind chill factor is {factor} degrees Fahrenheit."