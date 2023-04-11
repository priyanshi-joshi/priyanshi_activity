"""
Problem -II
Electromagnetic radiation can be classified into one of 7 categories according to its
frequency, as shown in the table below:

Radio Waves Less than 3 × 10^9
Microwaves 3 × 10^9 to less than 3 × 10^12
Infrared Light 3 × 10^12 to less than 4.3 × 10^14
Visible Light 4.3 × 10^14 to less than 7.5 × 10^14
Ultraviolet Light 7.5 × 10^14 to less than 3 × 10^17
X-Rays 3 × 10^17 to less than 3 × 10^19
Gamma Rays 3 × 10^19 or more

Write a program that reads the frequency of some radiation from the user and
displays name of the radiation as part of an appropriate message.
"""
radio_range = range(0, 3*10**9)
microwave_range = range(3*10**9, 3*10**12)
infrared_range = range(3*10**12, 4.3*10**14)
visible_range = range(4.3*10**14, 7.5*10**14)
ultraviolet_range = range(7.5*10**14, 3*10**17)
xray_range = range(3*10**17, 3*10**19)
gamma_range = range(3*10**19, float("inf"))

# read frequency from user
frequency = float(input("Enter frequency (in Hz): "))

# determine the category of the radiation based on its frequency range
if frequency in radio_range:
    category = "Radio Waves"
elif frequency in microwave_range:
    category = "Microwaves"
elif frequency in infrared_range:
    category = "Infrared Light"
elif frequency in visible_range:
    category = "Visible Light"
elif frequency in ultraviolet_range:
    category = "Ultraviolet Light"
elif frequency in xray_range:
    category = "X-Rays"
else:  # frequency in gamma_range
    category = "Gamma Rays"
    
print(f"The radiation with frequency {frequency:.2e} Hz is classified as {category