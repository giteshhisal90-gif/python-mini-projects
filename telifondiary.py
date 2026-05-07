# we are going to make teliphone diary
import pyttsx3
tel_diatry = {}

while True:
    a ="---TELIPHONE DIARY---"
    pyttsx3.speak("Wellcome to telephone diary")
    print("\n")
    print(a.center(100))
    print("1. Add contact")
    print("2. Deleat contact")
    print("3. view all contact")
    print("4. search contact")
    print("5. Exit\n")
    pyttsx3.speak("what you want to do ?")
    choice = input("Enter a choice : ")

    match choice :
        case "1":
            name =input("Enter a name : ").capitalize()
            contact = input("Enter a contact number :")
            tel_diatry[name] = contact
            print("contact save sucessfully")
            pyttsx3.speak("contact save sucessfully")
        case "2":
            name = input("Enter name for Deleat : ").capitalize()
            if name in tel_diatry:
                del tel_diatry[name]
                print("contact Deleat sucessfully")
                pyttsx3.speak("contact deleated sucessfully")
            else:
                print("contact not found")
                pyttsx3.speak("contact not found")
        case "3":
            if tel_diatry:
                print("All contact :")
                pyttsx3.speak("These are all contact avalable")
                for name ,contact in tel_diatry.items():
                    print(name.capitalize(),":",contact)
            else:
                print("no contact avalable")
                pyttsx3.speak("contact not avalable")
        case "4":
            name = input("Enter a name to search :").capitalize()
            if name in tel_diatry:
                print(f"phone Number : {tel_diatry[name]} ")
                pyttsx3.speak("this result found")
            else:
                print("contact not found")
                pyttsx3.speak("contact not found")
        case "5":
            print("Thanks for visiting us 😊😊💕 ")
            pyttsx3.speak("Thank you for visiting")
            break
        case _ :
            print('Thise operation is not alloketed')
            pyttsx3.speak("Thise operation is not alloketed")




