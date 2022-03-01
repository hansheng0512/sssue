# Koo susan
# TP067306


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
        if (cont == 1):
            fileHandler = open('suppliers.txt', 'a+')
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
    spl = [supplier_code, supplier_name, supplier_address]
    return supplier_list


def save_supplier_reg_list():
    try:
        fileHandler = open('suppliers.txt', 'w')
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
        line = line.rstrip()
        print(line)
    fileHandler.close()


def save_item_detials():
    try:
        fileHandler = open('ppe.txt', 'w')
    except:
        print('File cannot be opened')
        exit()

    for line in fileHandler:
        fileHandler.write()
        fileHandler.write('\t')
        fileHandler.write('\n')
    fileHandler.close()


def hospital_registration():
    hospital_list = []
    for e in range(3):
        hptl = []
        hospital_code = input('\nPlease Enter Hospital code: ')
        hptl.append(hospital_code)
        hospital_address = input('\nPlease Enter address: ')
        hptl.append(hospital_address)
        hospital_list.append(hptl)
    while True:
        cont = int(input(" Want to add 4th Hospital details? [ 1- yes, 0= no]"))
        if (cont == 1):
            fileHandler = open('Distribution.txt', 'a+')
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
    fileHandler = open('Distribution.txt', 'w')
    hospital_list = hospital_registration()

    for hptl in hospital_list:
        for hp in hptl:
            fileHandler.write(hp)
            fileHandler.write('\t')
        fileHandler.write('\n')
    fileHandler.close()


def print_hospital_reg_list():
    fileHandler = open('Distribution.txt', 'r')

    for line in fileHandler:
        line = line.rstrip()
        print(line)
    fileHandler.close()


# check
def checkItemCodeIsAssigned(item_code):
    fileHandler = open('ppe.txt', 'r')
    for lines in fileHandler:
        lines = lines.rstrip()
        lines = lines.split(",")
        if (lines[0] == item_code):
            return True
    return False


def assign_Item_to_supplier():
    item_code = input('Pls Insert Your Item Code: ')

    itemAssignedToSupplier = checkItemCodeIsAssigned(item_code)

    if (itemAssignedToSupplier == True):
        print('This item is taken by another supplier')
    else:
        supplier_code = input('You want to assign this item to which supplier (Enter the supplier code): ')
        item_name = input('Pls Enter Item name: ')
        custom_quantity = int(
            input('Do you want to set 100 boxes(default quantity) as the item quantity? [1-yes, 0-No]'))
        if (custom_quantity == 1):
            item_quantity = 100
        else:
            item_quantity = int(input('Pls Enter Item Quantity in boxes: '))

        fileHandler = open('ppe.txt', 'a+')
        fileHandler.write(item_code + "," + item_name + "," + str(item_quantity) + "," + supplier_code)
        fileHandler.write('\n')
        fileHandler.close()

    while True:
        cont = int(input('Want to assign another item? [1-yes, 0-No and Exit]: '))
        if (cont == 1):
            assign_Item_to_supplier()
        else:
            break


# view stock which les than 25
# searching funtion
# receive item from supplier ()
# distribute item to hospital()

def menu():
    while True:
        print('Select the operation that you want to perform: ')
        print('1. Supplier registration')
        print('2. Hospital registration ')
        print('3. Print all details')
        print('4. Assign Item to supplier')
        print('5. coming soon')
        print('6. Exit')
        print()
        choice = int(input('Enter selection: '))

        if (choice == 1):
            save_supplier_reg_list()
        elif (choice == 2):
            save_hospital_reg_list()
        elif (choice == 3):
            print('hi')
        elif (choice == 4):
            assign_Item_to_supplier()
        elif (choice == 5):
            print('no items yet')
        elif (choice == 6):
            print('Have a nice day')
            break
        else:
            print('Invalid input')

        print()


menu()