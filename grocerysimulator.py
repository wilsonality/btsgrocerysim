# grocery trip where you can
    # choose what to buy
    # choose how many to buy
    # and refill the fridge
        # so every day a random amount of food is consumed
        # maybe random events? (veggie day, hosting a bbq)
# game is lost when food total equals zero
    # diff foods worth more (meat > fruit)

# okay so i still need to add
    # purchasing unnecessary items
    # consumption random events


import random
import time

gameover = False
day = 1
dailymultiplier = 1 + float(day)/20
pricemultiplier = 1 + 1/random.randint(10,20)
# prices will increase between 5% to 10%

print("\n\n\n\n\nGame is loading...\n\n\n")

wallet = 40
moneyperquestion = 15
questionswrong = 0
goinghome = False

steakinventory = 0
applesinventory = 0
breadinventory = 0
cheeseinventory = 0
newsteak = 0
newapples = 0
newbread = 0
newcheese = 0
fridgeinventory = 5
todaystotal = 0

menu = ["steak", "apples", "bread", "cheese"]
grocery1 = "bananas"

# food values
    # steak = 4x ; apples = 1x ; bread = 2x ; cheese = 1x

# now some food prices

steakbase = 9
applesbase = 5
breadbase = 7
cheesebase = 2

steakprice = 9
applesprice = 5
breadprice = 7
cheeseprice = 2

# events!
members = ["Namjooon", "Seokjin", "Yoongi", "Hoseok", "Jimin", "Taehyung", "Jungkook"]
jiminsbbq = ["Jimin is hosting a barbeque party.",random.randint(3,5), menu[0], random.randint(3,5), menu[2]] # steak, bread
taekookpicnic = ["Taehyung and Jungkook are having a picnic.", random.randint(3,5), menu[0], random.randint(2,4), menu[1], random.randint(2,4), menu[2]] # steak, apples, bread
yoongisnacks = ["Yoongi asked you to bring him a snack in the studio.", random.randint(1,3), menu[1], random.randint(2,4), menu[3]] # apples, cheese
seokjindinner = ["Seokjin is hosting a dinner.", random.randint(5,7), menu[0]] # steak
birthdaymember = str(random.choice(members)) # picks the birthday person
birthdayparty = ["It's " + birthdaymember + "'s birthday today!", random.randint(3,5), menu[0], random.randint(2,4), menu[1], random.randint(1,3), menu[2], random.randint(4,6), menu[3]] # steak, apples, bread, cheeses
events = [jiminsbbq, taekookpicnic, yoongisnacks, seokjindinner, birthdayparty]
eventcounter = 0
todaysevent = 0
eventrng = 0


# i also need a coupon gen for random items (rng < 3 then save on total price)

# day cycle
def daybegin():
        print("\n\n\nGood morning. Day " + str(day) + " has begun.")
        time.sleep(2)
        print("It's time to do some work.")
        work()
        time.sleep(1)
        print("Work complete.")
        time.sleep(3)
        eventgen()
        time.sleep(3)
        todaysfood()
        time.sleep(2)
        findprice()
        time.sleep(3)
        shopping()
        eventactual()
        time.sleep(2)
        dayend()


def dayend():
        # the day ends, we add our food to the fridge and increase the day value
        global gameover
        global day
        global wallet
        global steakinventory
        global applesinventory
        global breadinventory
        global cheeseinventory
        global fridgeinventory
        global questionswrong
        questionswrong = 0
        print("\nDay " + str(day) + " has ended.")
        time.sleep(2)
        print("Adding today's purchases...")
        time.sleep (1)
        checkfridge()
        time.sleep(3)
        checkwallet()
        time.sleep (1)
        day = day + 1
        if gameover == False:
                print("The day has now ended. It is now Day " + str(day))
                daybegin()
        if gameover == True:
                gameend()
        pass


def gameend():
        print("Game over. Thank you for playing.")

# shopping events
def todaysfood():
        global grocery1
        global menu
        grocery1 = [random.choice(menu), random.randint(1,5)]
        # i wanna store it like: item[0], quantity[1]
        time.sleep(1)
        print(" ")
        print("Today, we need to restock on " + str(grocery1[0]) + ".")
def checkwallet():
        global wallet
        global gameover
        print("You have " + str(round(wallet,2)) + " money.")
        if wallet < 0:
            gameend()
            gameover = True
        pass
        
        
def shopping():
        # so we need to see wallet, decide how much to buy
            # i want to buy x, in y amount. this subtracts z from wallet
        # this will only include the choosing, bc i need to let ppl repeat it
        global wallet
        global menu
        global steakprice
        global newsteak
        global applesprice
        global newapples
        global breadprice
        global newbread
        global cheeseprice
        global newcheese
        global goinghome
        price = 0
        time.sleep(3)
        checkwallet()
        checkfridge()
        print("Today, we must buy " + str(grocery1[1]) + " " + grocery1[0] + ".")
        time.sleep(1)
        print(" ")
        if str(grocery1[0]) == "steak" :
                quantity = (input("How much steak do you want to buy? "))
                time.sleep(1)
                if int(quantity) < (grocery1[1]):
                        print("\nYou must buy more. Buy at least " + str(grocery1[1]) + grocery1[0] + ".")
                        # need to make quantity = grocery1[1]
                pass
                print("\nYou will buy " + quantity + " " + str(grocery1[0]) + " today.")
                price += float(steakprice) * float(quantity)
                time.sleep(1)
                print("\nThis will cost " + str(round(price,2)) + " money.")
                newsteak += int(quantity)
                pass
        if str(grocery1[0]) == "apples" :
                quantity = (input("How many apples do you want to buy? "))
                time.sleep(1)
                if int(quantity) < (grocery1[1]):
                        print("\nYou must buy more. Buy at least " + str(grocery1[1]) + grocery1[0] + ".")
                pass
                print("\nYou will buy " + quantity + " " + str(grocery1[0]) + " today.")
                time.sleep(1)
                price += float(applesprice) * float(quantity)
                print("\nThis will cost " + str(round(price,2)) + " money.")
                newapples += int(quantity)
                pass
        if str(grocery1[0]) == "bread" :
                quantity = (input("How much bread do you want to buy? "))
                time.sleep(1)
                if int(quantity) < (grocery1[1]):
                        print("\nYou must buy more. Buy at least " + str(grocery1[1]) + grocery1[0] + ".")
                pass
                print("\nYou will buy " + quantity + " " + str(grocery1[0]) + " today.")
                time.sleep(1)
                price += float(breadprice) * float(quantity)
                print("\nThis will cost " + str(round(price,2)) + " money.")
                newbread += int(quantity)
                pass
        if str(grocery1[0]) == "cheese" :
                quantity = (input("How much cheese do you want to buy? "))
                time.sleep(1)
                if int(quantity) < (grocery1[1]):
                        print("\nYou must buy more. Buy at least " + str(grocery1[1]) + grocery1[0] + ".")
                pass
                print("\nYou will buy " + quantity + " " + str(grocery1[0]) + " today.")
                time.sleep(1)
                price += float(cheeseprice) * float(quantity)
                print("\nThis will cost " + str(round(price,2)) + " money.")
                newcheese += int(quantity)
                pass
        time.sleep(1)
        wallet -= price
        checkwallet()
        # now to make your own purchases
        while goinghome == False:
                extrapurchase()
        else :
                wallet -= price
                time.sleep(1)
                print (" ")
                print("Let's go home.")
                time.sleep(2)
        

def extrapurchase():
        global wallet
        global menu
        global steakprice
        global newsteak
        global applesprice
        global newapples
        global breadprice
        global newbread
        global cheeseprice
        global newcheese
        global goinghome
        price = 0
        # okay uhh
        checkwallet()
        time.sleep(1)
        print(" ")
        purchase = input("Would you like to purchase something else?" )
        if purchase == "steak" :
                quantity = (input("How much steak do you want to buy? "))
                time.sleep(1)
                price += float(steakprice) * float(quantity)
                time.sleep(1)
                print("\nThis will cost " + str(round(price,2)) + " money.")
                newsteak += int(quantity)
        if purchase == "apples" :
                quantity = (input("How many apples do you want to buy? "))
                time.sleep(1)
                price += float(applesprice) * float(quantity)
                print("\nThis will cost " + str(round(price,2)) + " money.")
                newapples += int(quantity)
        if purchase == "bread" :
                quantity = (input("How much bread do you want to buy? "))
                time.sleep(1)
                price += float(breadprice) * float(quantity)
                print("\nThis will cost " + str(round(price,2)) + " money.")
                newbread += int(quantity)
        if purchase == "cheese" :
                quantity = (input("How much cheese do you want to buy? "))
                time.sleep(1)
                price += float(cheeseprice) * float(quantity)
                print("\nThis will cost " + str(round(price,2)) + " money.")
                newcheese += int(quantity)
        else :
                goinghome = True

def findprice():
        # we need a random multiplier to the base prices
        # but we also need to apply the daily multiplier
        global steakprice
        global applesprice
        global breadprice
        global cheeseprice
        print("Let's look at the prices today...")
        print(" ")
        time.sleep(2)
        steakprice = round(steakbase * pricemultiplier * dailymultiplier, 2)
        applesprice = round(applesbase * pricemultiplier * dailymultiplier, 2)
        breadprice = round(breadbase * pricemultiplier * dailymultiplier, 2)
        cheeseprice = round(cheesebase * pricemultiplier * dailymultiplier, 2)
        print("Steak: " + str(steakprice) + "\nApples: " + str(applesprice) + "\nBread: " + str(breadprice) + "\nCheese: " + str(cheeseprice))
        print(" ")
def checkfridge():
        # we need to calculate fridge population and see if < 0
        # food values
            # steak = 4x ; apples = 1x ; bread = 2x ; cheese = 1x
        global fridgeinventory
        global steakinventory
        global applesinventory
        global breadinventory
        global cheeseinventory
        global newsteak
        global newapples
        global newbread
        global newcheese
        global gameover
        steakinventory += newsteak
        applesinventory += newapples
        breadinventory += newbread
        cheeseinventory += newcheese
        fridgeinventory = steakinventory*4 + applesinventory + breadinventory*2 + cheeseinventory
        print("Checking fridge...")
        print (" ")
        time.sleep(1)
        if steakinventory < 0:
                print("You have run out of steak. The game is lost.")
                gameover = True
        if applesinventory < 0:
                print("You have run out of apples. The game is lost.")
                gameover = True
        if breadinventory < 0:
                print("You have run out of bread. The game is lost.")
                gameover = True
        if cheeseinventory < 0:
                print("You have run out of cheese. The game is lost.")
                gameover = True
        if fridgeinventory <= 0:
                if day != 1:
                        print("You have reached zero food. The game is lost.")
                        gameover = True
                pass
        else:
                print ("You have " + str(fridgeinventory) + " food.")
                print (" ")
                time.sleep(1)
                print ("You have " + str(steakinventory) + " steak.")
                print (" ")
                time.sleep(1)
                print ("You have " + str(applesinventory) + " apples.")
                print (" ")
                time.sleep(1)
                print ("You have " + str(breadinventory) + " bread.")
                print (" ")
                time.sleep(1)
                print ("You have " + str(cheeseinventory) + " cheese.")
                

# work meta
def work():
        # diff questions that generate money
        # can't get more than 3 wrong
        global moneyperquestion
        global questionswrong
        global todaystask
        print(" ")
        time.sleep(2)
        workbonus = random.randint(1,5)
        if workbonus > 3:
                 moneyperquestion += (workbonus-2)*10
                 print("A bonus has been found today.")
        else:
                  print("No bonus has been found today.")
        time.sleep(2)
        print (" ")
        print("Each task is worth " + str(moneyperquestion) + " money.")
        print (" ")
        time.sleep(2)
        while questionswrong < 3:
            print (" ")
            print("Finding work for today...")
            print(" ")
            time.sleep(1)
            generatework()
            time.sleep(3)
        else:
            print (" ")
            print("You have failed at 3 tasks. Your work has ended.")
            time.sleep(1)
            print(" ")
            checkwallet()
            moneyperquestion = 10    
def generatework():
        global todaystask
        todaystask = random.randint(1, 2)
        if todaystask == 1:
            jungkooktrivia()
        pass
        if todaystask == 2:
            namjoonsplant()


# kinds of work
def jungkooktrivia():
        global wallet
        global moneyperquestion
        global questionswrong
        print("It's time for some Jungkook trivia!")
        time.sleep(2)
        question = random.randint(1,2)
        if question == 1:
               print("Jungkook is thinking of a number between 1 and 3. What number is Jungkook thinking of?")
               jungkooknumber = random.randint(1,3)
               time.sleep(1)
               if input() == str(jungkooknumber):
                        wallet += moneyperquestion
                        time.sleep(1)
                        print("Jungkook is telling Dispatch that you can read minds...")
               else:
                        questionswrong += 1
                        time.sleep(1)
                        print("Oops! Jungkook was thinking of the number " + str(jungkooknumber) + ".")
        pass
        if question == 2:
                print ("Who is Jungkook's favorite member?")
                answer2 = "Namjoon"
                if input() == answer2:
                        wallet += moneyperquestion
                        time.sleep(1)
                        print ("Correct! Jungkook's favorite member is Namjoon.")
                else:
                        questionswrong += 1
                        time.sleep(1)
                        print("Wrong. Jungkook's favorite member is Namjoon. You have gotten " + str(questionswrong) + " questions wrong.")
        pass
def namjoonsplant():
        global wallet
        global moneyperquestion
        global questionswrong
        print("Namjoon asked you to water his bonsai. Hoseok left the watering can somewhere in the house, so you have to find it. \nYou only have time to search one room. Choose wisely.")
        rooms = ["kitchen", "bathroom", "dining", "bedroom", "garage"]
        time.sleep(3)
        print("The rooms are as following:\n %s." % [rooms])
        time.sleep(1)
        wateringcan = random.choice(rooms)
        if input() == wateringcan:
                        wallet += moneyperquestion
                        time.sleep(1)
                        print("Nice job! You found the watering can. Namjoon thanks you for watering his plant.")
        else:
                        questionswrong += 1
                        time.sleep(1)
                        print("Oh no! Hoseok left the watering can in the " + wateringcan + ".")
        pass


# random events # there has to be a warning after the day starts so ppl know what to buy # and then a consumption event after shopping

def eventgen ():
        # list of random events, bday happens every 3
        global menu
        global events
        global eventcounter
        global eventrng
        global day
        global todaysevent
        global jiminsbbq
        global taekookpicnic
        global yoongisnacks
        global seokjindinner
        global birthdayparty
        global birthdaymember
        time.sleep(2)
        print(" ")
        if day <= 3:
                todaysevent = random.choice(events)
                # food is predetermined, quantity will be rolled
                eventrng = random.randint(0,2)
                if eventrng > 0:
                        # having different consumptions means i'll have to make a diff prompt for each event...
                        print(" ")
                        while day < 3 and todaysevent == birthdayparty :
                                todaysevent = random.choice(events)
                        if eventcounter == 3:
                                todaysevent = birthdayparty
                                eventcounter = 0
                        if todaysevent == jiminsbbq :
                                print(todaysevent[0] + " This will consume " + str(todaysevent[1]) + " " + str(todaysevent[2]) + " and " + str(todaysevent[3]) + " " + str(todaysevent[4]) + ".")
                        if todaysevent == taekookpicnic : 
                                print(todaysevent[0] + " This will consume " + str(todaysevent[1]) + " " + str(todaysevent[2]) + ", " + str(todaysevent[3]) + " " + str(todaysevent[4]) + ", and " + str(todaysevent[5]) + " " + str(todaysevent[6]) +  ".")
                        if todaysevent == yoongisnacks :
                                  print(todaysevent[0] + " This will consume " + str(todaysevent[1]) + " " + str(todaysevent[2]) + " and " + str(todaysevent[3]) + " " + str(todaysevent[4]) + ".")
                        if todaysevent == seokjindinner :
                                print(todaysevent[0] + " This will consume " + str(todaysevent[1]) + " " + str(todaysevent[2]) + ".")
                        if todaysevent == birthdayparty :
                                if birthdaymember ==  "seokjin" :
                                        todaysevent[1] *= 2
                                        todaysevent[3] *= 2
                                        todaysevent[5] *= 2
                                        todaysevent[7] *= 2
                                        print(todaysevent[0] + " This will consume " + str(todaysevent[1]) + " " + str(todaysevent[2]) + ", " + str(todaysevent[3]) + " " + str(todaysevent[4]) + ", " + str(todaysevent[5]) + " " + str(todaysevent[6]) + ", and " + str(todaysevent[7]) + " " + str(todaysevent[8]) + " .")
                                pass
                                print(todaysevent[0] + " This will consume " + str(todaysevent[1]) + " " + str(todaysevent[2]) + ", " + str(todaysevent[3]) + " " + str(todaysevent[4]) + ", " + str(todaysevent[5]) + " " + str(todaysevent[6]) + ", and " + str(todaysevent[7]) + " " + str(todaysevent[8]) + " .")
                        if todaysevent != birthdayparty :
                                eventcounter += 1
                        pass
                else:
                        print("It's quiet in the house today...")
        pass

def eventactual ():
        # now we need to consume the food (change to new-xxxx)
        # let's do it by event type to get all types of food
        global menu
        global events
        global todaysevent
        global jiminsbbq
        global taekookpicnic
        global yoongisnacks
        global seokjindinner
        global birthdayparty
        global birthdaymember
        global newsteak
        global newapples
        global newbread
        global newcheese
        if todaysevent == jiminsbbq :
                newsteak -= todaysevent[1]
                newbread -= todaysevent[3]
                print("Jimin sends his thanks for helping with the barbeque.")
        if todaysevent == taekookpicnic :
                newsteak -= todaysevent[1]
                newapples -= todaysevent[3]
                newbread -= todaysevent[5]
                print("Taehyung brought you a flower from his picnic with Jungkook.")
        if todaysevent == yoongisnacks :
                newapples -= todaysevent[1]
                newcheese -= todaysevent[3]
                print("Yoongi appreciates the snack you brought him.")
        if todaysevent == seokjindinner :
                newsteak -= todaysevent[1]
                print("Seokjin's dinner went as well as his witty puns. (In one end, and out the other)")
        if todaysevent == birthdayparty :
                newsteak -= todaysevent[1]
                newapples -= todaysevent[3]
                newbread -= todaysevent[5]
                newcheese -= todaysevent[7]
                print(birthdaymember + " thanks you for hosting their birthday!")
        pass

daybegin()
