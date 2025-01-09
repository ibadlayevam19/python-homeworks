def convert_cel_to_far(cel):
    return cel*(9/5)+32
def convert_far_to_cel(far):
    return (far-32)*5/9
f=input("Enter a temperature in degrees F: ")
fc=round(convert_far_to_cel(float(f)),2)
print(f'{f} degrees F = {fc} degrees C')
c=input("Enter a temperature in degrees C: ")
cf=round(convert_cel_to_far(float(c)),2)
print(f'{c} degrees C = {cf} degrees F')