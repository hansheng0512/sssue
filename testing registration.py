#Koo susan
#TP067306

def supplier_registration():
    supplier_list = []
    for i in range(3):
        spl = []
        supplier_code = input('\nPlease Enter Supplier Code: ')
        spl.append(supplier_code)
        supplier_name = input('\nPlease Enter Your Name: ')
        spl.append(supplier_name)
        supplier_address = input('\nPlease Enter Your Address including STATE Name: ')
        spl.append(supplier_address)
        supplier_list.append(spl)
    while True:
        cont = int(input(" Want to add 4th supplier details? [ 1- yes, 0= no]"))
        if(cont == 1):
            fileHandler = open ('suppliers.txt','a+')
            print('Enter 4th supplier detials')
            spl4 = []
            supplier_code = input('\nPlease Enter Supplier Code: ')
            spl4.append(supplier_code)
            supplier_name = input('\nPlease Enter Your Name: ')
            spl4.append(supplier_name)
            supplier_address = input('\nPlease Enter Your Address including STATE Name: ')
            print()
            print('Maximum 4 hospitals can be registered')
            print()
            spl4.append(supplier_address)
            supplier_list.append(spl4)
        else:
            (cont == 0)
            break
    spl = [supplier_code, supplier_name,supplier_address]
    return supplier_list    

def save_supplier_reg_list():
    try:
        fileHandler = open('suppliers.txt','w')
    except:
        print('File cannot be opened: ')
        exit()
    supplier_list = supplier_registration()

    for spl in supplier_list:
        for sl in spl:
            fileHandler.write(sl)
            fileHandler.write('\t')
        fileHandler.write('\n')
    fileHandler.close()

def print_supplier_reg_list():
    try:
        fileHandler = open('suppliers.txt', 'r')
    except:
        print('File cannot be opened')
        exit()

    for line in fileHandler:
        line=line.rstrip()
        print(line)
    fileHandler.close()

def hospital_registration():
    hospital_list = []
    for e in range (3):
        hptl = []
        hospital_code = input('\nPlease Enter Hospital code: ')
        hptl.append(hospital_code)
        hospital_address = input('\nPlease Enter address: ')
        hptl.append(hospital_address)
        hospital_list.append(hptl)
    while True:
        cont = int(input(" Want to add 4th Hospital details? [ 1- yes, 0= no]"))
        if(cont == 1):
            fileHandler = open ('Distribution.txt','a+')
            print('Enter 4th supplier detials')
            hptl4 = []
            hospital_code = input('\nPlease Enter Hospital Code: ')
            hptl4.append(hospital_code)
            hospital_address = input('\nPlease Enter Hospital Address including STATE Name: ')
            print()
            print('Maximum 4 Hospitals can be registered')
            print()
            hptl4.append(hospital_address)
            hospital_list.append(hptl4)
        else:
            (cont == 0)
            break
            
    return hospital_list

def save_hospital_reg_list():
    fileHandler = open ('Distribution.txt','w')
    hospital_list = hospital_registration()

    for hptl in hospital_list:
        for hp in hptl:
            fileHandler.write(hp)
            fileHandler.write('\t')
        fileHandler.write('\n')
    fileHandler.close()

def print_hospital_reg_list():
    fileHandler = open('Distribution.txt','r')

    for line in fileHandler:
        line = line.rstrip()
        print(line)
    fileHandler.close()

def printItemDetails():
    counter = 0
    fileHandler = open('ppe.txt', 'r')
    content = fileHandler.readlines()
    content.sort()
    while (counter <= 5):
        print(content[counter])
        counter = counter + 1


def saveItemDetails(lItemDetails):
    fileHandler = open('ppe.txt','w')
    for details in lItemDetails:
        for i in details:
            fileHandler.write(str(i))
            fileHandler.write('\t')
        fileHandler.write('\n')
    fileHandler.close()

def ppeFile():
    itemDetails = []
    HcD = ['HC', 'Head_Cover',100]
    FsD = ['FS', 'Face_Shield',100]
    MsD = ['MS', 'Mask',100]
    GlD = ['GL', 'Glove',100]
    GwD = ['GW', 'Gown',100]
    ScD = ['SC', 'Shoe_Cover',100]
    itemDetails.append(HcD)
    itemDetails.append(FsD)
    itemDetails.append(MsD)
    itemDetails.append(GlD)
    itemDetails.append(GwD)
    itemDetails.append(ScD)
    return itemDetails
    
def assignItem_to_supplier():
        
    while True:
        askIC = input('Pls enter the item code that u want to assign to the particular supplier: ')
        askIC = askIC.upper()
        if (askIC == 'HC') or (askIC == 'FS') or (askIC == 'MS') or (askIC == 'GL') or (askIC == 'GW') or (askIC == 'SC'):
            print ('Valid item code')
            getSPC = input('Pls enter the supplier code u want to assign to: ')
        

def checkItemCodeIsAssigned(supplier_code, item_code):
    fileHandler = open("ppe.txt", "r")
    for lines in fileHandler:
        lines = lines.rstrip()
        lines = lines.split(",")
        if (lines[0] == item_code and lines[3] == supplier_code):
            return "found"
    return "not found"



# Assign Item to Supplier
def assignItemToSupplier():
    supplier_code = input("You want to assign this item to which supplier? ")
    item_code = input("Insert Item Code")

    # Check if item code assigned to any supplier
    itemAssignedToSupplier = checkItemCodeIsAssigned(supplier_code, item_code)
    if (itemAssignedToSupplier == "found"):
        print("This code is taken by another supplier")
    else:
        item_name = input("Insert Item Name")
        custom_quantity = int(input("Do you want to init with 100 quantity? [1 - yes 0 - no]"))
        if (custom_quantity == 1):
            item_quantity = input("Insert Item Quantity")
        else:
            item_quantity = 100

        # Write data into file
          # open file as "a" -> append
        # ask to continue







    
#add item for supplier
#view stock which les than 25
#searching funtion
#receive item from supplier ()
#distribute item to hospital()
    
def menu():
    itemDetails = ppeFile()
    saveItemDetails(itemDetails)
    while True:
        print('Select the operation that you want to perform: ')
        print('1. Supplier registration')
        print('2. Hospital registration ')
        print('3. Print all the details')
        print('4. Search for any particular items (supplier code)')
        print('5. Check')
        print('6. Exit')
        print()
        choice= int(input('Enter selection: '))
        
        if(choice == 1):
            save_supplier_reg_list()
        elif(choice == 2):
            save_hospital_reg_list()
        elif(choice == 3):
            print('hi')
        elif(choice == 4):
            print('hi')
        elif(choice == 5):
            print('no items yet')
        elif(choice == 6):
            print('Have a nice day')
            break
        else:
            print('Invalid input')

        print()

menu()
        
