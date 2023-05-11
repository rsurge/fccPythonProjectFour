import random


def winner(player, opp):
    if (player == 'R' and opp == 'S') or (player == 'S' and opp == 'P') or (player == 'P' and opp == 'R'):
        return True


def play():
    player = input('"R" for rock\n"P" for paper\n"S" for scissors.\nWhich will you choose?: ').upper()
    opp = random.choice(['R', 'S', 'P'])

    if player == opp:
        return 'You tied. Try again.'
    if winner(player, opp):
        return 'OH snap! You won...'
    return 'You loser. Try again.'


print(play())
