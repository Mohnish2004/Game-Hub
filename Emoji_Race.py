import random
import time

print('\n\t\t\t\t\t\tThe Emoji Race')

print('''
Instructions:
-> This is a Player vs AI dice based game
-> The player selects how many die they would like to roll (1 or 2)
-> As the game progresses the distance left for victory is displayed on the right
-> To win you must get a perfect roll otherwise your turn will not count and you will not move
-> The first person to reach the finish line wins
''')

input('Once the player is ready to begin please press enter....')
time.sleep(2)

print('\nRace Settings:\n')
time.sleep(1.5)
char_select=input('Select Custom Emojis (Y/N): ')
if char_select.upper()=='Y':
    faces={1:'(@_@)',2:'(-_-)',3:'(*_*)',4:'(>_<)',5:'(^-^)',6:'(x_x)',7:'(;-;)',8:'(o_o)',9:'(#_#)',10:'(~_~)',117:'Arnav'}

    print('\nPlayer Emoji Selection:')
    time.sleep(1)
    print('''
1) (@_@)
2) (-_-)
3) (*_*)
4) (>_<)
5) (^-^)
6) (x_x)
7) (;-;)
8) (o_o)
9) (#_#)
10)(~_~)
''')
    p_select=int(input('Please enter the number of the emoji that you would like to select '))
    player_char=faces[p_select]

    print('\nAI Emoji Selection:\n')
    time.sleep(1)
    print('''
1) (@_@)
2) (-_-)
3) (*_*)
4) (>_<)
5) (^-^)
6) (x_x)
7) (;-;)
8) (o_o)
9) (#_#)
10)(~_~)
''')
    AI_select=int(input('Please enter the number of the emoji that you would like to select for the AI '))
    AI_char=faces[AI_select]

if char_select.upper()=='N':
    player_char='(@_@)'
    AI_char='(-_-)'

print('\nPlayer Emoji:',player_char,'|','AI Emoji:',AI_char,'\n')

time.sleep(2)

print('''
Powerups:-

Single roll:
- If the Player/AI roll a 6, they are granted a second roll

Double roll:
- If the Player/AI roll the same number on both die they are granted a third die
''')
powers=input('Use Powerups [Powerups will be active for both the player and the AI](Y/N): ')
powers=powers.upper()

while True:
    print()
    game_len=int(input('Enter race length (50-100): '))
    if game_len>100 or game_len<50:
        print('\nPlease enter a distance between 50 and 100')
        time.sleep(1.5)
        continue
    else:
        break

time.sleep(5)

design_gap=game_len+11
end_display_gap=game_len+2
winner='None'
player_distance=0
AI_distance=0
player_gap=game_len
AI_gap=game_len

print('\t\t\t\t\t\tStarting Postions:\n\n')
print('P1:',' '*player_distance,player_char,' '*player_gap,'|',player_gap)
print(' '*design_gap,'|')
print('AI:',' '*AI_distance,AI_char,' '*AI_gap,'|',AI_gap)
print()

while winner=='None':
    time.sleep(2)
    DiceNumber=int(input('How many dice would you like to roll (1 or 2) '))
    print()
    
    tempA,tempB=player_distance,player_gap
    temp1,temp2=AI_distance,AI_gap
    
    if DiceNumber==1:
        d1=random.randint(1,6)
        d1AI=random.randint(1,6)

        player_distance+=d1
        AI_distance+=d1AI
        player_gap-=d1
        AI_gap-=d1AI

        print('You rolled a',d1)

        if powers=='Y' and d1==6 and player_gap>0:
            time.sleep(1.5)
            dpower=random.randint(1,6)
            print('\nPower Up Activated! you rolled a',dpower,'for your second roll')
            player_distance+=dpower
            player_gap-=dpower
            time.sleep(1.5)

        if player_gap<0:
            time.sleep(1)
            print('\nSorry since it was not a perfect roll you do not change position')
            player_distance,player_gap=tempA,tempB
            time.sleep(1.5)

        print()
        
        print('The AI rolled a',d1AI)
        
        if powers=='Y' and d1AI==6 and AI_gap>0:
            time.sleep(1.5)
            dpower=random.randint(1,6)
            print('\nPower Up Activated! The AI rolled a',dpower,'for its second roll')
            AI_distance+=dpower
            AI_gap-=dpower
            time.sleep(1.5)

        if AI_gap<0:
            time.sleep(1)
            print('\nSince the AI did not get a perfect roll its position has not changed')
            AI_distance,AI_gap=temp1,temp2

        print()
        
    if DiceNumber==2:
        d1,d2=random.randint(1,6),random.randint(1,6)
        d1AI,d2AI=random.randint(1,6),random.randint(1,6)

        player_distance+=(d1+d2)
        AI_distance+=(d1AI+d2AI)
        player_gap-=(d1+d2)
        AI_gap-=(d1AI+d2AI)

        print('You rolled a',d1,'and a',d2)

        if powers=='Y' and d1==d2 and player_gap>0:
            time.sleep(1.5)
            dpower=random.randint(1,6)
            print('\nPower Up Activated! you rolled a',dpower,'for your extra roll')
            player_distance+=dpower
            player_gap-=dpower
            time.sleep(1.5)
        
        if player_gap<0:
            time.sleep(1)
            print('\nSorry since it was not a perfect roll you do not change position')
            player_distance,player_gap=tempA,tempB
            time.sleep(1.5)

        print()
        
        print('The AI rolled a',d1AI,'and a',d2AI)

        if powers=='Y' and d1AI==d2AI and AI_gap>0:
            time.sleep(1.5)
            dpower=random.randint(1,6)
            print('\nPower Up Activated! The AI rolled a',dpower,'for its extra roll')
            AI_distance+=dpower
            AI_gap-=dpower
            time.sleep(1.5)
            
        if AI_gap<0:
            time.sleep(1)
            print('\nSince the AI did not get a perfect roll its position has not changed')
            AI_distance,AI_gap=temp1,temp2
        print()

    if DiceNumber>2 or DiceNumber<1:
        print('Please role either 1 or 2 dice only')
        print()
        time.sleep(1.5)
        continue

    if AI_distance>player_distance and player_gap>0 and AI_gap>0:
        indicator='The AI is in the lead :('
    if player_distance>AI_distance and player_gap>0 and AI_gap>0:
        indicator='You are in the lead :)'
    if player_distance==AI_distance and player_gap>0 and AI_gap>0:
        indicator='The player and AI are tied for the lead :|'
    
    time.sleep(1.5)
    if player_gap>0 and AI_gap>0:
        print('\t\t\t\t\t\tCurrent positions:\n\n')
        print('P1:',' '*player_distance,player_char,' '*player_gap,'|',player_gap)
        print(' '*design_gap,'|')
        print('AI:',' '*AI_distance,AI_char,' '*AI_gap,'|',AI_gap)
        print()
        print(indicator,'\n')


    if player_gap==0 and AI_gap>0:
        winner='P'
        print('\t\t\t\t\t\tFinal positions:\n\n')
        print('P1:',' '*end_display_gap,player_char+'|')
        print(' '*design_gap,'|')
        print('AI:',' '*AI_distance,AI_char,' '*AI_gap,'|')
        print()

    if AI_gap==0 and player_gap>0:
        winner='AI'
        print('\t\t\t\t\t\tFinal positions:\n\n')
        print('P1:',' '*player_distance,player_char,' '*player_gap,'|')
        print(' '*design_gap,'|')
        print('AI:',' '*end_display_gap,AI_char+'|')
        print()
    if AI_gap==0 and player_gap==0:
        winner='tie'
        print('\t\t\t\t\t\tFinal positions:\n\n')
        print('P1:',' '*end_display_gap,player_char+'|')
        print(' '*design_gap,'|')
        print('AI:',' '*end_display_gap,AI_char+'|')
        print()

time.sleep(1.5)

if winner=='P':
    print('''
                                     (: CONGRATULATIONS YOU HAVE WON THE EMOJI RACE :)
________________________________________________________________________________________________________________________

                                                  THANK YOU FOR PLAYING
''')
if winner=='AI':
    print('''
                                           ): THE AI WON. BETTER LUCK NEXT TIME :(
________________________________________________________________________________________________________________________

                                                   THANK YOU FOR PLAYING
''')        
if winner=='tie':
    print('''
                                         |: UH OH ITS A TIE. HOW DID THAT HAPPEN :|
________________________________________________________________________________________________________________________

                                                   THANK YOU FOR PLAYING
''')
