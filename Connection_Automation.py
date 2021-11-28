import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.keys import Keys
from os import environ


############################################# User Input Start ####################################################################################################
                                                                                                                                                                ###
getting_the_list_of_pepole = input("Type 3-5 names of pepole by the following rules: \n"                                                                        ###
                                   "[1]  Full and correct name of the person \n"                                                                                ###
                                   "[2]  You must be connected to the person \n"                                                                                ###
                                   "[3]  The 3 names must be seperated by a comma. Example - Ariel Silver, John Terry, Kevin Hart \n"                           ###
                                   "[*]  These pepole should have as many connections as possible \n"                                                           ###
                                   "###  Insert here  ###:  ")                                                                                                  ###
                                                                                                                                                                ###
getting_the_word_list = input("\n \n \n"                                                                                                                        ###
    "Type as many key words as you want. These key words will be searched in pepole's description and if found will attempt to Connect with the person. \n"     ###
    "Important rules: \n"                                                                                                                                       ###
    "[1] The words must be seperated by a comma. Example  -  Cyber, Security, Malware, Pentest, OSCP \n"                                                        ###
    "[*] The search is case-insensitive \n"                                                                                                                     ###
    "###  Insert here  ###:  ")                                                                                                                                 ###
                                                                                                                                                                ###
                                                                                                                                                                ###
username = input("\n Type your linkedin username, its your email address: ")                                                                                    ###
password = input("\n Type your linkdin password: ")                                                                                                             ###
                                                                                                                                                                ###
############################################# User Input End ######################################################################################################

pepole_list_beta = []
key_words_list = []

#linkedin Login page URL
linkedin_home_page = "https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin"

# getting the string of names and converting it to a clean list of names
for name in getting_the_list_of_pepole.split(","):
    pepole_list_beta.append(name.strip())
pepole_list = iter(pepole_list_beta)


# getting the string of keywords and converting it to a clean list of names
for word in getting_the_word_list.split(","):
    key_words_list.append(word.strip().lower())


class Linkedin():
    def __init__(self, Chrome_driver_path=r';C:\SeleniumDrivers'):
        self.Chrome_driver_path = Chrome_driver_path
        #Adding the Chrome driver to PATH
        environ['PATH'] += self.Chrome_driver_path
        self.driver = webdriver.Chrome()



    #Opening linkedin login page
    def get_home_page(self):
        self.driver.get(linkedin_home_page)
        self.driver.implicitly_wait(8)
        self.driver.maximize_window()

        self.login()#Next step




    #Loging into the user account
    def login(self):
        time.sleep(2)
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.ID, 'username')
                )
            )
        except Exception as e:
            print("[1.1] cant find login page : ", e)

        #Typing the username
        try:
            enter_username = self.driver.find_element_by_id('username')
            enter_username.clear()
            enter_username.send_keys(username.strip())
        except Exception as e:
            print("[1.2] can't write in username \n", e)

        #Typing the password
        try:
            enter_username = self.driver.find_element_by_id('password')
            enter_username.send_keys(password.strip())
        except Exception as e:
            print("[1.3] can't write in password \n", e)

        #Submiting the user credentials
        try:
            enter_username = self.driver.find_element_by_css_selector('button[data-litms-control-urn="login-submit"]')
            enter_username.click()
        except Exception as e:
            print("[1.4] can't press on submit \n", e)

        #This part probably won't be used and will output an informal error
        try:
            WebDriverWait(self.driver, 2).until(
                expected_conditions.presence_of_element_located(
                    (By.CLASS_NAME, 'secondary-action')
                )
            )
            enter_username = self.driver.find_element_by_class_name("secondary-action")
            enter_username.click()
        except Exception as e:
            print("[1.5] can't find or press skip \n", e)

        self.home_screen() #Next step



    # When we are done with the connections of a person, we need to go back to the home page before searching for the next person and doing all from the beginning
    def home_screen(self):
        person_to_use = next(pepole_list)
        self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight * -1)")  # scrolls to the top of the page

        # Search for the Blue linkedin icon.
        try:
            WebDriverWait(self.driver, 4).until(
                expected_conditions.presence_of_element_located(
                    (By.CLASS_NAME, "global-nav__branding")
                )
            )
        except Exception as e:
            print("[9.1] cant find the main blue 'ln' button \n", e)
        try:
            home_button = self.driver.find_element_by_class_name(
                "global-nav__branding").click()  # Click on the Blue linkedin icon.
        except Exception as e:
            print("[9.2] cant press the main blue 'ln' button \n", e)

        # Verifying we are back to the homepage, by searching for the toolbar.
        try:
            WebDriverWait(self.driver, 4).until(
                expected_conditions.presence_of_element_located(
                    (By.CLASS_NAME, "share-box-feed-entry__closed-share-box")
                )
            )
        except Exception as e:
            print("[9.3] cant validate it's the home page \n", e)

        self.find_person(person_to_use)



    # Function for searching pepole that the user specified
    def find_person(self, person_entered):
        self.driver.implicitly_wait(3)

        #Trying to find the search text box. If not found the user probably entered wrong credentials. Exeting if couldn't find
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.CLASS_NAME, 'search-global-typeahead__input')
                )
            )
        except Exception as e:
            print("[2.1] Probably Wrong credentials \n", e)
            self.driver.quit()
            exit()

        #Searching a person from the user input list. This may take few seconds !!!
        try:
            search_for = self.driver.find_element_by_class_name("search-global-typeahead__input")
            search_for.send_keys(person_entered)
            search_for.send_keys(Keys.ENTER)
        except Exception as e:
            print("[2.2] can't click search button \n", e)
        self.driver.implicitly_wait(8)

        self.enter_his_connection(person_entered)






    #Entering the person page and then connections
    def enter_his_connection(self, person_entered):
        #Trying to find the person after searching his name.
        try:
            WebDriverWait(self.driver, 8).until(
                expected_conditions.presence_of_element_located(
                    (By.CLASS_NAME, "search-nec__hero-kcard-v2")
                )
            )
        except Exception as e:
            print("[3.1] can't find box that holds person name' \n", e)

        #Trying to click on the name of the person we searched, so we can see his full page
        try:
            box_holding_profile_name_big = self.driver.find_element_by_class_name("search-nec__hero-kcard-v2")
        except:
            try:
                box_holding_profile_name_big = self.driver.find_element_by_class_name("search-nec__hero-kcard")
            except:
                pass
        try:
            box_holding_profile_name_medium = box_holding_profile_name_big.find_element_by_class_name("entity-result__title-line")
            box_holding_profile_name_small = box_holding_profile_name_medium.find_element_by_class_name('app-aware-link')
            box_holding_profile_name_small.click()
        except Exception as e:
            print("[3.2] can't click on 'view full profile' \n", e)
            self.home_screen()

        # Verify we are in the specified user profile page
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.presence_of_element_located(
                    (By.CLASS_NAME, "pb5")
                )
            )
            box_that_holds_number_of_connections_button = self.driver.find_element_by_class_name("pb5")
        except:
            try:
                WebDriverWait(self.driver, 2).until(
                    expected_conditions.presence_of_element_located(
                        (By.CLASS_NAME, "ph5")
                    )
                )
                box_that_holds_number_of_connections_button = self.driver.find_element_by_class_name("ph5")
            except Exception as e:
                print("[3.3] maybe cant find the box that holds the number of connections button \n", e)

        #Finding the 'connections' button on the user profile, by using the "sub-element" techniqe twice
        try:
            line_that_holds_number_of_connections_button = box_that_holds_number_of_connections_button.find_element_by_class_name("pv-top-card--list")
            connections_button = line_that_holds_number_of_connections_button.find_element_by_class_name("link-without-visited-state")
            connections_button.click()
        except Exception as e:
            print("[3.4] cant click connections button \n", e)
            self.home_screen()


        number_of_pages = self.number_of_connection_pages()
        #Main loop
        for j in range(number_of_pages):
            print("page {} in the connections of {}".format(j, person_entered))
            self.find_correct_pepole()
        self.home_screen()




    #We need to know when we are in the last connections page of the person, so we can go to the next person the user indicated.
    # Verifying we see the full connection page before we proceed
    def number_of_connection_pages(self):
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.presence_of_element_located(
                    (By.CLASS_NAME, "search-marvel-srp")
                )
            )
        except Exception as e:
            print("[4.1] cant find main connections page \n", e)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # going to the bottom of the page

        #See the bar that holds connection pages number
        try:
            WebDriverWait(self.driver, 8).until(
                expected_conditions.presence_of_element_located(
                    (By.CLASS_NAME, "artdeco-pagination--has-controls")
                )
            )
        except Exception as e:
            print("[4.2] can't find 'Bar that holds connection pages' \n", e)

        #There are 10 elements that represents connection pages. Here we get all of them into a list with find elements, then we return the last one in the list. It will always represent the connection pages amount
        try:
            bottom_Section = self.driver.find_element_by_class_name("artdeco-pagination--has-controls")
            ten_page_numbers = bottom_Section.find_elements_by_class_name("artdeco-pagination__indicator--number")
        except Exception as e:
            print("[4.3] can't get the 10 page numbers \n", e)
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight * -1)")
        return int(ten_page_numbers[-1].text)



    # Finding correct pepole to connect with, by looking for the specified key words, in the person description.
    def find_correct_pepole(self):
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.presence_of_element_located(
                    (By.CLASS_NAME, "search-marvel-srp")
                )
            )
        except Exception as e:
            print("[5.1] cant find main connections page \n", e)

        #Each connection page contains 10 pepole. We get all of the profiles into a list and then iterate through the list.
        try:
            full_page_Biggest = self.driver.find_element_by_class_name("search-marvel-srp")
            full_page_Medium = full_page_Biggest.find_element_by_class_name("pv2")
            full_page_Small = full_page_Medium.find_element_by_class_name("reusable-search__entity-result-list")
            pepole_full_box = full_page_Small.find_elements_by_class_name("reusable-search__result-container")
        except Exception as e:
            print("[5.2] cant get the 10 pepole boxes on the current page \n", e)
            self.home_screen()
        for i in pepole_full_box:
            print(pepole_full_box.index(i))
            if pepole_full_box.index(i) == 4 or pepole_full_box.index(i) == 7 :  #In Selenium we usually can't click what we cant see, so after it iterates through 6 pepole, the page goes down 600 pixels
                self.driver.execute_script("window.scrollTo(0, 360)")

            # Gets the description of the person and checks for a match to any keyword the user specified
            try:
                person_description = i.find_element_by_class_name("entity-result__primary-subtitle").text
                if len(person_description) > 3:
                    for key_word in key_words_list:
                        if key_word in person_description.lower():
                            self.connect(i)
            except Exception as e:
                print("[5.3] :  ", e)


        #When finished iterating through the 10 pepole, going to the next page.
        self.next_page()



    def connect(self, person):
        self.driver.implicitly_wait(2)
        try:
            person_box_right_side = person.find_element_by_class_name("entity-result__actions")
            connect_button = person_box_right_side.find_element_by_class_name("artdeco-button__text").text
        except Exception as e:
            print("[6.1] cant find the connect button \n", e)
        try:
            if connect_button == "Connect":
                person_box_right_side.find_element_by_class_name("artdeco-button__text").click()
        except Exception as e:
            print("[6.2] cant press on the connect button \n", e)
        try:
            self.check_pop_up_after_connect()
        except Exception as e:
            print("[6.3] cant check_pop_up_after_connect() \n", e)
        self.driver.implicitly_wait(8)



    # After each connection one of 3 pop-ups occur.
    def check_pop_up_after_connect(self):
        self.driver.implicitly_wait(1)
        # finds and stores the pop-up windows after the Connect
        try:
            WebDriverWait(self.driver, 5).until(
                expected_conditions.presence_of_element_located(
                    (By.CLASS_NAME, "artdeco-modal--layer-default")
                )
            )
            pop_up = self.driver.find_element_by_class_name("artdeco-modal--layer-default")
            self.driver.implicitly_wait(2)
        except Exception as e:
            print("[7.1] cant locate the pop-up window.   \n", e)
            return None

        # Check if we reached the weekly connection limit, by searching for a phrase in the pop-up text. If yes - close window and exit script
        try:
            try:
                pop_up_text = pop_up.find_element_by_class_name("ph4").text
                if 'You’ve reached' in pop_up_text:
                    print("++++++++++++++++++++++++++++"
                          "++++++++    DONE   +++++++++"
                          "++++++++++++++++++++++++++++")
                    self.driver.quit()
                    exit()

            except:
                pop_up_lower_part = pop_up.find_element_by_class_name("artdeco-modal__actionbar")
                pop_up_lower_part.find_element_by_class_name("artdeco-button--primary").click()
                print("+++++++++++++   CONNECT    ++++++++++++")
                time.sleep(1)  # It waits after each connect, so their wont be suspicious speed of connections

        # When it can't press the blue button of the pop-up
        except Exception as e:
            print("[7.2] Selenium couldn't find blue button\n:  ", e)
            self.home_screen()



    # Tries to find and press the 'next page button'
    def next_page(self):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")  # scrolls to the end of the page
        try: # tries to find the element
            WebDriverWait(self.driver, 4).until(
                expected_conditions.presence_of_element_located(
                    (By.CLASS_NAME, "artdeco-pagination__button--next")
                )
            )
            next = self.driver.find_element_by_class_name("artdeco-pagination__button--next")  # stores the element
        except Exception as e:
            print("[8.1] can't find next page button \n", e)
        try:
            next.click()
        except Exception as e:
            print("[8.2] can't press next page button \n", e)
            self.home_screen()




kk = Linkedin()
kk.get_home_page()




