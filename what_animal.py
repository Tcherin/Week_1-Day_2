# SET animal = INPUT "What animal are you?"
# IF animal is "chicken"
#   THEN PRINT "This is my favourite animal!"
# ELSE IF animal is "dog"
#  THEN PRINT "Ilove dogs!"
# ELSE
#    PRINT "Sadly not my favourite."
# END

animal = input("What animal are you?")

if animal == "chicken":
    print("This is my favourite animal!")
elif animal == "dog":
    print("I love dogs!")
else:
    print("Sadly not my favourite.")

result = "pass" if animal == "chicken" else "fail"