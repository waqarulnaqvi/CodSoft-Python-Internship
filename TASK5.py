class Contact:
    def __init__(self):
        self.name=""
        self.phn_number=0
        self.email=""
        self.address=""

    def input_ignore_case(self):
        return input("Enter Contact name:").capitalize()
    def filesavewritemode(self, myobject):
        with open("pt_81_contactbook", "w") as f:
            for i in myobject:
                f.writelines(f"name: {i[0]}\nphone number: {i[1]}\nemail: {i[2]}\naddress: {i[3]}\n\n")

    def filesaveappendmode(self, myobject):
        with open("pt_81_contactbook", "a") as f:
            for i in myobject:
                f.writelines(f"name: {i[0]}\nphone number: {i[1]}\nemail: {i[2]}\naddress: {i[3]}\n\n")
    def insert(self):
        self.name=self.input_ignore_case()
        self.phn_number=int(input("Enter phone number:"))
        self.email=input("Enter email:")
        self.address=input("Enter address:")
        print()
        return self.name,self.phn_number,self.email,self.address

    def Add_Contact(self):
        my_objects=[]
        i=0
        for i in range(int(input("How many contact you want to save:"))):
            my_objects.append(self.insert())
        print(f"{i+1} contact added successfully!\n")
        self.filesaveappendmode(my_objects)
        return my_objects

    def search_Contact(self,my_object):
        name=self.input_ignore_case()
        for i in my_object:
           if i[0] in name :
               print(f"Contact details:\nname: {i[0]}\nphone number: {i[1]}\nemail: {i[2]}\naddress: {i[3]}\n")
               break
        else:
            print("Contact does not exist\n")


    def view_all_contact(self,my_object):
        print('Contact details:')
        for i in my_object:
                print(f"name: {i[0]}\nphone number: {i[1]}\nemail: {i[2]}\naddress: {i[3]}\n")

    def delete_contact(self,my_object):
        j=0
        name=self.input_ignore_case()
        for i in my_object:
           if i[0] in name :
               print(f"Contact details:\nname: {i[0]}\nphone number: {i[1]}\nemail: {i[2]}\naddress: {i[3]}\nContact has been successfully deleted\n")
               del(my_object[j])
               self.filesavewritemode(my_object)
               break
           j=j+1
        else:
            print("Contact does not exist\n")

    def delete_all_contacts(self):
        print("All contacts has been deleted\n")
        self.filesavewritemode("")
        return list()

    def update_contact(self,my_object):
        name=self.input_ignore_case()
        j=0
        for i in my_object:
            if name in i[0]:
                print("Contact found!!\n\nEnter updated details:")
                my_object[j]=list(i)
                my_object[j][0],my_object[j][1],my_object[j][2],my_object[j][3]=self.insert()
                print("Contact details updated successfully!!\n")
                my_object[j]=tuple(my_object[j])
                self.filesavewritemode(my_object)
                return
            j=j+1
        print("name does not exist\n")



my_objects=[("Ram","1212","@gmail.com","lko"),("Shyaam","12","@gmail.com","delhi")]
contact=Contact()
contact.filesavewritemode(my_objects)
while True:
    user_choice=int(input("Enter\n1 for Add Contact\n2 for View Contact\n3 for Search Contact\n4 for Update existing contact\n5 for Delete contact\n6 for delete all contacts\nEnter any other key to exit:\n"))
    match user_choice:
        case 1:
            obj=contact.Add_Contact()
            for i in obj:
                my_objects.append(i)
        case 2:
             contact.view_all_contact(my_objects)
        case 3:
             contact.search_Contact(my_objects)
        case 4:
            contact.update_contact(my_objects)
        case 5:
            contact.delete_contact(my_objects)
        case 6:
            contact.delete_all_contacts()
        case _:
            break
