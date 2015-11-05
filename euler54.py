__author__ = 'RTryson'


class PokerHand:
    # pass in 'cards' variable as a list
    def __init__(self, cards):
        self.cards = cards

    def cardValues(self):
        l = []
        for card in self.cards:
            l.append(card[0])
        return l

    def getHighValue(self):
        return self.cards[0][0]

    def checkStraight(self):
        order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
        check = self.cardValues()
        check = ''.join(check)
        order = ''.join(order)
        return check in order

    def checkFlush(self):
        s = self.cards[0][1]
        for card in self.cards:
            curr = card[1]
            if curr != s:
                return False
        return True

    def checkBook(self):
        vals = self.cardValues()
        if vals[0] == vals[1] and vals[1] == vals[2] and vals[2] == vals[3]:
            return True
        if vals[1] == vals[2] and vals[2] == vals[3] and vals[3] == vals[4]:
            return True
        return False

    def getBookValues(self):
        vals = self.cardValues()
        if vals[0] == vals[1]:
            foursome = vals[0]
            other = vals[4]
        else:
            foursome = vals[4]
            other = vals[0]
        return [foursome, other]

    def checkHouse(self):
        vals = self.cardValues()
        if vals[0] == vals[1] and vals[2] == vals[3] and vals[3] == vals[4] and vals[1] != vals[2]:
            return True
        if vals[0] == vals[1] and vals[1] == vals[2] and vals[3] == vals[4] and vals[2] != vals[3]:
            return True
        return False

    def getHouseValues(self):
        vals = self.cardValues()
        if vals[1] == vals[2]:
            over = vals[0]
            under = vals[4]
        else:
            over = vals[4]
            under = vals[0]
        return [over, under]

    def checkThree(self):
        vals = self.cardValues()
        if vals[0] == vals[1] == vals[2]:
            return True
        if vals[1] == vals[2] == vals[3]:
            return True
        if vals[2] == vals[3] == vals[4]:
            return True
        return False

    def getThreeValues(self):
        vals = self.cardValues()
        if vals[0] == vals[1] == vals[2]:
            threesome = vals[0]
            other = vals[3]
        elif vals[1] == vals[2] == vals[3]:
            threesome = vals[1]
            other = vals[0]
        else:
            threesome = vals[2]
            other = vals[0]
        return [threesome, other]

    def checkTwoPair(self):
        vals = self.cardValues()
        if vals[0] == vals[1] and vals[2] == vals[3]:
            return True
        if vals[0] == vals[1] and vals[3] == vals[4]:
            return True
        if vals[1] == vals[2] and vals[3] == vals[4]:
            return True
        return False

    def getTwoPairVals(self):
        vals = self.cardValues()
        # cases: other is highest, other is in middle, other is lowest
        if vals[0] == vals[1]:
            highpair = vals[0]
            if vals[2] == vals[3]:
                lowpair = vals[2]
                other = vals[4]
            else:
                other = vals[2]
                lowpair = vals[4]
        else:
            other = vals[0]
            highpair = vals[1]
            lowpair = vals[3]
        return [highpair, lowpair, other]

    def checkPair(self):
        vals = self.cardValues()
        if vals[0] == vals[1] or vals[1] == vals[2] or vals[2] == vals[3] or vals[3] == vals[4]:
            return True
        return False

    def getPairVals(self):
        vals = self.cardValues()
        if vals[0] == vals[1]:
            pair = vals[0]
            other = vals[2]
        else:
            other = vals[0]
            if vals[1] == vals[2]:
                pair = vals[1]
            elif vals[2] == vals[3]:
                pair = vals[2]
            else:
                pair = vals[3]
        return [pair, other]

    def evaluate(self):
        valuation = ""
        # parse a poker hand and determine what its valuation should be
        # the options are:
        #   high card
        #   one pair
        #   two pair
        #   three of a kind
        #   straight
        #   flush
        #   full house
        #   four of a kind
        #   straight flush
        #   royal flush (technically this is just an Ace-high straight flush)
        high = self.getHighValue()
        if self.checkStraight():
            if self.checkFlush():
                valuation = "8" + high
            else:
                valuation = "4" + high
        elif self.checkFlush():
            valuation = "5" + high
        elif self.checkBook():
            [foursome, other] = self.getBookValues()
            valuation = "7" + foursome + other
        elif self.checkHouse():
            [over, under] = self.getHouseValues()
            valuation = "6" + over + under
        elif self.checkThree():
            [threesome, other] = self.getThreeValues()
            valuation = "3" + threesome + other
        elif self.checkTwoPair():
            [highpair, lowpair, other] = self.getTwoPairVals()
            valuation = "2" + highpair + lowpair + other
        elif self.checkPair():
            [pair, other] = self.getPairVals()
            valuation = "1" + pair + other
        else:
            valuation = "0" + high
        return valuation


def compare(p1, p2):
    order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]

    win = 0

    if p1[0] > p2[0]:
        win = 1
    elif p2[0] > p1[0]:
        win = 2
    else:
        v = int(p1[0])
        print("v = " + repr(v))
        if v == 0 or v == 4 or v == 5 or v == 8: # high card, flush, straight, straight flush
            if order.index(p1[1]) < order.index(p2[1]):
                win = 1
            else:
                win = 2

        elif v == 1 or v == 3 or v == 6 or v == 7: # pair - value,pair,other, also threesome, foursome, full house
            if order.index(p1[1]) < order.index(p2[1]):
                win = 1
            elif order.index(p1[1]) > order.index(p2[1]):
                win = 2
            else:
                # compare 'other'
                if order.index(p1[2]) < order.index(p2[2]):
                    win = 1
                else:
                    win = 2

        elif v == 2: # twopair - value,highpair,lowpair,other
            if order.index(p1[1]) < order.index(p2[1]):
                win = 1
            elif order.index(p1[1]) > order.index(p2[1]):
                win = 2
            else:
                if order.index(p1[2]) < order.index(p2[2]):
                    win = 1
                elif order.index(p1[2]) > order.index(p2[2]):
                    win = 2
                else:
                    if order.index(p1[3]) < order.index(p2[3]):
                        win = 1
                    elif order.index(p1[3]) > order.index(p2[3]):
                        win = 2


        # elif v == 2: # twopair - value,highpair,lowpair,other
        #     return twopair(p1, p2)
        # elif v == 3: # threesome - value,threesome,other
        #     return threesome(p1, p2)
        # elif v == 4:
        #     return straight(p1, p2)
        # elif v == 5:
        #     return flush(p1, p2)
        # elif v == 6:
        #     return fullhouse(p1, p2)
        # elif v == 7:
        #     return foursome(p1, p2)
        # elif v == 8:
        #     return straightflush(p1, p2)

    print("Player 1 value is " + p1 + ", Player 2 value is " + p2 + ", Player " + repr(win) + " wins")
    return win

# puts the cards in descending order
def sort_cards(cards):
    copy = list(cards)
    sorted = []
    order = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    while len(copy) > 0:
        m = 999
        i = 0
        for card in copy:
            # find the "max"
            c = order.index(card[0])
            if c < m:
                m = c
                i = copy.index(card)
        sorted.append(copy.pop(i))
    return sorted

count = 0
p1wins = 0
p2wins = 0
with open('poker.txt', 'r') as f:
    for line in f:
        count += 1
        both_hands = line.split()
        p1_cards = sort_cards(list(both_hands[0:5]))
        p2_cards = sort_cards(list(both_hands[5:10]))
        player_one = PokerHand(p1_cards)
        player_two = PokerHand(p2_cards)
        p1_value = player_one.evaluate()
        p2_value = player_two.evaluate()
        winner = compare(p1_value, p2_value)
        print(p1_cards, p2_cards)
        print(winner)
        if winner == 1:
            p1wins += 1
        else:
            p2wins += 1

print("Total = " + repr(count))
print("P1 = " + repr(p1wins))
print("P2 = " + repr(p2wins))
allwins = p1wins + p2wins
print("Wins = " + repr(allwins))