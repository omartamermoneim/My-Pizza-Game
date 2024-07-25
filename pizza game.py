import time
import random
def yes_or_no() :  #This function makes yes or no choice for user
    print ("1 for Yes")
    time. sleep(1)
    print ("2 for No")
    time. sleep(1)


def print_fun(m): #This function print and wait 1 second
    print (m)
    time. sleep(1)


def sup_or_comp(): #This function gives user choice to enter supermarket or competition
    print("1 for supermarket")
    time. sleep(1)
    print("2 for competition")
    
    
def again (): #This function make user play again
    while True:
        print_fun("play again?")
        again = input (">")
        if again == "yes":
            main()
            break
        elif again == "no" :
            print ("bye")
            exit()
            break
        else:
            print("please enter yes or no")


def main(): # This is the main game
    money = 0
    print ("Hi!,please Enter your name")
    time. sleep(1)
    name = input (">")
    if len(name) <= 2 : # check if the name of user small or not
        print ("Please inter your real name (more than 2 letters)")
        time. sleep(1)
        name = input ("Enter name here:")
        if len(name) <= 2 : # call user "user1" to start game
            print ("i will just call you  user1")
            name = "User1"
    while True:
        print ("hi " + name + "!,Are you ready?") #check if the user is ready
        time. sleep(1)
        yes_or_no()
        resp = input (">")
        if resp == "1":
            break
        else:
            print ("please be ready (enter1)")
    while True: # start of the game
        if resp == "1" :
            print_fun("You wake up in your home and you want to eat pizza, (total money collected "+str(money)+"$)")
            while True:
                print_fun("Do you want to Continue sleeping ? ")
                yes_or_no()
                res = input (">")
                if res == "2":
                    break
                elif res == "1":
                    break
            while True:
                if res == "1": # makes user lose bec. he didnot get the pizza
                    print_fun("your hunger now is 100% you lost,(total money collected "+str(money)+"$)")
                    again ()
                elif res == "2":
                    print_fun("you wake up and get ready to get your pizza, (total money collected "+str(money)+"$)")
                    print_fun("from the pizza shop but you need to get money")
                    print_fun("I think it costs 50$")
                    print_fun("While you are walking you find competition ")
                    print_fun("near to the super market")
                    while True:
                        print_fun("Which one do you want to enter")
                        sup_or_comp()
                        respo = input (">")
                        if respo == "1": #makes player in supermarket
                            print_fun("worker:Hi "+name+"!")
                            print_fun(name+":I want to work with you")
                            print_fun("worker:sure we need casher")
                            print_fun("Now you are a casher")
                            print_fun("worker:take this list")
                            print_fun("1k Rice = 5$")
                            print_fun("Egg = 3$")
                            print_fun("Chicken = 10$")
                            print_fun("1l Milk = 7$")
                            print_fun("Apple = 1$")
                            print_fun("frist customer:hi I bought 10 apples and 3 eggs,how much are they")
                            fircu = input (">")
                            if fircu == "19":
                                money = money + 10
                                print_fun("(total money collected "+str(money)+"$)")
                                print_fun("second customer:hi I bought 10k of rice and 2 Chickens and 5L of milk,how much are they")
                                seccu = input(">")
                                if seccu == "105":
                                    money = money + 15
                                    print_fun("(total money collected "+str(money)+"$)")
                                    print_fun("third customer:hi I bought 15k of rice and 3 Chickens and 3L of milk  and 30 apples and have 10$ discount ,how much are they")
                                    thicu = input(">")
                                    if thicu == "146":
                                        money = money + 15
                                        print_fun("(total money collected "+str(money)+"$)")
                                        print_fun("worker:very good you made it! now you can take your money here" +str(money)+"$")
                                        print_fun("I think I shoud go to pizza shop and try to get discount")
                                        print_fun("Pizza worker : hi,"+ name +" ,how can I help you")
                                        print_fun("1.Spin the lucky Wheel")
                                        print_fun("2.Buy pizza")
                                        resp = input(">")
                                        while True:
                                            if resp == "1":
                                                price = 50
                                                spin = [20,10,5]
                                                luspin = int(random.choice(spin))
                                                price = price - luspin
                                                print ("You win " + str(luspin) + "$ discount")
                                                if price <= money:
                                                    print ("Now I can buy the pizza")
                                                    print ("you won!")
                                                    print_fun("(total money collected "+str(money)+"$)")
                                                    again ()
                                                else:
                                                    print ("you lost :(")
                                                    print_fun("(total money collected "+str(money)+"$)")
                                                    again ()
                                            if resp == "2":
                                                price = 50
                                                if price <= money:
                                                    print ("you won!")
                                                    print_fun("(total money collected "+str(money)+"$)")
                                                    again ()
                                                else:
                                                    print ("you lost :(")
                                                    print_fun("(total money collected "+str(money)+"$)")
                                                    again ()
                                    else:
                                        print ("you lost :(")
                                        print_fun("(total money collected "+str(money)+"$)")
                                        again ()
                                else:
                                    print ("you lost :(")
                                    print_fun("(total money collected "+str(money)+"$)")
                                    again ()    
                            else:
                                print ("you lost :(")
                                print_fun("(total money collected "+str(money)+"$)")
                                again ()
                        if respo == "2":#makes the player enter the competition
                            print_fun("the organizer:welcom I will ask you 3 Q if you aswered you get 40$ ")
                            print_fun("Q1:A bat and a ball cost $1.10 in total. The bat costs $1 more than the ball. How much cents does the ball cost?")
                            respon = input(">")
                            if respon == "10":
                                money = money + 10
                                print_fun("(total money collected "+str(money)+"$)")
                                print_fun("Q2:If it takes five machines five minutes to make five widgets, how long would it take 100 machines to make 100 widgets?(in minutes)")
                                respond = input (">")
                                if respond == "100":
                                    money = money + 15
                                    print_fun("(total money collected "+str(money)+"$)")
                                    print_fun("Q3:In a lake, there is a patch of lily pads. Every day, the patch doubles in size. If it takes 48 days for the patch to cover the entire lake, how long would it take for the patch to cover half of the lake?(in days)")
                                    respon = input(">")
                                    if respon == "24":
                                        money = money + 15
                                        print_fun("(total money collected "+str(money)+"$)")
                                        print_fun("you win 40$")
                                        print_fun("I think I shoud go to pizza shop")
                                        print_fun("I think I shoud go to pizza shop and try to get discount")
                                        print_fun("Pizza worker : hi,"+ name +" ,how can I help you")
                                        print_fun("1.Spin the lucky Wheel")
                                        print_fun("2.Buy pizza")
                                        resp = input(">")
                                        while True: #make random discount
                                            if resp == "1":
                                                price = 50
                                                spin = [20,10,5]
                                                luspin = int(random.choice(spin))
                                                price = price - luspin
                                                print ("You win " + str(luspin) + "$ discount")
                                                if price <= money:
                                                    print ("Now I can buy the pizza")
                                                    print ("you won!")
                                                    print_fun("(total money collected "+str(money)+"$)")
                                                    again ()
                                                else:
                                                    print ("you lost :(")
                                                    print_fun("(total money collected "+str(money)+"$)")
                                                    again ()
                                            if resp == "2":
                                                price = 50
                                                if price <= money:
                                                    print ("you won!")
                                                    print_fun("(total money collected "+str(money)+"$)")
                                                    again ()
                                                else:
                                                    print ("you lost :(")
                                                    print_fun("(total money collected "+str(money)+"$)")
                                                    again ()
                                                    exit()
                                    else:
                                        print ("you lost :(")
                                        print_fun("(total money collected "+str(money)+"$)")
                                        again ()
                                else:
                                    print ("you lost :(")
                                    print_fun("(total money collected "+str(money)+"$)")
                                    again ()
                            else:
                                print ("you lost :(")
                                print_fun("(total money collected "+str(money)+"$)")
                                again ()
                            break
                    break
        
        

main()
