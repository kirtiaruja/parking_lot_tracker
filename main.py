'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
import os
import time
parking_slots = [None for ele in range(40)] 


def parking():
    exit = 1
    while exit:
        os.system('clear')
        print("\t \t WELCOME\n")
        print("\tSelect Option :\n")
        print("\t Press 1 To Park Vehicle")
        print("\t Press 2 To Check Parking Slot\n\n")
        
        arg = int(input("\t Enter Choice>> "))
        os.system('clear')
        match arg:
            case 1:
                print("\t \t Park Vehicle\n")
                print("\t Enter Vehicle Number To Park:\n")
                vehicle_no = (input("\t >> "))
                print("\t \t",vehicle_park(vehicle_no))
                time.sleep(3)
                os.system('clear')
                  
            case 2:
                print("\t \t Check Parking Slot\n")
                print("\t Enter Vehicle Number To Find:\n")
                vehicle_no = (input("\t >> "))
                print("\t",retrive_slot(vehicle_no))
                time.sleep(5)
                
        os.system('clear')       
        print("\t\t Select Option :\n")
        print("\tPress 0 To Exit")
        print("\tPress 1 For Main Menu")
        exit = int(input("\t >> "))    

def vehicle_park(vehicle_no):
    for spot in range(40):
        if(parking_slots[spot] == None):
            parking_slots[spot] = vehicle_no
            return "Done!"
            
def retrive_slot(vehicle_no):
    check = 0;
    while check < len(parking_slots) and parking_slots[check] != vehicle_no:
        check += 1
    if(check >= 0 and check <= 20):
        return {'level':'A', 'spot':check}
    elif(check >= 21 and check <= 40):
        return {'level':'B', 'spot':check}
    else:
        return "Not Found"
        

parking()
print("\t \t Thank You!!")