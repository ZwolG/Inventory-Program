
#========The beginning of the class==========
class Shoe:
    # class constructor with requied attributes
    def __init__(self, country, code, product, cost, quantity):

        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)
    
    # getters to get all the attibutes from the class object
    def get_country(self):
        return self.country
    
    def get_code(self):
        return self.code

    def get_product(self):
        return self.product

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity
    
    # function to increase quantity
    def add_to_quantity(self, addition):
        self.quantity = self.quantity + addition
        return self.quantity
    
    # function to print out all details of the class object
    def __str__(self):
        return f'{self.country} {self.code} {self.product} {self.cost} {self.quantity}'


#=============Shoe list===========

# list to store shoe objects
shoe_list = []

#==========Functions outside the class==============

# function to read data from the inventory file
# to use this date to create Shoe class objects and store the in the shoe_list
def read_shoes_data():
    # opening the file
    with open('inventory.txt', 'r') as f:
        # variable to store the data from the file
        data = f.readlines()
        # for loop to iterate over the lines in data
        # [1:] to skip the first line
        for line in data[1:]:
            # variables to store product details, split function to split string into a list of 5 elements
            country, code, product, cost, quantity = line.split(',')
            # creating shoe object and adding it to the list
            shoe_list.append(Shoe(country, code, product, cost, quantity))

# function to add new shoe to the invetory by the user
# requesting all the details from the user
def capture_shoes():
    # user input
    country = input('Enter country of origin of the product: ')
    code = input('Enter product code: ')
    product = input('Enter name of the product: ')
    # loop to prevent worng input
    while True:
        try:
            cost = int(input('Enter cost of the product: '))
            break
        except:
            print('Only numbers allowed')

    while True:
        try:
            quantity = int(input('Enter quantity of the product: '))
            break
        except:
            print('Only numbers allowed')
    # new shoe object created using user input
    shoe_object = (Shoe(country, code, product, cost, quantity))
    # adding new shoe object to the shoe object list
    shoe_list.append(shoe_object)

# function to print out all shoes in the inventory
def view_all():
    # iterating through the shoe object list an printing them
    for shoe_object in shoe_list:
        print(shoe_object)

# function to find the object/objects with the lowest quantity
# and to increase the quantity when requested by the user
# update the shoe list with new quantity value
def re_stock():
    # list to store the objects with the lowest quantity
    low_quantity = []
    
    # left and right pointer
    left, right = 0, len(shoe_list) - 1
    
    # loop to compare values 
    # finding the lowest quantity
    while left < right:
        
        # if value at left index is smaller than a value at the right index 
        # program will decrese right index
        if shoe_list[left].get_quantity() <= shoe_list[right].get_quantity():
            low_quantity = []
            low_quantity.append((shoe_list[left], left))
            right -= 1
        
        # if value at left index is bigger than a value at the right index 
        # program will increase left index
        else:
            low_quantity = []
            low_quantity.append((shoe_list[right], right))
            left += 1
    
    # checking if here is more then one product with the lowest quantity
    for index, shoe in enumerate(shoe_list):
        # condition to compare quantities and to avoid adding duplicates
        if shoe.get_quantity() == low_quantity[0][0].get_quantity() and shoe.get_code() != low_quantity[0][0].get_code() :
            low_quantity.append((shoe, index))

    # pritnitg out the result
    for i, shoe in enumerate(low_quantity):
        print(i , shoe[0])

    # block of co to increase item quantity when requested
    # with try/except and if/elif statements to prevent from the wrong input
    # allows you to increase the quantity of the product selected by the user 
    # when there is more than one product with the lowest quantity
    user_choice = input('\nWould you like to add quantity (yes/no): ').lower()[0]
    if user_choice == 'y':
        valid_input = True
        while valid_input == True:
            if len(low_quantity) > 1:
                index = int(input('Select the product whose quantity you want to increase: '))
            else:
                index = 0
            if index < len(low_quantity):
                try:
                    add_quantity = int(input('How many units of the item would you like to add?: '))
                except:
                    print('Only number can be entered.')
                shoe_list[low_quantity[index][1]].add_to_quantity(add_quantity)
                print(shoe_list[low_quantity[index][1]])
                valid_input = False
            elif index > len(low_quantity):
                print('Wrong input.')
                print(f'Options bewtween 0 and {len(low_quantity) - 1} available')
    return ''

# function to search for a shoe from the list
# using the shoe code and return this object so that it will be printed
def search_shoe(id_code):
    for shoe in shoe_list:
        if shoe.get_code() == id_code:
            return shoe      
    return 'The given code was not found.'

# function to calculate the total value for each item
# using formula value = cost * quantity
# print information on the console for all the shoes
def value_per_item():
    for shoe in shoe_list:
        value = shoe.get_quantity() * shoe.get_cost()
        print(f'{shoe}: value {value}')
    return ''

# function to the product with the highest quantity and print out the result
def highest_qty():
    # list to store the objects with the highest quantity
    high_quantity = []

    # left and right pointer
    left, right = 0, len(shoe_list) - 1

    # loop to compare values 
    # finding the highest quantity
    while left < right:
        # if value at left index is bigger than a value at the right index 
        # program will decrease right index
        if shoe_list[left].get_quantity() >= shoe_list[right].get_quantity():
            high_quantity = []
            high_quantity.append(shoe_list[left])
            right -= 1

        # if value at right index is bigger than a value at the left index 
        # program will increase value left index
        else:
            high_quantity = []
            high_quantity.append(shoe_list[right])
            left += 1

    # checking if here is more then one product with the hihgest quantity
    for shoe in shoe_list:
        # condition to compare quantities and to avoid adding duplicates
        if shoe.get_quantity() == high_quantity[0].get_quantity() and shoe.get_code() != high_quantity[0].get_code() :
            high_quantity.append(shoe)

    # pritnitg out the result
    print('Shoes for sale: ')
    for shoe in  high_quantity:
        print(shoe)
    return ''

# function to write to the file all changes made by the user
def write_to_the_file(item_list, file):
    with open(file, 'w') as f:
        f.write('Country,Code,Product,Cost,Quantity\n')
        for shoe in item_list:
            shoe_details = ','.join([shoe.get_country(), shoe.get_code(), shoe.get_product(), str(shoe.get_cost()), str(shoe.get_quantity())])
            f.write((shoe_details)+'\n')

read_shoes_data()

#==========Main Menu=============
# variable to terminate the loop
# loop to run program
run_program = True
while run_program == True:
    print(
    '''
    ================= Shoe Inventory ==================
    Search products by code                         (1)
    Determine the product with the lowest 
    quantity and restock it                         (2)
    Determine the product with the highest quantity (3)
    Calculate the value of each stock item          (4)
    Show all invetory                               (5)
    Add item to the inventory                       (6)
    Quit                                            (0)
    ===== Choose one of the options listed above ====== 
    ''')

    # writing to the file any changes made by the user
    write_to_the_file(shoe_list, 'inventory.txt')

    # block of code responsible for performing all the operations requesed by the user
    # secured by the try/except from wrong input
    try:
        user_choice = int(input('Choosse your option: '))

        # code to search products by it's code
        if user_choice == 1:
            id_code= input('Please enter the product code: ')
            print(search_shoe(id_code))

        # code to determine the lowest quantity and restock
        elif user_choice == 2:
            print(45 * '-', '\n')
            print('Product/products with the lowest quantity: \n')
            re_stock()
            print(45 * '-')

        # code to determine the highest quantity
        elif user_choice == 3:
            print(45 * '-', '\n')
            print('Product/products with the highest quantity:')
            highest_qty()
            print('\n',45 * '-')

        # code to calculate value of each stock item
        elif user_choice == 4:
            value_per_item()

        # code to show all inventory
        elif user_choice == 5:
            view_all()
            print(f'\nThere is/are {len(shoe_list)} item/items in the inventory.')

        # code to add items to the inventory
        elif user_choice == 6:
            print('\nTo add new item/items to the invertory follow the instructions.\n')
            capture_shoes()
            print('New inventory entry successfully added')

       # program termination
        elif user_choice == 0:
            print('Goodbye')
            run_program = False

    # message about wrong input
    except:
        print('Wrong input')
        print('Please select valid option.')    
