"""
Problem -I 
The wavelength of visible light ranges from 380 to 750 nanometers (nm). While the
spectrum is continuous, it is often divided into 6 colors as shown below:

Violet 380 to less than 450
Blue 450 to less than 495
Green 495 to less than 570
Yellow 570 to less than 590
Orange 590 to less than 620
Red 620 to 750

Write a program that reads a wavelength from the user and reports its color. Display
an appropriate error message if the wavelength entered by the user is outside of the
visible spectrum.
"""
violet_range = range(380, 450)
blue_range = range(450, 495)
green_range = range(495, 570)
yellow_range = range(570, 590)
orange_range = range(590, 620)
red_range = range(620, 751)

wavelength = int(input("Enter wavelength in nanometer"))

if wavelength < 380 or wavelength > 750:
    print("Error: wavelength is outside the visible spectrum.")
else:
    # determine color based on wavelength range
    if wavelength in violet_range:
        color = "violet"
    elif wavelength in blue_range:
        color = "blue"
    elif wavelength in green_range:
        color = "green"
    elif wavelength in yellow_range:
        color = "yellow"
    elif wavelength in orange_range:
        color = "orange"
    else:  
        color = "red"
        
    print(f"{wavelength}{color}.")

