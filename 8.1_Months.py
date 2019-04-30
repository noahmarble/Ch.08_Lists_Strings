'''
MONTHS PROGRAM
--------------
Write a user-input statement where a user enters a month number 1-13.
Using the starting string below in your program, print the three month abbreviation 
for the month number that the user enters. Keep repeating this until the user enters 13 to quit.
Once the user quits, print "Goodbye!"

months = "JanFebMarAprMayJunJulAugSepOctNovDec"

'''
months = "JanFebMarAprMayJunJulAugSepOctNovDec"
done=False
while not done:
    userinput = int(input("enter a month numbers 1-12:"))
    print(months[(3*userinput-3):(3*userinput)])
    if userinput==13:
        break