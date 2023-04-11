"""
Factor:  Calculate temperature that a person feels because of the wind (Python3)
"""

def wind_temperature(temperature, wind_speed):
   
    if temperature < 50 and wind_speed > 3:
        wind_temp = 35.74 + 0.6215*temperature - 35.75*(wind_speed**0.16) + 0.4275*temperature*(wind_speed**0.16)
        return wind_temp
    else:
        return temperature
temp = 20  # in Fahrenheit
wind_speed = 10  # in miles per hour
wind_temp = wind_temperature(temp, wind_speed)
print( wind_chtemp)