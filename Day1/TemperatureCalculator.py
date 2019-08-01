name = input("Enter patient's name:")
a = float(input("Enter patient's temperature:"))
norm_temp=36.9
print("%s's temperature is %.1f degree celsius from %.2f." %(name,a-norm_temp, norm_temp))