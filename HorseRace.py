#!usr/bin/python
#Horserace.py

''' Allows user to name turtles and watch them race across a track. The winner
    is determined and a player can play the game again. '''

__author__ = "Beth Fineberg"
__version__ = "1.0"

import turtle
import random
import time

def main():
    num_horses = 5
    
    win = turtle.Screen()

    win.setup(1000, 800)
    win.title("Horse Race")

    turtle.colormode(255)

    win.bgpic("ocean.gif")

    win.textinput("Welcome!", "Hello and welcome to Horse Race. The turtle " +
                  "racers\nare on an underwater race track and ill try to " +
                  "reach \nthe finish line the fastest. Press enter to continue.")

    ans = "yes"

    #creates all turtles used
    t = turtle.Turtle()
    a = turtle.Turtle()
    b = turtle.Turtle()
    c = turtle.Turtle()
    d = turtle.Turtle()
    e = turtle.Turtle()
    m = turtle.Turtle()
    winner = turtle.Turtle()
    balance = turtle.Turtle()

    #user's balance left for betting
    usr_balance = 100

    ################################
    ### runs game when user wants to
    ################################
    while ans == "yes":
        #hides turtles until they are used
        t.hideturtle()
        a.hideturtle()
        b.hideturtle()
        c.hideturtle()
        d.hideturtle()
        e.hideturtle()
        m.hideturtle()
        winner.hideturtle()
        balance.hideturtle()

        #sets up turtles for racing
        a.turtlesize(3)
        b.turtlesize(3)
        c.turtlesize(3)
        d.turtlesize(3)
        e.turtlesize(3)

        a.speed(8)
        b.speed(8)
        c.speed(8)
        d.speed(8)
        e.speed(8)

        turtles = [a, b, c, d, e]

        #user names turtles
        name1 = win.textinput("Choose a Name", "What do you want to name the " +
                              "first racer?")
        name2 = win.textinput("Choose a Name", "What do you want to name the " +
                              "second racer?")
        name3 = win.textinput("Choose a Name", "What do you want to name the " +
                              "third racer?")
        name4 = win.textinput("Choose a Name", "What do you want to name the " +
                              "fourth racer?")
        name5 = win.textinput("Choose a Name", "What do you want to name the " +
                              "fifth racer?")

        names = [name1, name2, name3, name4, name5]

        #shows the user's balance for betting
        balance.penup()
        balance.goto(-270, 270)
        balance.color("white")
        balance.write("Your balance: $" + str(usr_balance), align="center",
                      font=("Comic Sans MS", 30, "normal"))

        #original coordinates for beginning of drawings done in for loops
        line_height = -300
        turtle_height = -250
        start_height = -290
        end_height = -290
        mid_line = -265

        #pen settings to draw tracks
        t.speed(10)
        t.pensize(5)

        #################################
        ### draws turtles and race tracks
        #################################

        #draws tracks
        for i in range(num_horses + 1):
            t.showturtle()
            t.penup()
            t.goto(-450, line_height)
            t.pendown()
            t.fd(900)
            line_height += 100

        countdown = 3

        #draws start lines
        for i in range(num_horses):
            t.color("white")
            t.pensize(10)
            t.penup()
            t.goto(-450, start_height)
            t.pendown()
            t.goto(-450, start_height + 80)
            start_height += 100

        #draws end lines
        for i in range(num_horses):
            t.penup()
            t.goto(450, end_height)
            t.pendown()
            t.goto(450, end_height + 80)
            end_height += 100

        for j in range(num_horses):
            #draws turtles of random colors and place them at start line
            i = turtles[j]
            i.shape("turtle")
            i.showturtle()
            color = [random.randrange(0, 257, 10),
                     random.randrange(0, 257, 10), random.randrange(0, 257, 10)]
            i.color((color[0], color[1], color[2]))
            i.penup()
            i.goto(-450, turtle_height)
            i.pendown()
            turtle_height += 100

            #write the names of each turtle in middle of tracks
            n = names[j]
            m.speed(0)
            m.color(color[0], color[1], color[2])
            m.hideturtle()
            m.penup()
            m.goto(0, mid_line)
            m.write("Racer: " + n, align="center", font=("Comic Sans MS", 30,
                                                         "normal"))
            mid_line += 100

        ###########################
        ### allows user to make bet
        ###########################
        turtle_bet = win.textinput("Make a Bet", "Which turtle would you like " +
                                   "to bet on winning?")
        bet_amount = int(win.textinput("Make a Bet", "How much money would you " +
                                       "like to bet on this?"))

        while bet_amount > usr_balance:
            bet_amount = int(win.textinput("Make a Bet", "Your balance is too "
                                           + "low to bet this amount. Please " +
                                           "choose a lower amount to bet."))

        ###############
        ### race begins
        ###############
        t.hideturtle()
        t.penup()
        t.speed(8)
        t.goto(0, 220)
        t.color("white")
        t.write("The race will begin in:" , align="center",
                font=("Comic Sans MS", 30, "normal"))
        time.sleep(1)
        t.undo()

        #countdown for race to start
        for i in range(3):
            t.write(countdown, align="center", font=("Comic Sans MS", 30, "normal"))
            time.sleep(1)
            countdown -= 1
            t.undo()
        
        t.write("GO!!!!", align="center", font=("Comic Sans MS", 30, "normal"))

        a.speed(0)
        b.speed(0)
        c.speed(0)
        d.speed(0)
        e.speed(0)

        not_end = True

        winner_name = ""

        #turtles move forward at random range until one reaches end
        while(not_end == True):
            for i in range(num_horses):
                l = turtles[i]
                l.penup()
                l.fd(random.randrange(5, 50))

                #determines winner and saves information about them
                if (l.xcor() > 450):
                    not_end = False
                    winner = l
                    winner_name = names[i]

        t.undo()

        t.write("The winner is: " + winner_name + "!!!", align="center", font=("Comic Sans MS", 30, "normal"))

        time.sleep(2)
        t.undo()

        ###################################################################
        ### shows user message and updates balance depending upon their bet
        ###################################################################
        if turtle_bet == winner_name:
            t.write("Congratulations! You have won the bet and won $" +
                    str(bet_amount), align="center", font=("Comic Sans MS", 30, "normal"))
            usr_balance += bet_amount
        else:
            t.write("Sorry! You have lost the bet and lost $" +
                    str(bet_amount), align="center", font=("Comic Sans MS", 30, "normal"))
            usr_balance -= bet_amount

        time.sleep(1)

        #exits game if balance is zero or below
        if usr_balance == 0 or usr_balance < 0:
            win.textinput("Game Over", "You have lost all your money. Goodbye!")
            win.bye()

        ans = win.textinput("Done?", "Would you like to race again? (yes or no)")

        #resets all turtles in order to redo game
        t.reset()
        a.reset()
        b.reset()
        c.reset()
        d.reset()
        e.reset()
        m.reset()
        winner.reset()
        balance.reset()

        #shuts game if user doesn't want to replay
        if ans == "no":
            win.bye()
        
main()
