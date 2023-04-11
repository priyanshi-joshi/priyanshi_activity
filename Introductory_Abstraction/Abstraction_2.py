def do_conversion(num, unit, target_unit):
    """
    Conversion: Input some numbers, do some simple arithmetic to do silly conversions(Python3) 
    """
    if unit == "feet":
        factor = 0.3048
    elif unit == "miles":
        factor = 1609.34
    elif unit == "inches":
        factor = 0.0254
    # add more conversion factors for other units here

    converted_num = num * factor

    return f"{num} {unit} is equal to {converted_num} {target_unit}"