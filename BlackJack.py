# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 23:47:14 2017

@author: snoel
"""

from random import randint
from random import shuffle

""" *******************************************************
* Global message strings
********************************************************"""
msgDoYouWantACard = """Would you like another card (Y/N)? """
msgErrCantRecover = """ An unknown error occured, unfortunately, we cant recover! """
msgExitGame =  """
            *********************************** END OF GAME ***************************************
            Thank you for participating in this learning experience
            ***************************************************************************************
            """
            
msgInvalidBet = """ The value entered is an invalid bet, please enter an integer! """
msgThkYou4Bet = """Thank you for providing your bet : %s \n"""
msgWelcome =  """
            ************************************* NEW GAME *****************************************
            This game is fully automatic, no user intervension is required. The purpose of the game
            is not to interact with the user but to get use to classes in Python
            I home you will enjoy
            ****************************************************************************************
            """
msgWhatIsYourBet = """What would you like to bet (Integer)? """
msgWhatIsThePlayerName = """What is the player's name? """
msgWhatIsTheDealerName = """What is the dealer's name? """


""" *******************************************************
* Global Variables
********************************************************"""
gPlayerStatus = ('OK','BJ','BUST', 'Err')
cOk = 0
cBJ = 1
cBUST = 2
cErr = 3

""" *******************************************************
* Class Deck
********************************************************"""
class Deck(object):

    kinds = ('Heart', 'Diamond', 'Spade', 'Club')
    cardIds = ('2','3','4','5','6','7','8','9','10', 'J', 'Q', 'K', 'A')
    cardsDeck = []          #list of tuples cards containing (kind, cardID)
    cardsAlreadyChoosen = [] #list of tuples cards containing (kind, cardID)
    
    def __init__(self):
        self.cardsAlreadyChoosen.clear()
        self.cardsDeck.clear()
        self.buildDeck()
                        
   
    def alreadChoosen(self, newCard):
        """ 
        the newCard is a tuple identifying a card (kind, Number)
        This function will return True if the card was already choosen otherwise False
        """
        for card in self.cardsAlreadyChoosen:
            if card == newCard:
                return True
            
        return False
            
    def buildDeck(self):
        """
        build the deck of 52 cards
        """
        for k in self.kinds:
            for card in self.cardIds:
                self.cardsDeck.append((k, card))
                
        shuffle(self.cardsDeck)
        
        
    def dealCard(self):
        """
        dealCard will return a card from cards remaing in the deck to the requestor. 
        The card will be a tuple (Kind, cardID)
        """
        
        card = self.cardsDeck.pop(randint(0, 12)) #pick a random card from the remaining cards in the deck
        self.cardsAlreadyChoosen.append(card)     #keep a trace of given card
        return card

    
""" *******************************************************
* Class Player
********************************************************"""
class Player(object):
    
    
    def __init__(self, splayerName, ibankroll = 100, bActive = True):
        self.active = bActive
        self.bankroll = ibankroll   #chips available for betting
        self.cards = []             #list of tuples cards containing (kind, cardID) 
        self.minCardsCount = 16     #as a player, I want to play until the card count is at least
        self.playerName = splayerName.capitalize()
        self.status = gPlayerStatus[0] #OK
        self.totalBet = 0

    def countCard(self):
        """
        This function will return the sommation of all cards contain in cardsInHand
        Params : cardsInHand is a list of tuple (Kind, CardId)
        Return: If you have an Ace, this card will be consider a 1 or 11 according the other cards in your hands
        """
        total = 0
        try:
            
            for k,n in self.cards:     #extract each card
                if n in ['2','3','4','5','6','7','8','9','10']:
                    total += int(n)
                elif n in ['J', 'Q', 'K']:
                    total += 10
                else:                   # must be a Ace 'A'
                    if total > 11 :
                        total += 1      # Ace is 1 otherwise we are over 21
                    else:
                        total += 11     # Let's count the Ace as 11 for now
            
        except:
            print("An error occur while counting the cards!")
        finally:
            return total
        
    def IWhishToBet(self, amount):
        """
        if the new bet amount does not surpass the chips available, accept the bet otherwise refuse it
        """
        try:
            amount = int(amount)    #ensure this is an integer
            if (self.totalBet + amount) <= self.bankroll:
                self.totalBet += amount
                self.bankroll -= amount   #deduct the bet from the chips available
                return self.totalBet
            else:
                return 0
        except:
            return 0


    def __str__(self):
        return "Name: %s, \nActive %s, \nGame Status: %s, \nNumber of Cards: %s, \nSum of Cards: %s, \nTotal Chips available: %s \nCurrent bet: %s \nCards in hand : %s \n"  \
                %(self.playerName, self.active, self.status, len(self.cards), self.countCard(), self.bankroll, self.totalBet, self.cards)
                                                                
   
""" *******************************************************
* Class Dealerd
********************************************************"""    
class Dealer(Player):
    def __init__(self, splayerName):
        Player.__init__(self, splayerName, 0, False)
        self.deckOfCards = Deck()       #the Dealer own the deck of cards
        
    def giveCard(self, player):
        player.cards.append(self.deckOfCards.dealCard()) 
            
    def doIHaveABlackjack(self, cardsInHand):
        """
        You are consider to have a blackjack if the sommation of your cards in hands total 21
        Param:
        Return: Return true if the of cardsInHand is equal to 21
        """
        if self.countCard() == 21:
            return True
        
        return False
    
    
    def payPlayer(self):
        """
        Paying the player
        """
        pass
    


""" *******************************************************
* GiveTheFirst2Cards
********************************************************"""
def GiveTheFirst2Cards(dealer, player):
    try:
        dealer.giveCard(player)
        dealer.giveCard(player)
        return True
    except:
        print('Unable to initiate the table for %s' %player.playerName)
        return False

""" *******************************************************
* inputYourBet
********************************************************"""
def inputYourBet():

    i = -1
    while True:
        try:
            i = int(input(msgWhatIsYourBet))
            break
        except ValueError:
            print(msgInvalidBet)
            continue
        finally:
            print(msgThkYou4Bet %i)
            break

    return i

""" *******************************************************
* inputYourName
********************************************************"""
def inputString(msg):
    return input(msg)


""" *******************************************************
* playerRequestCards
********************************************************"""
def playerRequestCards(dealer, player):
    """
    Allow the player to get the cards from the dealer
    the player will stop asking when his minCardsCount is reach or 21 or the player bust
    Params:
            dealer is a Dealer class. The dealer will provide the cards and check for the hand status
            player is the player to receive the cards
    Return:
            the system will assist you to get card one by one from the dealer
            if you reach your Minimum Cards Count, the system will automaticall assume that you are done
    """
    retVal = True
    try:
        while True:
            if not dealer.doIHaveABlackjack(player.cards):
                if player.countCard() < player.minCardsCount:
                    print(player)
                    if inputString(msgDoYouWantACard)[0].upper() != "N":
                        dealer.giveCard(player)
                        print(player)
                    else:
                        break
                elif player.countCard() < 21:
                    print('\n%s is in good position to win, sit and wait ' % player.playerName)
                    player.status = gPlayerStatus[cOk]
                    break
                elif player.countCard() == 21:
                    player.status = gPlayerStatus[cBJ] 
                    print('\n%s have a BlackJack! Congratulation' % player.playerName)
                    break
                else:
                    print('\n%s unfortunateluy you busted, I am sorry!' % player.playerName)
                    player.status = gPlayerStatus[cBUST] 
                    player.active = False
                    break
            else: 
                #there is a blackjack
                player.status = gPlayerStatus[cBJ] 
                print('\n%s have a BlackJack! Congratulation' % player.playerName)
                break
    except:
        print('An error occur while dealing the cards to the player')
        player.status = gPlayerStatus[3] #Err
        retVal = False
    finally:
        # Print the player and its cards to help follow up on the screen
        if dealer.doIHaveABlackjack(player.cards) == 21:
            player.status = gPlayerStatus(1)
            
        print(player)

    return retVal

""" *******************************************************
* PrintWelcomeMsg
********************************************************"""
def PrintWelcomeMsg():    
    print(msgWelcome)

""" *******************************************************
* PrintExitGameMsg
********************************************************"""    
def PrintExitGameMsg():
    print(msgExitGame)

    
""" *******************************************************
* Main
********************************************************"""

PrintWelcomeMsg()
dealer = Dealer(inputString(msgWhatIsTheDealerName))
player1 = Player(inputString(msgWhatIsThePlayerName), 1000, True)

print('***** %s *****' % player1.playerName.upper())

#******************* PLAYER get his cards ***************************
print('********************** PLAYER **********************')
if GiveTheFirst2Cards(dealer, player1) and GiveTheFirst2Cards(dealer, dealer):
    while True:
        print(player1)
        if player1.IWhishToBet(inputYourBet()) >= 0: #not sure if this is a real rule in BlackJack but it will do for now
            playerRequestCards(dealer, player1)
            if player1.countCard() < player1.minCardsCount: 
                if player1.status == gPlayerStatus[cOk]:
                    player1.IWhishToBet(inputYourBet())
                    break
                else:
                    break
            else:
                print('Thank you, the next player will play now!')
                break
        else:
            if inputString('Do you want to stay in the game (Y/N):')[0].upper() != 'N':
                continue
            else:
                print('You have withdraw from the table, thank you for playing')
                break
    
print(player1)
inputString('%s your status is %s. Press any key to allow the next user to play' %( player1.playerName, player1.status))

#******************* DEALER get his cards ***************************
print('********************** DEALER **********************')
print('\n***** %s *****' % dealer.playerName.upper())
dealer.minCardsCount = 17   #the dealer must play until 17
print(dealer)
playerRequestCards(dealer, dealer)
inputString('%s your status is %s. Press any key to allow the next user to play and start paying the player' %( dealer.playerName, dealer.status))


#******************* DEALER get his cards ***************************
if player1.active:
    if (dealer.countCard() > player1.countCard()):
        player1.bankroll += player1.totalBet*1.5        #you receive 1.5 time your bet as you are higher than the dealer
    elif player1.status == gPlayerStatus[cBJ]:
        player1.bankroll += player1.totalBet*4          #receive 4 times what you bet ... you have a BJ so it is a big pay day
    else:
        player1.bankroll += player1.totalBet
elif player1.status == dealer.status == gPlayerStatus[cBUST]:
    player1.bankroll += player1.totalBet                #both the player and dealer busted, return the money to the player. No one loose


print(player1)

PrintExitGameMsg()
