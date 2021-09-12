import os

acidRemoved = False
cardIsHidden = True
coverOpened = False
packageArrived = False
packageMoved = False
packageOpened = False
playerInventory = []
score = 0
username = "nothing"

def titleScreen():
    print("\n\nThe Delivery\n")
    print("An interactive text adventure by Jeff Arwady\n")
    answer = input("Type 'begin' to play\n\n")
    if answer.lower().strip() == "begin":
        playGame()
    else: 
        exit()

def playGame():
    os.system('clear')
    homeOffice()

def homeOffice():
    printScore()
    answer = input("\nYou are sitting at a u-shaped desk in an oddly-shaped office with an open window.  There are two lazy-boy chairs in front of the desk.  On the desk in front of you is a spiffy-looking Macbook Pro.\n\n")
    decisionLogic(answer)

def decisionLogic(decisionString):
    if decisionString.lower() == "look around":
        lookAround()
    elif decisionString.lower() == "look":
        homeOffice()
    elif decisionString.lower() == "look at u-shaped desk":
        desk()
    elif decisionString.lower() == "look at desk":
        desk()
    elif decisionString.lower() == "look at oddly-shaped office":
        office()
    elif decisionString.lower() == "look at office":
        office()
    elif decisionString.lower() == "look at open window":
        window()
    elif decisionString.lower() == "look at window":
        window()
    elif decisionString.lower() == "look at chairs":
        firstChair()
    elif decisionString.lower() == "look at first lazy-boy chair":
        firstChair()
    elif decisionString.lower() == "look at first chair":
        firstChair()
    elif decisionString.lower() == "sit in first lazy-boy chair":
        negativeResponse()
    elif decisionString.lower() == "sit in first chair":
        negativeResponse()
    elif decisionString.lower() == "look at chair":
        whichChair()
    elif decisionString.lower() == "sit in chair":
        whichChair()
    elif decisionString.lower() == "look at second lazy-boy chair":
        secondChair()
    elif decisionString.lower() == "look at second chair":
        secondChair()
    elif decisionString.lower() == "sit in second lazy-boy chair":
        negativeResponse()
    elif decisionString.lower() == "sit in second chair":
        negativeResponse()
    elif decisionString.lower() == "look at macbook pro":
        computer()
    elif decisionString.lower() == "look at macbook":
        computer()
    elif decisionString.lower() == "look at computer":
        computer()
    elif decisionString.lower() == "look at laptop":
        computer()
    elif decisionString.lower() == "look at screen":
        computer()
    elif decisionString.lower() == "look at keyboard":
        keyboard()
    elif decisionString.lower() == "restart computer":
        restartComputer()
    elif decisionString.lower() == "use keyboard":
        useKeyboard()
    elif decisionString.lower() == "search first lazy-boy chair":
        searchFirstChair()
    elif decisionString.lower() == "search first chair":
        searchFirstChair()
    elif decisionString.lower() == "search second lazy-boy chair":
        searchSecondChair()
    elif decisionString.lower() == "search second chair":
        searchSecondChair()
    elif decisionString.lower() == "search chair":
        whichChair()
    elif decisionString.lower() == "get credit card":
        getCard()
    elif decisionString.lower() == "get card":
        getCard()
    elif decisionString.lower() == "take credit card":
        getCard()
    elif decisionString.lower() == "take card":
        getCard()
    elif decisionString.lower() == "look at credit card":
        lookCard()
    elif decisionString.lower() == "look at card":
        lookCard()
    elif decisionString.lower() == "inventory":
        inventory()
    elif decisionString.lower() == "look at package":
        lookPackage()
    elif decisionString.lower() == "get package":
        getPackage()
    elif decisionString.lower() == "take package":
        getPackage()
    elif decisionString.lower() == "open package":
        openPackage()
    elif decisionString.lower() == "open tome":
        openTome()
    elif decisionString.lower() == "remove acid vile":
        removeAcid()
    elif decisionString.lower() == "remove acid":
        removeAcid()
    elif decisionString.lower() == "turn first page":
        turnPage()
    elif decisionString.lower() == "turn page":
        turnPage()
    elif decisionString.lower() == "exit":
        exit()
    else:
        notSure()

def restartComputer():
    global score

    score += 1
    printScore()
    answer = input("\nYou remember fondly how Roy would say 'Have you tried turning it off and on again?'  Also your personal favorite 'I'm sorry are you from the past?'  You laugh to yourself but no you won't be restarting someone else's computer today.\n\n")
    decisionLogic(answer)

def lookPackage():
    printScore()
    answer = input("\nThe package is in pristeen shape.  You can hardly believe how sharp it looks considering the drone flew it over here so quickly!  You spend a few moments re-considering your stock options.\n\n")
    decisionLogic(answer)

def turnPage():
    global acidRemoved
    global score

    if acidRemoved:
        score += 25
        printScore()
        print("\nHaving removed the acid vile, you are now ready for the ultimate knowledge (although you must admit to being pretty skeptical, I mean this thing was on Amazon).  However, your doubts are quickly asuaged when the pages begin to glow uncontrollably.  You suddenly can't move.  It feels like pure electricity is coursing through your veins but somehow it doesn't hurt.  You begin shaking violently and notice that your hair is sparking.  What's happening??  The window shatters.  You begin to understand the very nature of the universe itself!  All of life's questions are now answerable by one equation and it's so simple.  You begin to laugh uncontrollably as you understand the secrets of existence as clearly as a kindergardner can add 2+2.  The lazy-boy chairs catch on fire.  The desk explodes.  You begin floating and yes it's effortless.  You amass ultimate and unlimited knowledge in mere seconds.  The office is ablaze with fire and energy and your thoughts becomes so pure, so quantum that you literally blink out of exist....\n\n")
        print("The End - You now exist only in subspace...")
    else:
        score += 29
        printScore()
        print("\nHaving not removed the acid vile you decide that you value your human existence - your family, your friends, and the beautiful life you have.  You decide that no human should have ultimate knowledge as that is reserved for God.  You turn the page boldly and watch as the acid vile breaks open and dissolves all the pages within seconds.  Feeling a renewed sense of your own humanity, and the somewhat out-of-place notion that you've just wasted a lot of time and someone else's money, you nevertheless go on with your life and live it to the fullest!\n\n")
        print("The End - You re-discovered your humanity and your purpose!")

def exit():
    os.system('clear')
    print("\ngoodbye...\n")

def removeAcid():
    global acidRemoved
    global coverOpened
    global score

    if coverOpened:
        score += 4
        acidRemoved = True
        printScore()
        answer = input("\nYou carefully remove the acid vile and dispoe of it safely.  Are you sure you know what you're doing??\n\n")
        decisionLogic(answer)
    else:
        printScore()
        answer = input("\nYou can't reach the acid vile with the tome closed.\n\n")
        decisionLogic(answer)

def openTome():
    global coverOpened
    global packageOpened
    global score

    if packageOpened:
        score += 5
        coverOpened = True
        printScore()
        answer = input("\nYou open the hefty volume and notice a hand-written note on the inner cover.  It reads: 'To whomever finds this tome, you now have the choice to end all choices.  You may either live your life as if you never found this accursed book - simply turn the first page and my solvent trap will destroy the knowledge contained therein; or you may simply remove the acid vile first and then ultimate knowledge will be yours.  But be warned!!  These pages are supernatural and it is said that one will never be able to go back to their life once they gaze upon this ultimate knowledge.  Signed, ' and it looks like someone has crossed out the signatore.  What the hell is this thing!?\n\n")
        decisionLogic(answer)
    else:
        notSure()

def openPackage():
    global packageArrived
    global packageMoved
    global packageOpened
    global score

    if packageArrived:
        if packageMoved:
            score += 5
            packageOpened = True
            printScore()
            answer = input("\nYou manage to open the rather excessive packaging and discover an ancient tome labeled 'The Meaning of Everything'; You are intimidated.  You also notice what looks like a vile of acid in a very haphazard and easy to disable trap mechanism.  You ascertain that you can open the tome without triggering the acid.\n\n")
            decisionLogic(answer)
        else:
            printScore()
            answer = input("\nYou try but it is very awkward opening the package on the floor.\n\n")
            decisionLogic(answer)
    else:
        notSure()

def getPackage():
    global packageArrived
    global packageMoved
    global score
    
    if packageArrived:
        score += 5
        packageMoved = True
        printScore()
        answer = input("\nThe package is too heavy to take with you, however you do manage to place it on the desk.  Whew!\n\n")
        decisionLogic(answer)
    else:
        notSure()

def inventory():
    global playerInventory

    inventoryString = ""
    printScore()
    for item in playerInventory:
        inventoryString += item
    print("\n" + inventoryString + "\n\n")
    answer = input()
    decisionLogic(answer)

def lookCard():
    global cardIsHidden
    global username
    global score

    if cardIsHidden:
        notSure()
    else: 
        score += 10
        username = "Steve Vogler"
        printScore()
        answer = input("\nThe credit card looks slightly worn but you can still make out the cardholder: 'Steve Vogler', and the security code on the back: '278'.\n\n")
        decisionLogic(answer)

def notSure():
    printScore()
    answer = input("\nNot sure what you mean.  Try again without unnecessary words such as 'the', etc.\n\n")
    decisionLogic(answer)

def getCard():
    global cardIsHidden
    global playerInventory
    global score

    if cardIsHidden:
        notSure()
    else:
        score += 5
        printScore()
        playerInventory.append("Credit Card")
        answer = input("\nTaken.\n\n")
        decisionLogic(answer)

def searchFirstChair():
    global cardIsHidden
    global score

    score += 15
    printScore()
    if cardIsHidden:
        answer = input("\nYou shimmey the chair a bit and a plastic credit card falls to the floor.  You maneuver the chair to a position that looks correct for the room.  Your O.C.D. is now at rest; at least for now...\n\n")
        cardIsHidden = False
        decisionLogic(answer)
    else:
        searchSecondChair()

def searchSecondChair():
    printScore()
    answer = input("\nThere is no need to search this chair.\n\n")
    decisionLogic(answer)

def useKeyboard():
    global username
    global packageArrived
    global score

    if username == "nothing":
        printScore()
        answer = input("\nYou go to type something but realize you don't have the information the computer is asking for.  Oddly, typing anything else or hitting the 'escape' key has no affect.\n\n")
        decisionLogic(answer)
    else:
        score += 25
        packageArrived = True
        printScore()
        answer = input("\nYou grab a seat in front of the Macbook Pro.  With the card in hand, you try entering the cardholder name and the security code on the back into the on-screen form.  After hitting 'return' on the keyboard, a simple message reads: 'Contratulations on your purchase Steve!  You will receive your package in a few seconds.'  As you feel a twinge of guilt, I mean jeez poor Steve - you hope the purchase was not too expensive - a small drone flies to the open window and drops off a package on the floor.  It whirls and whistles, as if to get your attention, and then flies away; right out the window through which it came.\n\n")
        decisionLogic(answer)

def keyboard():
    printScore()
    answer = input("\nYou rest your fingers on the black, comfortable keys.  Man this thing was made to type!\n\n")
    decisionLogic(answer)

def computer():
    printScore()
    answer = input("\nThe Macbook Pro is open with a visible keyboard.  You examine the screen intently.  It shows a credit card dialogue asking for a name and a security code.\n\n")
    decisionLogic(answer)
    
def firstChair():
    printScore()
    answer = input("\nThe first lazy-boy chair looks somewhat out of place here...\n\n")
    decisionLogic(answer)

def negativeResponse():
    printScore()
    answer = input("\nYou'd rather not.\n\n")
    decisionLogic(answer)

def whichChair():
    printScore()
    answer = input("\nWhich lazy-boy chair do you mean?  The first lazy-boy chair or the second lazy-boy chair?\n\n")
    decisionLogic(answer)

def secondChair():
    printScore()
    answer = input("\nThe second lazy-boy chair appears unremarkable.\n\n")
    decisionLogic(answer)

def window():
    printScore()
    answer = input("\nThe window seems stuck open.  Looking out you see an unremarkable landscape consistent with where you believe the office is located.\n\n")
    decisionLogic(answer)

def office():
    printScore()
    answer = input("\nThe office has a mis-shapen form being a rectangle with a more narrow base where the u-shaped desk is located.\n\n")
    decisionLogic(answer)

def desk():
    printScore()
    answer = input("\nThe desk is made of a faux-cherry-wood material and is generally unremarkable.\n\n")
    decisionLogic(answer)

def lookAround():
    global cardIsHidden

    if cardIsHidden:
        printScore()
        answer = input("\nThe office needs to be cleaned, eeck.  More than that, though, something isn't exactly right about the layout.  Your O.C.D. is agitating your brain.  However, a general inspection does not reveal anything out of the ordinary.\n\n")
        decisionLogic(answer)
    else:
        printScore()
        answer = input("\nThe office needs to be cleaned, eeck.")
        decisionLogic(answer)

def printScore():
    global score

    print("\nCurrent Score: " + str(score) + "/100\n")

if __name__ == "__main__":
    titleScreen()