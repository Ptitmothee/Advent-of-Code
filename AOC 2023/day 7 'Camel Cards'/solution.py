"""
Your all-expenses-paid trip turns out to be a one-way, five-minute ride in an airship. (At least it's a cool airship!) It drops you off at the edge of a vast 

desert and descends back to Island Island.

"Did you bring the parts?"

You turn around to see an Elf completely covered in white clothing, wearing goggles, and riding a large camel.

"Did you bring the parts?" she asks again, louder this time. You aren't sure what parts she's looking for; you're here to figure out why the sand stopped.

"The parts! For the sand, yes! Come with me; I will show you." She beckons you onto the camel.

After riding a bit across the sands of Desert Island, you can see what looks like very large rocks covering half of the horizon. The Elf explains that the 

rocks are all along the part of Desert Island that is directly above Island Island, making it hard to even get there. Normally, they use big machines to move 

the rocks and filter the sand, but the machines have broken down because Desert Island recently stopped receiving the parts they need to fix the machines.

You've already assumed it'll be your job to figure out why the parts stopped when she asks if you can help. You agree automatically.

Because the journey will take a few days, she offers to teach you the game of Camel Cards. Camel Cards is sort of similar to poker except it's designed to be 

easier to play while riding a camel.

In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand. A hand consists of five cards labeled one of A, K, 

Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of each card follows this order, where A is the highest and 2 is the lowest.

Every hand is exactly one type. From strongest to weakest, they are:

    Five of a kind, where all five cards have the same label: AAAAA
    Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    High card, where all cards' labels are distinct: 23456

Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.

If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand. If these cards are different, the hand 

with the stronger first card is considered stronger. If the first card in each hand have the same label, however, then move on to considering the second card 

in each hand. If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger because its first card is stronger. Similarly, 77888 and 77788 are both a full house, 

but 77888 is stronger because its third card is stronger (and both hands have the same first and second card).

To play Camel Cards, you are given a list of hands and their corresponding bid (your puzzle input). For example:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483

This example shows five hands; each hand is followed by its bid amount. Each hand wins an amount equal to its bid multiplied by its rank, where the weakest 

hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. Because there are five hands in this example, the strongest hand 

will have rank 5 and its bid will be multiplied by 5.

So, the first step is to put the hands in order of strength:

    32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.

    KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and 
    KK677 gets rank 3.

    T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.

Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). So the total winnings in this example are 6440.

Find the rank of every hand in your set. What are the total winnings?
"""

import sys
sys.path.insert(0, 'C:/Users/timot/Documents/Programmation/Python/Advent of code 2023')
import Functions as Fn

Players_lines = Fn.getlines("C:/Users/timot/Documents/Programmation/Python/Advent of code 2023/day 7 'Camel Cards'/input.txt")
n = len(Players_lines)
Players = []
for i in range(n):
    player = Players_lines[i].split(" ")
    Players.append([player[0], int(player[1])])

def getHandType(hand):
    """
    Type = 6 : Five of a kind, where all five cards have the same label: AAAAA
    Type = 5 : Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    Type = 4 : Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    Type = 3 : Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    Type = 2 : Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    Type = 1 : One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    Type = 0 : High card, where all cards' labels are distinct: 23456
    """
    Dict = {}
    for c in hand:
        x = Dict.get(c)
        if x == None:
            Dict[c] = 1
        else:
            Dict[c] = x+1
    List = list(Dict.values())
    List.sort(reverse=True)
    Type = 0
    match List:
        case [5]:
            Type = 6
        case [4, 1]:
            Type = 5
        case [3, 2]:
            Type = 4
        case [3, 1, 1]:
            Type = 3
        case [2, 2, 1]:
            Type = 2
        case [2, 1, 1, 1]:
            Type = 1
    return Type

def comparePlayers(player1, player2):
    """
    Tests wether the hand of player2 is inferior to that of player1 according to the sorting system chosen for Camel Cards

    If player2[0] is strictly inferior to player1[0], return True, else return False
    """
    CardVal = {"T" : 8 , "J" : 9 , "Q" : 10 , "K" : 11 , "A" : 12}
    for i in range(2, 10):
        CardVal[str(i)] = i-2

    h1, b1, t1 = player1
    h2, b2, t2 = player2
    Result = True

    if t1 > t2:
        Result = False

    elif t1 == t2:
        i = 0
        c1 = h1[0]
        c2 = h2[0]
        while c1 == c2 and i<len(h1):
            i += 1
            c1 = h1[i]
            c2 = h2[i]
        if CardVal[c1] > CardVal[c2]:
            Result = False
    return Result

def quickSort_Bets(players, compare):
    n = len(players)
    PlayersType = [players[i] + [getHandType(players[i][0])] for i in range(n)]

    def partition(arr, low, high):
        pivot = high
        i = low
        for j in range(low, high):
            if compare(arr[j], arr[pivot]):
                i += 1
                arr[i-1], arr[j] = arr[j], arr[i-1]
        arr[i], arr[pivot] = arr[pivot], arr[i]
        return i
    
    def aux(arr, low, high):
        if low < high:
            pivot = partition(arr, low, high)
            aux(arr, low, pivot-1)
            aux(arr, pivot+1, high)

    aux(PlayersType, 0, n-1)
    return [PlayersType[i][1] for i in range(n)]

SortedBets = quickSort_Bets(Players, comparePlayers)

def getScores(sbets):
    n = len(sbets)
    Result = [0]*n
    for i in range(n):
        Result[i] = (i+1)*sbets[i]
    return Result

SOLUTION_p1 = sum(getScores(SortedBets))
print(SOLUTION_p1)


"""
To make things a little more interesting, the Elf introduces one additional rule. Now, J cards are jokers - wildcards that can act like whatever card would make 

the hand the strongest type possible.

To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind. However, for the 

purpose of breaking ties between two hands of the same type, J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J 

is weaker than Q.

Now, the above example goes very differently:

32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483

    32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
    KK677 is now the only two pair, making it the second-weakest hand.
    T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.

With the new joker rule, the total winnings in this example are 5905.

Using the new joker rule, find the rank of every hand in your set. What are the new total winnings?
"""

def getHandType2(hand):
    """
    Type = 6 : Five of a kind, where all five cards have the same label: AAAAA
    Type = 5 : Four of a kind, where four cards have the same label and one card has a different label: AA8AA
    Type = 4 : Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
    Type = 3 : Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
    Type = 2 : Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
    Type = 1 : One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
    Type = 0 : High card, where all cards' labels are distinct: 23456
    """
    Dict = {'T' : 0, 'J' : 0, 'Q' : 0, 'K' : 0, 'A' : 0}
    for i in range(2, 10):
        Dict[str(i)] = 0
    for c in hand:
        Dict[c] += 1
        x = Dict.get(c)

    List = list(Dict.values())
    List.sort(reverse=True)
    Type = 6
    match Dict['J']:
        case 3:
            if List[1] == 1:
                Type = 5 # Four of a kind JJJ*$
        case 2:
            if List[0] == 2 and List[1] == 2:
                Type = 5 # Four of a kind JJ**$
            else:
                Type = 3 # Three of a kind JJ*$@
        case 1:
            match List[0]:
                case 3:
                    Type = 5 # Four of a kind J***$
                case 2:
                    if List[1] == 2:
                        Type = 4
                    else:
                        Type = 3
                case 1:
                    Type = 1
        case 0:
            Type = getHandType(hand)
    return Type

def comparePlayers2(player1, player2):
    """
    Tests wether the hand of player2 is inferior to that of player1 according to the sorting system chosen for Camel Cards

    If player2[0] is strictly inferior to player1[0], return True, else return False
    """
    CardVal = {"T" : 9 , "J" : 0 , "Q" : 10 , "K" : 11 , "A" : 12}
    for i in range(2, 10):
        CardVal[str(i)] = i-1

    h1, b1, t1 = player1
    h2, b2, t2 = player2
    Result = True

    if t1 > t2:
        Result = False

    elif t1 == t2:
        i = 0
        c1 = h1[0]
        c2 = h2[0]
        while c1 == c2 and i<len(h1):
            i += 1
            c1 = h1[i]
            c2 = h2[i]
        if CardVal[c1] > CardVal[c2]:
            Result = False
    return Result

def quickSort_Bets2(players, compare):
    n = len(players)
    PlayersType = [players[i] + [getHandType2(players[i][0])] for i in range(n)]

    def partition(arr, low, high):
        pivot = high
        i = low
        for j in range(low, high):
            if compare(arr[j], arr[pivot]):
                i += 1
                arr[i-1], arr[j] = arr[j], arr[i-1]
        arr[i], arr[pivot] = arr[pivot], arr[i]
        return i
    
    def aux(arr, low, high):
        if low < high:
            pivot = partition(arr, low, high)
            aux(arr, low, pivot-1)
            aux(arr, pivot+1, high)

    aux(PlayersType, 0, n-1)
    return [PlayersType[i][1] for i in range(n)]

SortedBets2 = quickSort_Bets2(Players, comparePlayers2)

SOLUTION_p2 = sum(getScores(SortedBets2))
print(SOLUTION_p2)