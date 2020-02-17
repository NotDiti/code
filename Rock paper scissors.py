
import random 
  

print("Rregullat e lojes gur leter gersher: \n"
                                +"guri vs letra->letra wins \n"
                                + "guri vs gershera->guri wins \n"
                                +"letra vs gershera->gershera wins \n") 
  
while True: 
    print("zgjeghni \n 1. guri \n 2. letra \n 3. gershera \n") 
     
    choice = int(input("lojtari luan: ")) 
  
    
    while choice > 3 or choice < 1: 
        choice = int(input("shkruani nje numer valid: ")) 
          
  
  
    if choice == 1: 
        choice_name = 'guri'
    elif choice == 2: 
        choice_name = 'letra'
    else: 
        choice_name = 'gershera'
          
   
    print("zgjedhja e lojtarit esht: " + choice_name) 
    print("\ntani esht rradha e kompjuterit.......") 

    comp_choice = random.randint(1, 3) 
      
   
    while comp_choice == choice: 
        comp_choice = random.randint(1, 3) 
  
    if comp_choice == 1: 
        comp_choice_name = 'guri'
    elif comp_choice == 2: 
        comp_choice_name = 'letra'
    else: 
        comp_choice_name = 'gershera'
          
    print("zgjedhja e kompjuterit esht: " + comp_choice_name) 
  
    print(choice_name + " V/s " + comp_choice_name) 
  
   
    if((choice == 1 and comp_choice == 2) or
      (choice == 2 and comp_choice ==1 )): 
        print("letra fiton => ", end = "") 
        result = "letra"
          
    elif((choice == 1 and comp_choice == 3) or
        (choice == 3 and comp_choice == 1)): 
        print("guri fiton =>", end = "") 
        result = "guri"
    else: 
        print("gershera fiton =>", end = "") 
        result = "gershera"
  
   
    if result == choice_name: 
        print("<== lojtari fiton ==>") 
    else: 
        print("<== kompjuteri fiton ==>") 
          
    print("Deshironi qe te luani prap? (P/J)") 
    ans = input() 
  
   
    if ans == 'j' or ans == 'J': 
        break
      
print("\nFaleminderit qe luajtet") 