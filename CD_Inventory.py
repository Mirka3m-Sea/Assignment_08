#------------------------------------------#
# Title: Assignmen08.py
# Desc: Assignnment 08 - Working with classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, created file
# DBiesinger, 2030-Jan-01, added pseudocode to complete assignment 08
# Miroslava M., 2022-Mar-19. added code for class CD, FileIO
#Miroslava, 2022-Mar-20 fixed all the errors encoutered in the script
#------------------------------------------#

# -- DATA -- #
strFileName = 'cdInventory.txt'
lstOfCDObjects = []



class CD:
    """Stores data about a CD:

    properties:
        cd_id: (int) with CD ID
        cd_title: (string) with the title of the CD
        cd_artist: (string) with the artist of the CD
    methods:
        
    (1) For class CD, added the constructor with instance attributes : cd_id, cd_tittle, and cd_artist
    (2) Define properties
    """
    #--- Fields ---#
    """
    Assignment 08
        Adding the fields for the class CD
        the three data depositories needed are:
            Parameters:
            ID: (Int) variable, this is the identifying number for each entry.
            title: (str) variable. CD album name.
            artist: (str) variable, artist name.
    """
    
    # TO DONE Add Code to the CD class
    #----- Constructor -----#
    
    """
    Constructor to define the  attributes for the Object CD.
    #def __init__(self, cd_id, cd_title, cd_artist):
    """
    def __init__(self, strID, title, artist):
        self.__id= strID
        self.__title = title
        self.__artist = artist

    #---Properties ----#
    """"These properties will be used later as attributes. The returns
    of each function match the values defined in the __init__ function.
    """
    @property
    def cd_id(self):
        #will handle input errors in I/O
        """"
        Parameters:
                __cd_id: (object attribute)
        Returns: self.__id
        """
        return self.__id
    @property
    def cd_title(self):
        """"
        Parameters:
                cd_title: (object attribute)
        Returns: self.__title
        """
        return self.__title
    @property
    def cd_artist(self):
        """"
        Parameters:
                __cd_artist : (object attribute)
        Returns: self.__artist
        """
        return self.__artist
        

        
# -- PROCESSING -- #
class FileIO:
    """Processes data to and from file:

    properties:

    methods:
        save_inventory(file_name, lst_Inventory): -> None
        load_inventory(file_name): -> (a list of CD objects)

    """
    #----------Fields ----------#
    """
    Assignment 08
        Added the fields to store data within this class.
        lstOfCDObjects: (list of objects)
        lst_Inventory:  (list)
    """

    
    # TO DONE Add code to process data from a file
#----------Reading the file into a table of objects -------------}

    @staticmethod
    """staticmethod function, this is not an object 
    
        arguments: 
            file_name (str): file name that will be opened
            lst_Inventory (list): this will be a list of objects
            objFile (obj): object created to open and close a file
            lstValues (list): temporary list values to be save into a external file
        return:
            None
    """
    def save_inventory(file_name, lst_Inventory):
        objFile= open(file_name, 'w')
        for row in lst_Inventory:
            lstValues =[]
            lstValues.extend([row.cd_id, row.cd_title, row.cd_artist])
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()
        

    @staticmethod
    """staticmethod function, this is not an object 
    
        arguments: 
            file_name (str): file name that will be opened
            lstOfCDObjects (list): this a list of objects stored in temporary memory
            objFile (obj): object created to open and close a file
            data (list): list values read from a file to be loaded into a temporary table (lstOfCDObjects)
            dicRow (CD object): object with the attributes of function CD.
        return:
            None
    """
    def load_inventory(file_name):
        lstOfCDObjects.clear()
        objFile= open(file_name, 'r')
        for line in objFile:
            data = line.strip().split(',')
            dicRow = CD(data[0], data[1], data[2])
            lstOfCDObjects.append(dicRow) # I had the wrong brackets and did not load.
        objFile.close()

#        
    #------------- writing ------------------#
    #TO DONE find the way to call the previous definitions.


# -- PRESENTATION (Input/Output) -- #
class IO:
    # TO DONE add docstring
    """Handling Input / Output"""
    
    # TO DONE add code to show menu to user
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user
            Args: None.
            Returns: None.
        """
        print('Menu\n\n[l] Load Inventory from file\n[a] Add CD entry\n[d] Display Current Inventory')
        print('[s] Save Inventory to file\n[x] Exit\n')


    # TO DONE add code to captures user's choice
    @staticmethod
    def menu_choice():
        """Gets user input for menu selection
        Args:  None.
        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x
    
        """
        choice = ' '
        while choice not in ['l', 'a', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    # TO DONE add code to display the current data on screen
    @staticmethod
    def show_inventory(lstOfCDObjects):
        """Displays current inventory table
        Args:lstOfCDObjects (list of objects) holds the data temporarily while the script is running.
        Returns:  None.
        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in lstOfCDObjects:
            print('{}\t{} (by:{})'.format(row.cd_id,row.cd_artist, row.cd_title))
        print('======================================')
    
    # TO DONE add code to get CD data from user
    def data_input() :
        """
        This function request the user to input data for each CD.
        Arg: 
            ID, intID, title, artist. All of these entries are held
            in the internal memory of this function. They are no global variables.
            
        Returns: new_entry (CD object), entry for CD witht attributes (ID, tittle, artist)
        """
        while True:
            strID = input('Enter ID: ').strip()
            try:
                intID = int(strID)
                break
            except ValueError:
                print('Invalid ID entry\t')
        title = input('What is the CD\'s title? ').strip()
        artist = input('What is the Artist\'s name? ').strip()
        new_entry= CD(strID, title, artist)
        return new_entry

# -- Main Body of Script -- #
# TO DOING Add Code to the main body
#    print('There isn\'t a file yet, please choose [a] or [s] first\n')
file_name2=open('cdInventory.txt', 'a') #@Laura: I fixed this as you recommended, thanks!.
file_name2.close()
# Display menu to user
while True:
    IO.print_menu()
    strChoice = IO.menu_choice()
    
    # Start assessing choices.
    #first choice is to exit.
    if strChoice == 'x':
       break

    # show user current inventory
    elif strChoice == 'd':
        IO.show_inventory(lstOfCDObjects)
        continue
    
    # let user add data to the inventory
    elif strChoice == 'a':
        data1= IO.data_input() #data1 is a temporary variable, only used for appending the table
        lstOfCDObjects.append(data1)
        IO.show_inventory(lstOfCDObjects)
        continue # start loop back at top.
    
    # let user save inventory to file
    elif strChoice == 's':
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileIO.save_inventory(strFileName, lstOfCDObjects)
        else:
             input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
        
    # let user load inventory from file
    elif strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled\t')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileIO.load_inventory(strFileName)
            IO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstOfCDObjects)
    else:
        print('\nThat is not a valid option, please select from the menu\n')
        continue


