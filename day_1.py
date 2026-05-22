"""
 Challenge: CLI Contact Book (CSV-Powered)

Create a terminal-based contact book tool that stores and manages contacts using a CSV file.

Your program should:
1. Ask the user to choose one of the following options:
   - Add a new contact
   - View all contacts
   - Search for a contact by name
   - Exit
2. Store contacts in a file called `contacts.csv` with columns:
   - Name
   - Phone
   - Email
3. If the file doesn't exist, create it automatically.
4. Keep the interface clean and clear.

Example:
Add Contact
View All Contacts
Search Contact
Exit

Bonus:
- Format the contact list in a table-like view
- Allow partial match search
- Prevent duplicate names from being added
"""

import csv
import os

FILE_NAME = "contacts.csv"

if not os.path.exists(FILE_NAME):
    with open(FILE_NAME , "w" , newline="" , encoding= "utf-8") as f:
       writer = csv.writer(f)
       writer.writerow(["Name" , "Phone" , "Email" , "Address"])

def add_user():
    name    = input("Name: ").strip()
    phone   = input("Phone no: ").strip()
    email   = input("Email:  ").strip()
    address = input("Address: ").strip()

#check for duplicates
    with open(FILE_NAME , "r" , encoding="utf-8") as f :
        reader = csv.DictReader(f)
        for row in reader:
             if row["Name"].lower() == name.lower():
                 print("Contact already exists!")
                 return

    with open(FILE_NAME , "a" , encoding="utf-8") as f:
           writer = csv.writer(f)
           writer.writerow([name,phone,email,address])
           print("Contact added!")

def view_contacts():
    with open(FILE_NAME , "r" ,newline="" ,encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

        if len(rows) < 1:
            print("No contact found!")
            return
        
        print("\n Your Contacts \n")

        for row in rows[1:]:
              if len(row) == 0:
                  continue
              print(f" {row[0]} | {row[1]} | {row[2]} | {row[3]}")
              print()

def search_contact():
     search = input("Enter the name you want to search: ").strip()
     found = False

     with open(FILE_NAME , "r" , encoding="utf-8") as f:
      reader = csv.DictReader(f)
      for row in reader:
        if  search in row["Name"]:
              print(f"{row["Name"]}  | 📞 {row["Phone"]}")
              found = True 
              return
        if not found:
             print("No contact match found!")


def main():
    while True:
        print("1.ADD CONTACT")
        print("2.VISIT ALL CONTACTS")
        print("3.SEARCH CONTACT")
        print("4.EXIT")

        contact = input("Select the option (1-4)")

        if contact == "1":
            add_user()
        elif contact == "2":
            view_contacts()
        elif contact == "3":
            search_contact()
        elif contact == "4":
             print("Thanks for using our software")
             break
        
        else:
            print("Invalid option")


if __name__ == "__main__":
    main()