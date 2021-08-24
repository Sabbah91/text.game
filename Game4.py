while True:
    print(' ')
    answer=input ("Do you wanna play a game?(Yes/NO)\n"+'> ')
    if answer.lower() == 'yes':
        name=input('please enter your name:  '+'\n> ')
        print(" ")
        print('  Wassup ',name,'\U0001F60A'""". 
\U000027A1It's a warm summer evening A.D. 
you finish shoping at your local market and you headed out to your hotel \U0001F3E8,
and you look up at the star wondering,
then a black van stop in front of you grab you and throwing your body into that van 
you suddenly wake-up,find yourself into an empty room, you hear voices through the wall 
(screaming and curses), then a gun shot cut all the voices and a foot steps 
approaching to your room, what would you do
         """)
        answer=input('(stay put/ambush him):'+'\n> ')
        print('')
        if answer.lower() =='stay put':
            print(f"""
  He's standing in front of you and said somthings you dont understand obviously 
it's a foreign language, then he said "5 minutes {name}"and he headed out
what would you do now, stop him and try to be reasonable and
find out what he want or you'll going crazy and charge toward him 
with the lawn chair you setting on   
""")
            answer=input("stop him/attack:"+'\n> ')
            print('')
            if answer.lower() == 'stop him':
                print("""
He looked at you and say some words you dont understand 
then headed out and look the door, 
few minutes later he come back with another guy luckely this new guy can speak english ,
he ask "Are you the delevery man" 
""")
                answer=input('Answer me he said (yes/no)'+'\n> ')       
                if answer.lower() == 'yes':
                    print("""
they ask you about stuff, 
And of corse you know nothing they torture  you for hours, 
at the end they find out that  you are useless and get rid of you 
GAME OVER
""")            
                elif answer.lower( )=='no':
                  print(f"""
 Then prove it !!
 You tell them everything, where are you from and why you are here in JAPAN,
 they send someone to your hotel room he find your ID and he read  the name {name}
 NOW they belive you and 
 they give you 10 hours to go out of this country and never come back
 You made it out Alive Congrats 'WE HAVE A WINNER!!
 """)         
            elif answer.lower() == 'attack':
               print("""
you tried to attack him 
but he hear your foot steps  turn around quickly dodge your stupid attack, 
then he beat the shit out of you till you black out
Finally you woke-up, the  man ask you "for the last time where are they" 
you tried to deffence yourself but no matter what you say he did not belive you 
because you tried to attack him,
At the end he look at you and say any last word before you say anything "BAMM"  
You are dead GAME OVER 
""")  
        elif answer =='ambush him':
            print("""
You find a medium size rock here,
you have 2 choices stand behind the door or lay on the ground. 
""")
            answer10=input("what would you choose >>> (door/ground)"+'\n> ')
            print(" ")    
            if answer10 == 'door':
                print("""
you stand behind the door and the second he enter "BAMMM" 
you crash his head and knock him down then you search him and you find: 
(electric key,small knife, piece of paper has 4 digit  "9191") 
you memorise it then quickly headed outside the room. Outside you find 2 paths (up/down) stairs:  
""")
                answer=input("Up/down"+'\n> ')
                if answer == 'up':
                   print("""
You headed up, all the doors are locked,
so you go up to the roof and you find a stairs
attach to the building, you use them to flee
Congrats you made it out, You Win!!   
""")            
                elif answer.lower() == 'down':
                    print("""
You headed down find a door you use the electrical key to open it,
2 second later you hear a machine vocie saying: 
""")  
                    answer=input('Please input the security number: '+'\n> ')
                    if answer == '9191':
                       print("""
Access comfirmed;
the door is open now and you faced 2 ofthe giant man(they were headed out) 
and the security guy( stand in the corner) you pulled your gun up shot the firts guy but they shot you back immediately
you are laying on the ground woonded but you killed one of them so you're dead 
GAME OVER !! 
""")      
                    else:
                       print("""
Access denied please look at the camera (now the security guy notice and saw you ). 
You have been spoted!! GAME OVER!! they definitely gonna kill you 
""")      
            elif answer10.lower()== 'ground':
                print("""
He enter the room man with a gun in his hand 
(and at this moment you know that you are messed up) 
you tried to smash his head but he dodge your move and knock you out,
later they find you're useless and kill you,
GAME OVER !!
""")
    else:
        print("Then GO away \U0001F620 ")