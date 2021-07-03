import time
import random
print('''                                                              
                      ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
                  ░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░                    
              ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                
              ▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░▓▓                
            ▓▓▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓              
            ▓▓▒▒▒▒▒▒░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓              
            ▓▓▒▒▒▒▒▒▓▓▒▒░░░░░░░░░░░░░░░░░░░░░░░░▓▓            
            ▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            
            ▓▓▒▒▓▓░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓              
            ▓▓▒▒▓▓░░░░▓▓▓▓▓▓░░░░░░░░░░▓▓▓▓▓▓░░▓▓              
            ▓▓▒▒▓▓░░░░░░░░░░░░░░░░░░░░▒▒░░  ░░▓▓              
            ▓▓▓▓▓▓░░░░  ██░░░░░░░░░░░░░░██  ░░▓▓              
          ▒▒░░░░░░░░░░    ░░░░░░░░░░░░░░    ░░░░▒▒            
          ▒▒░░░░░░░░░░  ░░░░░░░░░░░░░░░░░░░░░░░░▒▒            
          ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒            
            ▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒              
            ▒▒░░░░░░░░░░              ░░░░░░░░▒▒              
              ▒▒░░░░░░░░░░          ░░░░░░░░▒▒                
              ▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒                
                ▒▒░░░░░░░░░░░░░░░░░░░░░░░░▒▒                  
                  ▒▒▒▒░░░░░░░░░░░░░░░░▒▒▒▒                    
                      ▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒                        
                  ▒▒▒▒▓▓▒▒▒▒░░░░░░░░▓▓▒▒▒▒                    
              ▓▓▓▓░░▓▓  ▓▓░░░░░░░░▓▓  ▓▓░░▓▓▓▓                
            ▓▓░░░░░░▓▓    ▓▓░░░░▓▓    ▓▓      ▓▓              
            ▓▓░░░░  ▒▒▒▒▒▒░░▓▓▓▓░░▒▒▒▒▓▓      ▓▓              
  ░░░░  ░░▓▓░░░░    ░░░░░░░░░░▓▓    ░░  ░░  ░░░░▒▒░░    ░░░░  
          ▓▓░░░░  ░░░░  ░░  ░░▓▓░░░░  ░░        ▓▓            
    ░░  ▒▒░░░░    ▒▒░░  ░░  ░░    ░░      ▒▒░░    ▒▒          
  ░░    ▒▒░░░░  ░░▒▒░░            ░░  ░░░░▓▓░░░░  ▒▒░░  ░░    
        ▓▓░░░░  ▒▒░░░░                    ▓▓░░    ▓▓          
        ▓▓▒▒▒▒▒▒▓▓░░░░                    ▓▓▒▒▒▒▒▒▓▓          
        ▒▒░░░░░░▒▒░░░░                    ▒▒░░░░░░▒▒          
        ▒▒░░░░░░▒▒░░░░                    ▓▓░░░░░░▒▒          
        ▒▒░░░░░░▒▒░░░░                    ▓▓░░░░░░▒▒          
        ▒▒░░░░▒▒▒▒░░░░    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓▓▓▓▓▓▓▓▓
    ▒▒▓▓▒▒░░░░░░▒▒░░░░▒▒▓▓▓▓▒▒▒▒░░░░░░░░░░░░░░░░░░░░▒▒░░░░░░▓▓
    ▓▓▒▒▒▒░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░▓▓
    ▓▓▓▓▒▒░░░░░░░░▒▒▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒▒▒▓▓
          ▒▒▒▒▒▒▒▒░░░░░░░░▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▓▓▓▓
          ░░    ▓▓░░░░    ░░░░░░░░░░░░░░░░▓▓░░                
                ▓▓░░░░      ▓▓▓▓░░░░░░    ▓▓                  
                ▓▓░░░░    ▓▓░░░░▒▒░░░░    ▓▓                  
                ▓▓░░░░    ▓▓    ▓▓░░░░    ▓▓                  
                ▓▓░░░░▒▒▒▒▓▓    ▓▓░░░░▒▒▒▒▓▓                  
                ▓▓░░▒▒░░░░▓▓    ▓▓░░▒▒░░░░▓▓                  
                ▓▓░░▒▒░░░░▓▓    ▓▓░░▒▒▒▒  ▓▓                  
                ▓▓░░▒▒▒▒░░▓▓    ▓▓░░▒▒░░  ▓▓                  
                ▓▓░░▒▒░░░░▓▓    ▓▓░░▒▒▒▒░░▓▓                  
                ▓▓░░▒▒░░  ▓▓    ▓▓░░▒▒░░  ▓▓                  
                ▓▓░░▓▓▓▓▓▓▓▓    ▓▓░░▓▓▓▓▓▓▓▓                  
                ▓▓▓▓░░░░    ▓▓  ▓▓▓▓░░░░    ▓▓                
                ▓▓░░░░░░░░  ▓▓  ▓▓░░░░░░░░  ▓▓                
                ▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓                
                                                              
                                                              
                                                              
                                          ░░░░░░  ░░░░  ░░░░  
''')
print('''
------------------------------- Welcome To The Nostalgic Cricket Game--------------------------------
THIS GAME HAS BEEN PLAYED BY STUDENTS FOR OVER GENERATIONS WITH EACH OTHER.IT IS ALSO POPULARLY CALLED
   AS "ODD OR EVEN".DUE TO THE PANDEMIC, STUDENTS ACROSS ALL GRADES HAVE BEEN GOING INTO DEPRESSION
BECAUSE THEY HAVENT BEEN ABLE TO PLAY THIS LEGENDARY GAME OF CRICKET FOR OVER A YEAR......TO CURE THIS
HUGE WAVE OF SUDDEN DEPRESSION, GAMEHUB HAS RECREATED THIS GAME SO THAT YOU CAN ALWAYS HAVE A BUDDY TO
                       PLAY YOUR FAVOURITE GAME AT THE COMFORT OF YOUR HOMES''')
#toss of the game
time.sleep(4)
print('''                                  COIN TOSS      
                                        
                                           ████████▓▓██              
                                       ████  ░░  ░░  ░░████          
                                     ██  ░░░░░░░░░░░░░░  ░░██        
                                   ██░░░░░░            ░░░░  ██      
                                   ██  ░░                ░░░░██      
                                 ██░░░░      ▓▓▓▓▓▓▓▓      ░░  ██    
                                 ██  ░░    ░░░░░░░░░░▓▓    ░░░░██    
                                 ██░░░░    ░░░░░░░░░░▓▓    ░░  ██    
                                 ██  ░░    ░░░░░░░░░░▓▓    ░░░░██    
                                 ██░░░░    ░░░░░░░░░░▓▓    ░░  ██░░  
                                 ██  ░░      ░░░░░░░░      ░░░░██    
                                   ██░░░░                ░░  ██      
                                   ██  ░░░░            ░░░░░░██      
                                     ██░░  ░░░░░░░░░░░░░░  ██        
                                       ████░░  ░░  ░░  ████     
                                           ████████████              
                                ''')        
                                        
time.sleep(1)
player_choice = input('''
                                     Choose heads or tails = ''')
coin = random.choice(["heads","tails"])
time.sleep(1)
print('''
                                      The coin shows ''',coin)
result_ai=""
result_player=""
final_runs_needed=0

if player_choice==coin:
    time.sleep(0.5)
    print('''
------------------------------------------------------------------------------------------------------
''')
    time.sleep(0.5)
    print('''
                                         you won the toss''')
    time.sleep(0.5)
    print('''
------------------------------------------------------------------------------------------------------
''')
    time.sleep(1)
    player_one_decision=input('''
                                        🏏 batting or bowling ⚾'
 
                                                   ''') 
    result_player+=player_one_decision

else:
    ai_toss_decision = random.choice(["batting","bowling"])
    time.sleep(1)
    print('''
------------------------------------------------------------------------------------------------------
''')
    time.sleep(0.5)
    print('''
                                        You lost the toss''')
    time.sleep(0.5)
    print('''
------------------------------------------------------------------------------------------------------
''')
    time.sleep(1)
    print('''
                                    MOHNISH chooses ''',ai_toss_decision)
    result_ai+=ai_toss_decision
    
if result_player=="batting":
    result_ai+="bowling"
elif result_player=="bowling":
    result_ai+="batting"
elif result_ai=="batting":
    result_player+="bowling"
elif result_ai=="bowling":
    result_player+="batting"

if result_player == "batting":
    time.sleep(1)
    print('''
    ______________________________
 / \                             \.
|   |                            |.
 \_ |                            |.
    |     *Instructions *        |.
    |                            |.
    | You will be playing against|.
    |          MOHNISH           |.
    | best AI in the sport of    |.
    |         cricket            |.
    |      Total 2 overs         |.
    |Score as many runs by using |.
    |     numbers from 0-6       |.                  
    |                            |.
    |   YOU will lose a wicket   |.
    |  if the ai predicts your   |.
    |          number            |.
    |                            |.
    |                            |.
    |        ALL THE BEST        |.
    |              |             |.
    |              |             |.
    |              V             |.
    |   _________________________|___
    |  /                            /.
    \_/____________________________/.

    ''')
    #first innings
    current_player_runs=0
    current_player_wickets=0
    ball=0

    for i in range(12):
        ball+=1
        time.sleep(2)
        print('''
------------------------------------------------------------------------------------------------------
''')
        time.sleep(0.5)
        print('''
                                             ⚾''',ball)
        time.sleep(0.5)
        player_runs_input=int(input('''
                                 Enter your number between 0 to 6 '''))
        time.sleep(0.5)
        print('''
------------------------------------------------------------------------------------------------------
''')
        time.sleep(0.5)
        print('''
                                     You hit a 🏏 ''',player_runs_input,'' )
        ai_bowling_input=random.choice([0,1,2,3,4,5,6])
        time.sleep(0.1)
        print('''
                                    Mohnish bowled a ⚾ ''',ai_bowling_input)
        time.sleep(0.1)
        if player_runs_input == ai_bowling_input:
            current_player_wickets+=1
            time.sleep(1)
            print('''
                                       ITS A WICKET!!!!''')
            time.sleep(0.5)
            print('''
------------------------------------------------------------------------------------------------------
''')
            time.sleep(1)
            print('''
                                  The current score is''',current_player_runs,"/",current_player_wickets)

                
        else:
            current_player_runs+=player_runs_input
            time.sleep(1)
            print('''
                                  The current score is ''',current_player_runs,"/",current_player_wickets)
            final_runs_needed+=player_runs_input
            
        

        
elif result_player=="bowling" :
    time.sleep(1)
    print('''
    ______________________________
 / \                             \. 
|   |                            |.
 \_ |                            |.
    |     *Instructions *        |.
    |                            |.
    | You will be playing against|.
    |          MOHNISH           |.
    | best AI in the sport of    |.
    |         cricket            |.
    |      Total 2 overs         |.
    |   Predict the ai's number  |.
    |     numbers from 0-6 to    |.                  
    |        get a wicket        |.
    |   stop the ai from scoring |.
    |  many runs to make an easy |.
    |          chase             |.
    |                            |.
    |                            |.
    |        ALL THE BEST        |.
    |              |             |.
    |              |             |.
    |              V             |.
    |   _________________________|___
    |  /                            /.
    \_/____________________________/.

    ''')
    current_player_runs_1=0
    current_player_wickets_1=0
    ball_1=0
    for i in range(12):
        ball_1+=1
        time.sleep(2)
        print('''
------------------------------------------------------------------------------------------------------
''')
        time.sleep(0.5)
        print('''
                                             ⚾''',ball_1)
        time.sleep(0.5)
        player_bowling_input_1=int(input('''
                                 Enter your number between 0 to 6 '''))
        time.sleep(0.5)
        print('''
------------------------------------------------------------------------------------------------------
''')
        time.sleep(0.1)

        print('''
                                         You bowled a ⚾ ''',player_bowling_input_1)
        ai_runs_input_1=random.choice([0,1,2,3,4,5,6])
        time.sleep(0.1)
        print('''
                                        Mohnish hit a 🏏 ''',ai_runs_input_1)
        if player_bowling_input_1 == ai_runs_input_1:
            current_player_wickets_1+=1
            time.sleep(1)
            print('''
------------------------------------------------------------------------------------------------------
''')
            time.sleep(0.5)
            print('''
                                     The current score is ''',current_player_runs_1,"/",current_player_wickets_1)
        else:
            current_player_runs_1+=ai_runs_input_1
            time.sleep(0.5)
            print('''
                                      The current score is''',current_player_runs_1,"/",current_player_wickets_1)
            final_runs_needed+=ai_runs_input_1

time.sleep(2)
print('''
----------------------------------------------------------------------------------------------------
@                               _                                  ,,
 \\   _   @'                    ( )_                       .      _  \\
  \\_( )_//                    / Y |                   .      /--( )_//
    | Y/--                    /\   /               .        '//  \~ \
    |_/       _ / o"         ( _\ /            .                   - \
  _ //\      | | |    .       \_\\\        .                     //  \\--,
 /_// /      | | |      .    / \ \\\ .                           \\
/ // /_______|_|_|__________/_/_\ \_______________________________\\________________________________
-------------------------------------------- 2nd innings -------------------------------------------
''')
print('''
                                                |
                                                |
                                                |
                                                |
                                                |
                                                |
                                                |
                                                V
                                                       ''')
final_runs_needed+=1
if result_player=="batting":
    time.sleep(1)
    print('''
                                      mohnish needs''',final_runs_needed,"to win")
elif result_player=="bowling":
    time.sleep(1)
    print('''
                                         you need''',final_runs_needed,"to win")
elif result_ai=="batting":
    time.sleep(1)
    print('''
                                      you need''',final_runs_needed,"to win")
elif result_ai=="bowling":
    time.sleep(1)
    print('''
                                      mohnish needs''',final_runs_needed,"to win")
    
t2_innings_player=""  
t2_innings_ai=""

if result_player=="batting":
    result_ai+="bowling"
    t2_innings_player+="bowling"
    t2_innings_ai+="batting"
elif result_player=="bowling":
    result_ai+="batting"
    t2_innings_player+="batting"
    t2_innings_ai+="bowling"
elif result_ai=="batting":
    result_player+="bowling"
    t2_innings_player+="batting"
    t2_innings_ai+="bowling"
elif result_ai=="bowling":
    result_player+="batting"
    t2_innings_player+="bowling"
    t2_innings_ai+="batting"

time.sleep(0.5)
    
print('''
------------------------------------------------------------------------------------------------------
''')   
if t2_innings_player == "batting":
    time.sleep(0.2)
    print('''
                                    You need to get''',final_runs_needed,"to win")
    t2ndinnings_player_runs=0
    t2ndinnings_player_wickets=0
    ball=0
    final_runs=0
    for i in range(12):
        time.sleep(0.5)
        
        print('''
------------------------------------------------------------------------------------------------------
''') 
        ball+=1
        time.sleep(0.5)
        print('''
                                              ⚾''',ball)
        time.sleep(0.2)
        player_runs_input=int(input('''
                                 Enter your number between 0 to 6 '''))
        time.sleep(0.5)
        print('''
------------------------------------------------------------------------------------------------------
''')
        time.sleep(0.1)

        print('''
                                   You hit a 🏏 ''',player_runs_input)
        ai_bowling_input=random.choice([0,1,2,3,4,5,6])
        time.sleep(0.1)
        print('''
                                   Mohnish bowled a ⚾ ''',ai_bowling_input)
        if player_runs_input == ai_bowling_input:
            t2ndinnings_player_wickets+=1
            time.sleep(0.5)
            print('''
------------------------------------------------------------------------------------------------------
''')
            time.sleep(0.2)
            print('''
                                       The current score is ''',t2ndinnings_player_runs,"/",t2ndinnings_player_wickets)     
        else:
            t2ndinnings_player_runs+=player_runs_input
            time.sleep(0.2)
            print('''
------------------------------------------------------------------------------------------------------
''')
            time.sleep(0.2)
            print('''
                                       The current score is''',t2ndinnings_player_runs,"/",t2ndinnings_player_wickets)
            final_runs+=t2ndinnings_player_runs



    
elif t2_innings_player=="bowling":
    time.sleep(0.2)
    print('''
------------------------------------------------------------------------------------------------------
''')
    time.sleep(0.2)
    print('''
                                    You need to defend''',final_runs_needed," runs to win")
    t2ndinnings_player_runs_1=0
    t2ndinnings_player_wickets_1=0
    ball_1=0
    final_runs_1=0
    for i in range(12):
        ball_1+=1
        time.sleep(0.5)
        print('''
------------------------------------------------------------------------------------------------------
''')
        time.sleep(0.2)
        print('''
                                                 ⚾''',ball_1)

        player_runs_input_1=int(input('''
                                             Enter from 0 to 6 '''))
        time.sleep(0.2)
        print('''
                                             You bowled a ⚾ ''',player_runs_input_1)
        ai_runs_input_1=random.choice([0,1,2,3,4,5,6])
        print('''
                                              Mohnish hit a 🏏 ''',ai_runs_input_1)
        if player_runs_input_1 == ai_runs_input_1:
            t2ndinnings_player_wickets_1+=1
            time.sleep(0.2)
            print('''
------------------------------------------------------------------------------------------------------
''')
            time.sleep(0.2)
            print('''
                                       The current score is ''',t2ndinnings_player_runs_1,"/",t2ndinnings_player_wickets_1)

        else:
            t2ndinnings_player_runs_1+=ai_runs_input_1
            time.sleep(0.2)
            print('''
------------------------------------------------------------------------------------------------------
''')
            time.sleep(0.2)
        
            print('''
                                       The current score is ''',t2ndinnings_player_runs_1,"/",t2ndinnings_player_wickets_1)
            final_runs_1+=ai_runs_input_1
        
                
#results






            
print("the end")




