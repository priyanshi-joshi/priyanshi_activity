"""
Earthquake Impact: Input some numbers, do some simple arithmetic, output results. (Python3)
"""
def calculate_earthquake_impact(magnitude):
    # formula to calculate impact based on magnitude
    impact = 10**(1.5*magnitude - 5.75)

    return f"The potential impact of the earthquake is {impact}"
