import pyttsx3
import random
import string
import time

def generate_id():
    digits = list(str(random.randint(1000, 9999)))
    letters = random.choices(string.ascii_letters, k=4)
    
    combined = digits + letters
    random.shuffle(combined)
    
    return ''.join(combined)

pyttsx3.init()

name = input("Enetr player name: ")
code = generate_id()

text1 = f'''Wellocome Mr.{name}
player player ID is {code}'''

pyttsx3.speak(text1)


while True:
    def check():
      
        if user == comp:
            return 0
        elif user == 1 and comp == 3:
            return -1
        elif user == 2 and comp ==1:
            return -1
        elif user == 3 and comp == 2:
            return -1
        else:
            return 1

    comp = random.randint(1,3)
    a = "!!! snake water Gun game !!!"
    pyttsx3.speak(f"Wellcome to {a}")
    print(a.center(50))
    print("1.snake")
    print("2.water")
    print("3.Gun")
    print("4.Exit")

    text ="please choose your option"
    pyttsx3.speak(text)
    user = int(input("Enter a choice : "))
    time.sleep(2)
    if user >4:
            instruction = "enter valid choice"
            print(instruction)
            pyttsx3.speak(instruction)
            continue
    if user==4:
            t ="Thank you for play !!"
            print(t.center(50))
            pyttsx3.speak(t)
            break
    if check() == 0:
        result = "Draw"
        print(result)
        pyttsx3.speak(result)
        
    elif check() == -1:
        result = "You Loss"
        print(result)
        pyttsx3.speak(result)
    else:
        result = "You Won"
        print(result)
        pyttsx3.speak(result)