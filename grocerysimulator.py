import random
import time

gameover = False
day = 0
eventcounter = 0
dailymultiplier = 1
pricemultiplier = 1

wallet = int(30)
moneyperquestion = 15
questionswrong = 0
fridgeinventory = 0

menu = []
class Foodtype:
    def __init__(self, name, base, inventory, cart, price) -> None:
        self.name = name
        self.base = base # subject to price mulitipliers
        self.inventory = inventory # how much is in the fridge
        self.cart = cart # how much is in the cart
        self.price = price # final price we see at the store
        menu.append(self)

steak = Foodtype("steak", 10, 0, 0, 10)
apples = Foodtype("apples", 5, 0, 0, 5)
bread = Foodtype("bread", 7, 0, 0, 7)
cheese = Foodtype("cheese", 2, 0, 0, 2)

class Purchase:
     def __init__(self, food, amount) -> None:
          self.food = food
          self.amount = amount

dailygrocery = Purchase(steak, 4)

# day cycle

def sunrise(): # we need to gen price multipliers
     global dailymultiplier
     global pricemultiplier
     dailymultiplier = 1 + float(day-1)/40
     pricemultiplier = 1 + 1/random.randint(10,20)
     print("\nThe sun is rising.")
     time.sleep(2)
def sunset(): # day end stuff
      global day
      print("\nDay " + str(day) + " has come to an end")
      day += 1
def gameend():
        gameover = False
        print("Game over. Thank you for playing.")
        # print("\nTesting mode.")

def cycle():
      time.sleep(1)
      print("\n\n\nGame is loading...\n\n\n")
      time.sleep(1)
      sunrise()
      workmeta()
      todaysfood()
      eventpicker()
      shopping()
      print("Heading home...")
      time.sleep(2)
      eventactual()
      openthefridge()
      sunset()
      time.sleep(5)


# HOW TO CHECK THE FRIDGE?

def unloadgroceries():
     global fridgeinventory
     global menu
     global Foodtype
     # so we need to add new groceries
     for Foodtype in menu:
          Foodtype.inventory += Foodtype.cart
          # YAY

def openthefridge():
     global fridgeinventory
     global menu
     global Foodtype
     time.sleep(2)
     for Foodtype in menu:
          if Foodtype.inventory < 1 :
               print("Oh no! Looks like you ran out of " + Foodtype.name + ".")
               gameend()
          else :
               print("We have " + str(Foodtype.inventory) + " " + Foodtype.name + ".")

# shoppingmeta

def todaysfood():
    global menu
    global dailygrocery
    global foodie
    global Purchase
    foodie = random.choice(menu)
    dailygrocery = Purchase(foodie, random.randint(1,5))
    print("\nToday we need to restock on " + dailygrocery.food.name + ".")
    time.sleep(5)
def checkwallet():
        global wallet
        global gameover
        print("You have " + str(round(wallet,2)) + " money.")
        time.sleep(2)
        if wallet < 0:
            gameend()
        pass
def pricegen():
     # multiplier time!
     global menu
     global Foodtype
     global dailymultiplier
     global pricemultiplier
     print("\nLet's look at the prices today...")
     time.sleep(1)
     for Foodtype in menu:
          Foodtype.price = round(Foodtype.base * dailymultiplier * pricemultiplier, 2)
          print ("\nToday, " + Foodtype.name + " will cost " + str(Foodtype.price) + ".")
          pass
def shopping():
     global wallet
     global menu
     global dailygrocery
     global Purchase
     global Foodtype
     checkwallet()
     time.sleep(2)
     print("\n")
     todaysfood()
     time.sleep(2)
     print("\n")
     pricegen()
     print("\nToday, we must buy "  + str(dailygrocery.amount) +  " " + str(dailygrocery.food.name) + ".") # okay
     time.sleep(1)
     dailygrocery.food.cart = int(input("\nHow much/many " + dailygrocery.food.name + " do you want to buy?")) # hnnnnn
     if dailygrocery.food.cart < dailygrocery.amount :
          print("\nYou must buy more. You will buy " + str(dailygrocery.amount) + " " + dailygrocery.food.name + ".")
          dailygrocery.food.cart = dailygrocery.amount
     else:
          print("\nBuying " + str(dailygrocery.food.cart) + " " + str(dailygrocery.food.name) + ".")
          wallet -= dailygrocery.food.price*dailygrocery.amount
     checkwallet()
     consumerism = input("\nWould you like to buy something else? \n Yes or No\n")
     time.sleep(1)
     consumerism = input("\nWhat would you like to buy?")
     for Foodtype in menu :
         if consumerism == Foodtype.name :
              Foodtype.cart = input("\nHow much/many " + Foodtype.name + " do you want to buy?")
              time.sleep(1)
              print("Purchasing " + Foodtype.name + "...")
              wallet -= round(float(Foodtype.cart) * float(Foodtype.price), 2)
              time.sleep(2)
              checkwallet()
         pass
     time.sleep(2)
              
# events

eventindex = []
class Event:
     def __init__(self, prompt, target, level) -> None:
          self.prompt = prompt
          self.target = target
          self.level = level
          eventindex.append(self)

memberindex = ["Namjooon", "Seokjin", "Yoongi", "Hoseok", "Jimin", "Taehyung", "Jungkook"]
birthdaymember = "\nim sorry for my fault.." # double check bdaygen
birthdayparty = Event("It's " + birthdaymember + "'s birthday today!", [steak, apples, bread, cheese], [random.randint(3,5), random.randint(2,4), random.randint(1,3), random.randint(4,6)])

jiminsbbq = Event("\nJimin is hosting a barbeque party.", [steak, bread], [random.randint(3,5), random.randint(3,5)])
taekookpicnic = Event("\nTaehyung and Jungkook are having a picnic.", [steak, apples, bread], [random.randint(3,5), random.randint(2,4), random.randint(2,4)])
yoongisnacks = Event("\nYoongi asked you to bring him a snack in the studio.", [apples, cheese], [random.randint(1,3), random.randint(2,4)])
seokjindinner = Event("\nSeokjin is hosting a dinner.", [steak], random.randint(5,7))
namseoklunch = "ayo hitman bang introduces" # placeholder for event idea
todaysevent = 0
eventrng = 0

def eventpicker():
     global todaysevent
     global eventrng
     global eventcounter
     global birthdaymember
     global Foodtype
     global Event
     birthdaymember = random.choice(memberindex)
     if day >= 2:
          todaysevent = random.choice(eventindex)
          eventrng = random.randint(0,1)
          if eventrng == 0 :
               print("\nLooks like something is happening today...")
               eventcounter += 1
               while day < 5 and todaysevent == birthdayparty :
                    todaysevent = random.choice(eventindex)
               if eventcounter == 3:
                     todaysevent = birthdayparty
                     eventcounter = 0
                     pass
               print("\n" + todaysevent.prompt)
               if len(todaysevent.target) > 1:
                     print("You must buy :")
                     print (*todaysevent.target, sep = ", " + ".")
               else :
                     print("You must buy " + todaysevent.target.name + ".")             
def eventactual():
     global todaysevent # we get eventotd and update the fridge
     global menu
     global eventindex
     global Foodtype
     global birthdaymember
     eventcatalog = 0
     print(todaysevent.prompt)
     time.sleep(1)
     if todaysevent == birthdayparty :
          print("\nHappy birthday " + birthdaymember + "!")
     for Foodtype in todaysevent.target :
          Foodtype.inventory -= todaysevent.level[eventcatalog]
          eventcatalog += 1
          print("\n" + Foodtype.name + "   " + str(Foodtype.inventory))
          pass
     eventcatalog = 0
     openthefridge() # that was painful

# work meta

def workmeta():
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
        time.sleep(2)
        while questionswrong < 3:
            print("\nFinding work for today...")
            print(" ")
            time.sleep(2)
            generatework()
            time.sleep(3)
        else:
            print("You have failed at 3 tasks. Your work has ended.")
            time.sleep(2)
            checkwallet()
            moneyperquestion = 10    
def generatework():
        global todaystask
        todaystask = random.randint(1, 2)
        if todaystask == 1:
            jungkooktrivia()
        if todaystask == 2:
            namjoonsplant()
def jungkooktrivia():
        global wallet
        global moneyperquestion
        global questionswrong
        print("\nIt's time for some Jungkook trivia!")
        time.sleep(1)
        question = random.randint(1,2)
        if question == 1:
               print("\nJungkook is thinking of a number between 1 and 3. What number is Jungkook thinking of?")
               jungkooknumber = random.randint(1,3)
               time.sleep(1)
               if input() == str(jungkooknumber):
                        wallet += moneyperquestion
                        time.sleep(1)
                        print("\nJungkook is telling Dispatch that you can read minds...")
               else:
                        questionswrong += 1
                        time.sleep(1)
                        print("\nOops! Jungkook was thinking of the number " + str(jungkooknumber) + ".")
        pass
        if question == 2:
                print ("\nWho is Jungkook's favorite member?")
                answer2 = "Namjoon"
                if input() == answer2:
                        wallet += moneyperquestion
                        time.sleep(1)
                        print ("\nCorrect! Jungkook's favorite member is Namjoon.")
                else:
                        questionswrong += 1
                        time.sleep(1)
                        print("\nWrong. Jungkook's favorite member is Namjoon. You have gotten " + str(questionswrong) + " questions wrong.")
        pass
def namjoonsplant():
        global wallet
        global moneyperquestion
        global questionswrong
        print("\nNamjoon asked you to water his bonsai. Hoseok left the watering can somewhere in the house, so you have to find it. \nYou only have time to search one room, so choose wisely.")
        rooms = ["kitchen", "bathroom", "dining", "bedroom", "garage"]
        print("\nThe rooms are as following:\n %s." % [rooms])
        time.sleep(1)
        wateringcan = random.choice(rooms)
        if input() == wateringcan:
                        wallet += moneyperquestion
                        time.sleep(1)
                        print("\nNice job! You found the watering can. Namjoon thanks you for watering his plant.")
        else:
                        questionswrong += 1
                        time.sleep(1)
                        print("\nOh no! Hoseok left the watering can in the " + wateringcan + ".")

cycle()
