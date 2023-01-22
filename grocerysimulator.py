# grocery trip where you can
    # choose what to buy
    # choose how many to buy
    # and refill the fridge
        # so every day a random amount of food is consumed
        # maybe random events? (veggie day, hosting a bbq)
# game is lost when food total equals zero
    # this means i need to have a food counter
    # diff foods worth more (meat > fruit)

# okay so i still need to add
    # purchasing unnecessary items
    # consumption random events


import random
import time

gameover = False
day = 1
dailymultiplier = 1 + float(day)/40
pricemultiplier = 1 + 1/random.randint(10,20)
# prices will increase between 5% to 10%

print("\n\n\nGame is loading...\n\n\n")

wallet = 10
moneyperquestion = 15
questionswrong = 0

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

steakbase = 10
applesbase = 5
breadbase = 7
cheesebase = 2

steakprice = 10
applesprice = 5
breadprice = 7
cheeseprice = 2

# i need a check-if-we-are-starving function LMAO
# i also need a day start function
# i also need a coupon gen for random items (rng < 3 then save on total price)
# i need an eventgen for work to get bonuses DONE

# day cycle
def daybegin():
        print("\n\n\nGood morning. Day " + str(day) + " has begun.")
        time.sleep(1)
        print("It's time to do some work.")
        work()
        print("Work complete.")
        time.sleep(2)
        todaysfood()
        time.sleep(2)
        findprice()
        time.sleep(2)
        shopping()
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
        print("The day has now ended. It is now Day " + str(day))
        if gameover == False:
                daybegin()
        else:
                gameend()
    
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
        checkwallet()
        print("Today, we must buy " + str(grocery1[1]) + " " + grocery1[0] + ".")
        time.sleep(1)
        print(" ")
        if str(grocery1[0]) == "steak" :
                global steakprice
                global newsteak
                quantity = (input("How much steak do you want to buy? "))
                time.sleep(1)
                if int(quantity) < (grocery1[1]):
                        print("\nYou must buy more. Buy at least " + str(grocery1[1]) + grocery1[0] + ".")
                pass
                print("\nYou will buy " + quantity + " " + str(grocery1[0]) + " today.")
                price = float(steakprice) * float(quantity)
                time.sleep(1)
                print("\nThis will cost " + str(round(price,2)) + " money.")
                newsteak += int(quantity)
                pass
        if str(grocery1[0]) == "apples" :
                global applesprice
                global newapples
                quantity = (input("How many apples do you want to buy? "))
                time.sleep(1)
                if int(quantity) < (grocery1[1]):
                        print("\nYou must buy more. Buy at least " + str(grocery1[1]) + grocery1[0] + ".")
                pass
                print("\nYou will buy " + quantity + " " + str(grocery1[0]) + " today.")
                time.sleep(1)
                price = float(applesprice) * float(quantity)
                print("\nThis will cost " + str(round(price,2)) + " money.")
                newapples += int(quantity)
                pass
        if str(grocery1[0]) == "bread" :
                global breadprice
                global newbread
                quantity = (input("How much bread do you want to buy? "))
                time.sleep(1)
                if int(quantity) < (grocery1[1]):
                        print("\nYou must buy more. Buy at least " + str(grocery1[1]) + grocery1[0] + ".")
                pass
                print("\nYou will buy " + quantity + " " + str(grocery1[0]) + " today.")
                time.sleep(1)
                price = float(breadprice) * float(quantity)
                print("\nThis will cost " + str(round(price,2)) + " money.")
                newbread += int(quantity)
                pass
        if str(grocery1[0]) == "cheese" :
                global cheeseprice
                global newcheese
                quantity = (input("How much cheese do you want to buy? "))
                time.sleep(1)
                if int(quantity) < (grocery1[1]):
                        print("\nYou must buy more. Buy at least " + str(grocery1[1]) + grocery1[0] + ".")
                pass
                print("\nYou will buy " + quantity + " " + str(grocery1[0]) + " today.")
                time.sleep(1)
                price = float(cheeseprice) * float(quantity)
                print("\nThis will cost " + str(round(price,2)) + " money.")
                newcheese += int(quantity)
                pass
        time.sleep(1)
        wallet -= price
        checkwallet()



def findprice():
        # we need a random multiplier to the base prices
        # but we also need to apply the daily multiplier
        global steakprice
        global applesprice
        global breadprice
        global cheeseprice
        print("Let's look at the prices today...")
        print(" ")
        time.sleep(1)
        steakprice = round(steakbase * pricemultiplier * dailymultiplier, 2)
        applesprice = round(applesbase * pricemultiplier * dailymultiplier, 2)
        breadprice = round(breadbase * pricemultiplier * dailymultiplier, 2)
        cheeseprice = round(cheesebase * pricemultiplier * dailymultiplier, 2)
        print( "Today's prices are\nSteak: " + str(steakprice) + "\nApples: " + str(applesprice) + "\nBread: " + str(breadprice) + "\nCheese: " + str(cheeseprice))
        print(" ")
def checkfridge():
        # we need to calculate fridge population and see if > 0
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
        steakinventory += newsteak
        applesinventory += newapples
        breadinventory += newbread
        cheeseinventory += newcheese
        fridgeinventory = steakinventory*4 + applesinventory + breadinventory*2 + cheeseinventory
        print("Checking fridge...")
        time.sleep(1)
        if fridgeinventory < 0:
                print("You have reached zero food. The game is lost.")
        else:
                print ("You have " + str(fridgeinventory) + " food.")
                print ("You have " + str(steakinventory) + " steak.")
                print ("You have " + str(applesinventory) + " apples.")
                print ("You have " + str(breadinventory) + " bread.")
                print ("You have " + str(cheeseinventory) + " cheese.")
                



# work meta
def work():
        # diff questions that generate money
        # can't get more than 3 wrong
        global moneyperquestion
        global questionswrong
        global todaystask
        print(" ")
        workbonus = random.randint(1,5)
        if workbonus > 3:
                 moneyperquestion += (workbonus-2)*10
                 print("A bonus has been found today.")
        else:
                  print("No bonus has been found today.")
        print("Each task is worth " + str(moneyperquestion) + " money.")
        print (" ")
        time.sleep(1)
        while questionswrong < 3:
            print("Finding work for today...")
            print(" ")
            time.sleep(1)
            generatework()
            time.sleep(2)
        else:
            print("You have failed at 3 tasks. Your work has ended.")
            time.sleep(1)
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
# i need a third later
    # maybe making a song with yoongi
def jungkooktrivia():
        global wallet
        global moneyperquestion
        global questionswrong
        print("It's time for some Jungkook trivia!")
        time.sleep(1)
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
        print("Namjoon asked you to water his bonsai. Hoseok left the watering can somewhere in the house, so you have to find it. \nYou only have time to search one room, so choose wisely.")
        rooms = ["kitchen", "bathroom", "dining", "bedroom", "garage"]
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


daybegin()
