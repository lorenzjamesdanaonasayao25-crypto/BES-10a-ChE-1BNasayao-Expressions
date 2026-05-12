#This project is personalized in a way for me to keep track as to how much my commisions would cost me. Since ifs functions are too advanced for this
#topic, the hourly rate can be freely typed by the user.

inyou = input('Hello Content Editor! Please state your name: ')
inpR = input('Enter Hourly Rate of your commision: ')
inpH = input('Enter Work Done in Hours (Minutes not included): ')
inpM = input('Enter Work Done in Minutes: ')
    #input variables

pay = float(inpH)*float(inpR) + (float(inpM)/60)*float(inpR)
    #formula for payment
    #the payment for each hour "float(inpH)*float(inpR)" is added to the payment for each minute "float(inpH)*(float(inpM)/60)"
    #which is why it is instructed in the input that the Work Done in Hours, the minutes are not included.
    #It is divided by 60 because the minutes need to be converted into hours for the payment to make sense.

print("Content Editor:", (inyou))
print("Number of hours done:", float(inpH), "hours and", float(inpM), ("minutes"))
print("Hourly Rate:", float(inpR))
print("Thank You! Here is your pay for the video:", int(pay))