contact = {}
def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
     print("{}\t\t{}".format(key, contact.get(key)))

while True:
    choice=int(input(" 1. add a new contact \n 2. Search a Contact \n 3. Display Contact \n 4. Edit Contact \n 5. Delete Contact. \n 6. Exit \n Enter your choice: " ))
    if choice== 1:
        name = input("Enter the name of the contact :")
        phone = input("Enter the contact of "+name)
        contact[name] = phone
    elif choice == 2:
        search_name = input("Enter the name of the contact you are looking for : ")
        if search_name in contact:
            print(search_name,"'s contact number is ",contact[search_name],":")
        else:
            print("No contact with that name :")
    elif choice == 3:
        if not contact:
            print("Empty contact")
        else:
            display_contact()
    elif choice == 4:
        edit_contact = input("Enter the contact name to be edited: ")
        if edit_contact in contact:
            phone = input("Enter the edited contact number: ")
            contact[edit_contact] = phone
            print("Contact updated")
            display_contact()
        else:
         print("No contact with that name")
    elif choice == 5:
        delete_contact = input("Enter the contact's name to be deleted :")
        if delete_contact in contact:
            contact.pop(delete_contact)
            display_contact()
        else:
            print("No contact with that name")
    else:
        break