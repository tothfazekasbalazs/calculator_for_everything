import time
import colorama

def main():

    def kilepes():
        print("\nA rendszer 3 másotperc múlva bezárja magát")
        time.sleep(3)
        exit()

    
    def choice():

        print("""
   ____        _  _               _         _                  _                ____                    _  
  / ___| __ _ | || |  ___  _   _ | |  __ _ | |_  ___   _ __   | |__   _   _  _ | __ )   __ _  ____ ___ (_) 
 | |    / _` || || | / __|| | | || | / _` || __|/ _ \ | '__|  | '_ \ | | | |(_)|  _ \  / _` ||_  // __|| | 
 | |___| (_| || || || (__ | |_| || || (_| || |_| (_) || |     | |_) || |_| | _ | |_) || (_| | / / \__ \| | 
  \____|\__,_||_||_| \___| \__,_||_| \__,_| \__|\___/ |_|     |_.__/  \__, |(_)|____/  \__,_|/___||___/|_| 
                                                                      |___/                                """)

        print("""
    Ez egy számológép alkalmazás:

    Válaszd ki a neked kellő művelet számat.
        
        (0) Kilépés
        (1) Összeadás
        (2) Kivonás
        (3) Szorzás
        (4) Osztás 
        (5) Négyzetre emelés
        (6) Négyzet gyökvonás
        (7) Kerület
        (8) Terület 
              
              """)

        global user_choise
        user_choise = input("Választásod? ")  

        if user_choise == "0":
            kilepes()

        elif user_choise == "1":
            input_1 = int(input("\nMennyit szeretnél összeadni: "))
            input_2 = int(input("\nMenyit szertnél hozzáadni: "))
            eredmeny = input_1 + input_2  
            print(f"\n Az szamolás eredménye: {eredmeny}") 

        elif user_choise == "2":
            input_1 = int(input("\nMennnyiből szeretnél kivonni: "))
            input_2 = int(input("\nMennyit?: "))
            eredmeny = input_1 - input_2  
            print(f"\n Az szamolás eredménye: {eredmeny}") 

        elif user_choise == "3":
            input_1 = int(input("\nMennyit szeretnél összeszorozni: "))
            input_2 = int(input("\nMenyivel: "))
            eredmeny = input_1 * input_2  
            print(f"\n Az szamolás eredménye: {eredmeny}") 

        elif user_choise == "4":
            input_1 = int(input("\nMennyit szeretnél osztani: "))
            input_2 = int(input("\nMenyivel: "))
            eredmeny = input_1 / input_2  
            print(f"\n Az szamolás eredménye: {eredmeny}")   

        elif user_choise == "5":
            input_1 = int(input("\nMennyit szeretnél négyzetre emelni: "))
            eredmeny = input_1 ** input_1  
            print(f"\n Az szamolás eredménye: {eredmeny}") 


        elif user_choise == "6":
            input_1 = int(input("\nMennyit szeretnél osztani: "))
            input_2 = int(input("\nMenyivel: "))
            eredmeny = input_1 ** 0,5  
            print(f"\n Az szamolás eredménye: {eredmeny}")                            

        else:
            print("\nIlyer érték nincs felsorolva")  
            choice()

    def repait():
        user_continue = input("\nSzeretnéd folytatni? ( igen / nem ) ")

        if user_continue == "igen":
            kilepes()

        elif user_continue == "nem":            
            kilepes()

        else:
            print("\nIlyen érték nincs megadva.")
            repait()

    choice()
    repait()

main()