# app.py - The main executable file
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
from Test_Locators import locators
from Test_Data import data
import pytest

# Orange Hrm
class Test_Hrm:
   
    # Generator function
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
       
        
      
# Code for Test case ID: Tc_LOGIN_01

    def test_validlogin(self,booting_function):
        self.driver.maximize_window()
        self.driver.get(data.Hrm_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()    
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS :The User is Logged in successfully Login_name{a} and Password {b}". format(a=data.Hrm_Data.username, b=data.Hrm_Data.password))

       
        
# Code for Test case ID: Tc_LOGIN_02

    def test_invalidlogin(self,booting_function):
        self.driver.maximize_window()
        self.driver.get(data.Hrm_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().pass_word)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()    
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS : Invalid credentials login_name {a} and Password {b}". format(a=data.Hrm_Data.username, b=data.Hrm_Data.pass_word))

        
# Code for Test case ID: Tc_PIM_01
        
    def test_entry_employee(self,booting_function):
        self.driver.maximize_window()
        self.driver.get(data.Hrm_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pimbutton).click()     
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().add_employee).click() 
        sleep(2)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().employee_fullname).send_keys(data.Hrm_Data().name)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().employee_lastname).send_keys(data.Hrm_Data().lastname)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().save_button1).click() 
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS : Add new Employee Employee_name {a} and lastname {b}". format(a=data.Hrm_Data.name, b=data.Hrm_Data.lastname))


# Code for Test case ID: Tc_PIM_02

    def test_edit_employee(self,booting_function):
        self.driver.maximize_window()
        self.driver.get(data.Hrm_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pimbutton).click() 
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().employee_name).send_keys(data.Hrm_Data().employee_name)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_button).click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().click_button).click() 
        sleep(2)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().midname_box).send_keys(data.Hrm_Data().midname)  
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().saveicon).click()
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS : Edit in with employeename midname {a}". format(a=data.Hrm_Data.midname))


                
# Code for Test case ID: Tc_PIM_03

    def test_delete(self,booting_function):
        self.driver.maximize_window()
        self.driver.get(data.Hrm_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().username_inputBox).send_keys(data.Hrm_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Hrm_Locators().password_inputBox).send_keys(data.Hrm_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().LoginButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().pimbutton).click()    
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().employee_name).send_keys(data.Hrm_Data().employee_name)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().search_button).click()    
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().delete_button).click() 
        self.driver.find_element(by=By.XPATH, value=locators.Hrm_Locators().yes_button).click() 
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS: Employee information successfully delete")




   

