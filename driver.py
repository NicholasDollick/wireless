import bt
import empldb
import threading
from datetime import datetime

#DB functions needed
#read db function that returns every piece of information given first name, last name, macadr.
#read db function that returns every piece of information given device name, mac address.
# or a read db function that returns list of every piece of info given whatever value as argument e.g. firstname, device name, etc.
#change db function that when given a mac address, table argument, and user input will replace that value on that table for the specified mac address.
#delete function given a mac address delete whole data entry

#thread function to actually continously scan for devices and record clock in/out info
def scan():
    discovered = run_scan()
    #check if device and mac address are on table for loop each device in the list
    #if not we append that device name combo into the db
    #check if the device is an employee if not in db
    #if an employee we send a 2FA email to that person
    #once they reply to that email
    #How to keep track of clock in clock out?
    #prompts about clocking in
    #prompts about clocking out

#function to create/set as employee given device name and mac address
def AddToDB():
    ##ask for employee device name
    print("To set a device as an employee, please provide the device name")
    deviceName = input("Please input the device name.")

    ##Check if device exists in database
    #retTuple = readDB(device, mac address)
    #if retTuple == null idk if this is the right way to check a tuple
    #print("Device not found in database")
    #return

    ##check if already an employee
    #bool employed = false
    #(FirstN, LastN, DeviceName, MAC, IsEmployee) = retTuple #unpackage tuple
    #if(IsEmployee == true)
        #employed == true

    #if(employed)
        #print("The device mac address pair indicates the user is already set as employed")
        #return

    ##return information about that device
    #(ID, FirstN, LastN, DeviceName, MAC, IsEmployee) = retTuple #unpackage tuple
    #print("ID: " + ID, end =" ")
    #print("First Name: " + FirstN, end =" ")
    #print("Last Name: " + LastN, end =" ")
    #print("DeviceName: " + DeviceName, end ="")
    #print("MAC: " + MAC, end = " ")
    #print("IsEmployee: " + IsEmployee, end=" ")

    #confirmation
    getInput = False
    while(getInput == False):
        userInput = input("Would you like to set this device as employee? y/n")
        if(userInput == 'y'):
            getInput = True
        elif(userInput == 'n'):
            return
        else:
            print("invalid input: try again")

    ##set as employee
    firstN = input("Please input employee first name.")
    lastN = input("Please input employee last name.")
    #set_employee(,firstN, lastN, deviceName) #what does the self arg do?


#Given Mac Address, delete from table
def DeleteFromDB():
    ##ask for mac address
    macAdr = input("To delete an employee, please provide the mac address of the device")

    ##Check if device exists in database
        #retTuple = readDB(mac address)
        #if(retTuple == null)
            #print("Device not found in database")
            #return

    ##display information about that mac address e.g. read from db
    #(ID, FirstN, LastN, DeviceName, MAC, IsEmployee) = retTuple #unpackage tuple
    #print("ID: " + ID, end =" ")
    #print("First Name: " + FirstN, end =" ")
    #print("Last Name: " + LastN, end =" ")
    #print("DeviceName: " + DeviceName, end ="")
    #print("MAC: " + MAC, end = " ")
    #print("IsEmployee: " + IsEmployee, end=" ")

    ##ask for confirmation
    getInput = False
    while(getInput == False):
        userInput = input("Would you like to delete this employee? y/n")
        if(userInput == 'y'):
            getInput = True
        elif(userInput == 'n'):
            return
        else:
            print("invalid input: try again")

    ##delete whole data entry
            #deleteDB(macAdr)

#function to return info of employee
def ReadFromDB():

    ##get device name and mac address
    print("To return info about an employee please give the first name, last name, and mac address")
    firstN = input("Please input the first name.")
    lastN = input("Please input the last name.")
    macAdr = input("please input the mac address.")

    ##Check if employee exists in database
    #retTuple = readDB(firstN,lastN, macAdr)
    #if retTuple == null idk if this is the right way to check a tuple
    #print("Employee not found in database")
    #return

    ##Check if an employee
    #bool employed = false

    #(FirstN, LastN, DeviceName, MAC, IsEmployee) = retTuple #unpackage tuple
    #if(IsEmployee == true)
        #employed == true

    #if(employed)
        #print("MAC Address does not return a device that belongs to an employee")
        #return

    ##print out that employee information
    #(ID, FirstN, LastN, DeviceName, MAC, IsEmployee) = retTuple #unpackage tuple
    #print("ID: " + ID, end =" ")
    #print("First Name: " + FirstN, end =" ")
    #print("Last Name: " + LastN, end =" ")
    #print("DeviceName: " + DeviceName, end ="")
    #print("MAC: " + MAC, end = " ")
    #print("IsEmployee: " + IsEmployee, end=" ")

#Function to change value in DB
#def ChangeFromDB():
    ##Take mac adress as input
    #print("To change info of an employee, please provide the MAC address of the device")
    #macAdr = input("Please input the MAC address.")

    ##Check if employee exists
    #retTuple = readDB(firstN,lastN, macAdr)
    #if retTuple == null idk if this is the right way to check a tuple
    #print("Employee not found in database")
    #return

    ##Check if an employee
    #bool employed = false

    #(FirstN, LastN, DeviceName, MAC, IsEmployee) = retTuple #unpackage tuple
    #if(IsEmployee == true)
        #employed == true

    #if(employed)
        #print("MAC Address does not return a device that belongs to an employee")
        #return

    ##read db info, print it out
    #(ID, FirstN, LastN, DeviceName, MAC, IsEmployee) = retTuple #unpackage tuple
    #print("ID: " + ID, end =" ")
    #print("First Name: " + FirstN, end =" ")
    #print("Last Name: " + LastN, end =" ")
    #print("DeviceName: " + DeviceName, end ="")
    #print("MAC: " + MAC, end = " ")
    #print("IsEmployee: " + IsEmployee, end=" ")

    ##then we get input to see what value you want to change
    #value = input("What value would you like to change?")
    #valueTo = input("What would you like to change that value to?")

    ##then change it e.g. change db function
    #changeDB(mac, value, valueTo)

def main():
    print("Welcome to the BT Timecard Interface.")
    print("To add an employee to the database use the 'add' command.")
    print("To delete an employee to the database 'delete' command.")
    print("To change an employee info in the database use the 'change' command.")
    print("To read from the database use the 'read' command.")
    print("To quit use the 'quit' command.")
    done = False
    while(done == False):
        userInput = input("Please input a command")

        #Check if user input is a string
        if(userInput.isalpha()):
            print("invalid input: try again")

        #Check for user input
        if(userInput == 'add'):
            AddToDB()
        elif(userInput == 'delete'):
            DeleteFromDB()
        # elif(userInput == 'change'):
        #     ChangeFromDB()
        elif(userInput == 'read'):
            ReadFromDB()
        elif(userInput == 'quit'):
            done = True
        else:
            print("invalid input: try again")

if __name__ == "__main__":
    main()