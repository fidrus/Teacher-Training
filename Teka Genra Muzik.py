#!/usr/bin/env python3

import random as rnd

musiclist = {
    'Rock': 'Iron Maiden',
    'Pop': 'Michael Jackson',
    'Rock n Roll': 'Alan Merrill',
    'Heavy Metal': 'Led Zeppelin',
}

score=0;
tries=3
while tries > 0:
    try:
        random_music=rnd.choice(list(musiclist.items()))
        intials=[]
        for first_letter in random_music[0].split():
            intials.append(first_letter[0].capitalize())

        print(f'The intials for the music are {"".join(intials)} and the artist is {random_music[1].title()}')
        print('Can you guess the music?')
        music=input('>>')

        if music.lower().strip() == random_music[0].lower().strip():
            print(f'Well done! You have {tries-1}tries left. Your score is {score + 1}')
            tries-=1
            score+=1
        else:
            print(f'That is incorrect. You have {tries-1}tries left. Your score is {score}')
            tries-=1
            continue

        break
    except ValueError as error:
            print(erro)
            


