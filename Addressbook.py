#!/usr/bin/python3.9
#Mini Project: Addressbook
#Author: Pooria Taghdiri
#Student ID: 40090326
#Email: pooria.taghdiri@mail.concordia.ca

#Building the Personal Contant management which contains the attributes of: 
#---> Name 
#---> Surname 
#---> address
#---> email
#---> tel numbers
#---> Keywords used to facilitate the search
#and the methods of 
#---> Adding a new contact.
#---> Deleting a contact. (Searching by keywords)
#---> Viewing the detailed information of a contact. (Searching by keywords)
#---> Modifying the information of a contact. (Searching by keywords)
#---> Showing full list of contacts.

##########################################
#Importing the required library 
import csv
import os.path

##########################################
#Defining the required classes

#Personal info (Name and Surname)
#Parent 1
class Person():
    # Initialization
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        
#Parent 2
class Info:
    # Initialization
    def __init__(self, tel, email, address, keyword):
        self.tel = tel
        self.email = email
        self.address = address
        self.keyword = keyword



#Child class (Contact)
class Contact(Person,Info):
    def __init__(self, index, name="", surname="", tel="0", email="", address=""):
        #Creating keyword based on the name and surename without any space
        keyword = name.lower() + surname.lower()
        self.index = index
        Person.__init__(self, name, surname)
        Info.__init__(self, tel, email, address, keyword)
    
    #MEthod of adding initial data of new Obj in newline of CSV file    
    def addToCSV(self):
        #Adding the new contact to CSV
        filename = "contact.csv"
        fields = []
        rows = []
        new_row = [self.index, self.name, self.surname, self.tel, self.email, self.address]
        #Reading the whole data from CSV file
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            # extracting field names through first row
            fields = next(csvreader)
            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)
            
            rows.append(new_row)
            
        #Write or Rewrite the rows in CSV file    
        with open(filename, 'w') as csvfile:   
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing the fields
            csvwriter.writerow(fields)
            # writing the data rows
            csvwriter.writerows(rows)
        
    #Method of searching the contact based on the keyword        
    def searchByKeyword(self, searchItem):
        if searchItem == self.keyword:
            return True
        else:
            return False
    
    #Method of deleting the selected contact from CSV file
    def deleteFromCSV(self):
        idx = self.index
        filename = "contact.csv"
        fields = []
        rows = []
        
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            # extracting field names through first row
            fields = next(csvreader)
            # extracting each data row one by one
            for row in csvreader:
                if row[0] == idx:
                    continue
                elif row[0] > idx:
                    row[0] -= 1
                rows.append(row)
                
        with open(filename, 'w') as csvfile:    
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing the fields
            csvwriter.writerow(fields)
            
            # writing the data rows
            csvwriter.writerows(rows)
        
    #Method of modifying the selected contact in the CSV 
    def ModifyContact(self,new_name, new_surname, new_tel, new_email, new_address):
        new_keyword = new_name + new_surname
        self.name = new_name
        self.surname = new_surname
        self.tel = new_tel
        self.email = new_email
        self.address = new_address
        self.keyword = new_keyword
        
        #Modify the CSV file
        idx = self.index
        filename = "contact.csv"
        fields = []
        rows = []
        
        # reading csv file
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            # extracting field names through first row
            fields = next(csvreader)
            # extracting each data row one by one
            for row in csvreader:
                if row[0] == idx:
                    row = [idx, new_name, new_surname, new_tel, new_email, new_address ]
                rows.append(row)
                
        with open(filename, 'w') as csvfile:    
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing the fields
            csvwriter.writerow(fields)
            # writing the data rows
            csvwriter.writerows(rows)
    
    #Method of inquiry the full list of all contacts
    def viewInfo(self):
        text1 = str(self.index) + "-" + self.name + " " + self.surname
        text2 = "\n    ---> Tel:" + self.tel 
        text3 = "\n    ---> Email:" + self.email
        text4 = "\n    ---> Address:" + self.address + "\n"
        totText = text1 + text2 + text3 + text4
        print(totText)
        
    
    
##########################################
#Defining the required functions

#Initializing the CSV file tosave thecontacts
def initialization():
    #First, we have to check whether the file exists
    filename = "contact.csv"
    # field names
    fields = []
    rows = []
 
    if not os.path.exists(filename):
        fields = ['No', 'Name', 'Surname', 'Telephone #', 'Email', 'Address']
        with open(filename, 'w') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing the fields
            csvwriter.writerow(fields)
    else:
        # reading csv file
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            # extracting field names through first row
            fields = next(csvreader)
            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)
        
    return rows        

           
##########################################
#Main 
if __name__ == "__main__":
    welcomeMsg = "Welcome to Contact Manager ...!!!"
    print(welcomeMsg)
    print("*"*len(welcomeMsg))
    
    #Initialization
    option = 0
    initial_data = initialization()
    objLst = []
    for item in initial_data:
        objLst.append(Contact(
                    item[0], item[1], item[2], item[3], item[4], item[5]
                ))
    
    #Main route of menu
    while True:
        print("Insert the number of your option")
        print("1. Adding new contact")
        print("2. Deleting the contact")
        print("3. Viewing the detailed information of a contact")
        print("4. Modifying the information of a contact")
        print("5. Showing the full list of contacts")
        print("6. Quit?!\n")
        
        while option not in list(range(1,7)):
            try:
                option = int(input("Enter the number of your option: "))
            except: 
                print("Number is only valid to choose the option...")
            print("\n")
            
        
        if option == 1:
            print("Please enter the related information:")
            print("_____________________________________")
            name = input("Name: ").strip()
            surname = input("Surname: ").strip()
            tel = input("Telphone number: ").strip()
            email = input("Email Address: ").strip()
            address = input("Address: ").strip()
            idx = len(objLst) + 1
            if name != "":
                objLst.append(Contact(
                    idx, name, surname, tel, email, address
                ))
                objLst[len(objLst)-1].addToCSV()
            else:
                print("You didn't enter the name!!!\n")
                
        elif option == 2:
            print("Search the contact based on the keywords")
            print("KEYWORD: a combination of name and surname without space")
            insertedKeyword = input("Insert the keyword: ").strip().lower()
            
            for obj in objLst:
                if obj.searchByKeyword(insertedKeyword):
                    obj.deleteFromCSV()
                    objLst.remove(obj)
            else:
                print("There is no such an item.\n")
            
        elif option == 3:
            print("Search the contact based on the keywords")
            print("KEYWORD: a combination of name and surname without space")
            insertedKeyword = input("Insert the keyword: ").strip().lower()
            
            for obj in objLst:
                if obj.searchByKeyword(insertedKeyword):
                    obj.viewInfo()   
                    break                 
            else:
                print("There is no such an item.\n")
                    
        elif option == 4:
            print("Search the contact based on the keywords")
            print("KEYWORD: a combination of name and surname without space")
            insertedKeyword = input("Insert the keyword: ").strip().lower()
            
            for obj in objLst:
                if obj.searchByKeyword(insertedKeyword):
                    print("The old contact info: ")
                    obj.viewInfo()
                    
                    print("Enter the new information:")
                    name = input("Name: ").strip()
                    surname = input("Surname: ").strip()
                    tel = input("Telphone number: ").strip()
                    email = input("Email Address: ").strip()
                    address = input("Address: ").strip()
                    obj.ModifyContact(name,surname,tel,email,address)
                    break
            else:
                print("There is no such an item.\n")
            
        elif option == 5:
            print("Showing the full list of contacts \n")
            for obj in objLst:
                obj.viewInfo()
        elif option == 6:
            print("Goodbye!!!")
            break
        
        #Reset the option
        option = 0
