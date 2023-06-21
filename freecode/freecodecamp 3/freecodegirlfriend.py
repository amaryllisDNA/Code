rateday=input("Rate your day on a scale going from 0 (terrible) to 10 (awesome).").int()
if rateday <= 3:
    print ("Your day was bad, you need to see your gf to feel better.")
else:
    if rateday<=7:
        print("You could make it a 10 if you saw your gf.")
    else:
        print("It can't be a 10 if you did not see your gf.")


###

cry=input("Has your gf been crying for more than 5 minutes ?(yes/no) ").lower()
if cry=="yes":
    badcare=input("Did your gf mention multiple time a lack of care, in the past few days ? (yes/no)").lower()
    if badcare=="yes":
        print("Your gf is having a breakdown and needs your support.")
    else:
        print("Difficult to say. Your gf might as well just be sweating a lot from her eyes.")
else:
    print("You're all good !")

###

sleepyboy=input("Are you feeling sleepy ? (yes/no)").lower()
sleepygirl=input("Is your gf feeling sleepy? (yes/no)").lower()

if sleepyboy=="yes" and sleepygirl=="yes":
    print("Alright ! Turn the lights off, tell her you love her and give her a goodnight kiss.")
if sleepyboy=="yes" and sleepygirl=="no":
    sad=input("Is your girlfriend feeling sad ?(yes/no)").lower()
    if sad=="yes":
        print("Give your gf cuddles and ask her why she's sad. Try to encourage her to fall asleep in your arms.")
    if sad=="no":
        print("Tell your gf you are going to sleep. Wish her a good night, give her a goodnight kiss.")
if sleepyboy=="no" and sleepygirl=="yes":
    print("Alright, tell her you love her, wish her a good night, give her a kiss and go on with your activities, but make sure not to be loud.")


###

kisses=int(input("How many kisses did you share today ? (number)"))
hugs = int(input("How many times did you hug today ? (number)"))
love=int(input("How many times did you tell her you love her today? number"))

total=kisses+hugs+love
if total<15:
    print("You should show your gf more attention.")
else: 
    print("Good job, your gf should be filled with love.")

###

hungry=input("Did your girlfriend ask if you are hungry ? (yes/no)").lower()

if hungry=="yes":
    print("Your girlfriend is hungry and waits for you to take her out. Ask her what she'd like to eat.")
else:
    mention=input("Did your girlfriend asked if you'd like something specific ? (yes/no)").lower()
    if mention=="yes":
        specific=input("What exactly ?").lower()
        print("Your girlfriend is hungry, she wants to eat", specific, ". Suggest to take her out to eat", specific,".")
    else:
        restaurant=input("Did your girlfriend tell you about some new restaurant she heard of ? (yes/no)").lower()
        if restaurant=="yes":
            specific=input("Which one exactly ?")
            print("Your girlfriend is hungry. Suggest to take her to", specific,".")
        else:
            print("It doesn't seem your girlfriend is starving. You can still ask her !")



