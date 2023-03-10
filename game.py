# @Author Jake Busse
#  This file 'game.py' contains most of the basic BINGO game functions outside the card, such as calling numbers,
#  displaying calls, UI plays, and declaring a winner.

from card import *


def call_number(calls):
    """
    Takes a list calls and appends random number from 1 to 75 that is not already in the list
    """
    call = random.randint(0, 76)
    while call in calls:
        call = random.randint(0, 76)
    calls.append(call)
    return calls


def display_call(call):
    """
    Displays called number with appropriate BINGO letter in front of it for UI games
    :param call:
    """
    if call <= 15:
        print('B', end='')
    elif call <= 30:
        print('I', end=''),
    elif call <= 45:
        print('N', end=''),
    elif call <= 60:
        print('G', end=''),
    elif call <= 75:
        print('O', end='')
    print(call)


def fast_play(cards, pattern):
    """
    Plays multiple cards at once and keeps calling until one or multiple cards wins. Returns winning card indexes.
    :param cards:
    :param pattern:
    :return:
    """
    win = False
    winners = []
    while not win:
        call = call_number()
        for card in cards:
            daub_number(card, call)
            if check_card(card, pattern):
                win = True
                winners.append(cards.index(card))
    return winners


def slow_play(cards, pattern):
    """
    UI version of fast play where user must consent to each number being called so they can see the progress as their
    cards get daubed. More akin to real-life BINGO. Returns dictionary containing number of balls called upon win
    and the winning card.
    :param cards:
    :param pattern:
    :return:
    """
    nums_called = 0
    win = False
    while not win:
        input('Call? > ')
        call = call_number()
        nums_called += 1
        display_call(call)
        for card in cards:
            daub_number(card, call)
            display_card(card)
            if check_card(card, pattern):
                win = True
                game_info = {'nums_called': nums_called, 'winning_card': card}
    return game_info


def declare_winners(winners, prize):
    """
    Takes list winners and int prize to list winners and their respective prize amount rounded to the nearest dollar
    :param winners:
    :param prize:
    :return:
    """
    if len(winners) == 1:
        return "Card " + str(winners[0]) + " wins " + str(prize)
    else:
        return "Cards " +str(winners) + " win " + str(prize//len(winners))