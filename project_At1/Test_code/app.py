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

class Test_Hrm1:
   
    # Generator function
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
       
        
# Code for Test case ID: Tc_LOGIN_02

    def test_invalidlogin(self,booting_function):
        self.driver.maximize_window()
        self.driver.get(data.Hrm1_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Hrm1_Locators().username_inputBox).send_keys(data.Hrm1_Data().user_name)
        self.driver.find_element(by=By.NAME, value=locators.Hrm1_Locators().password_inputBox).send_keys(data.Hrm1_Data().pass_word)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm1_Locators().LoginButton).click()    
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS : Invalid credentials login_name {a} and Password {b}". format(a=data.Hrm1_Data.user_name, b=data.Hrm1_Data.pass_word))


class Test_Hrm2:
   
    # Generator function
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        
        
# Code for Test case ID: Tc_PIM_01
        
    def test_entry_employee(self,booting_function):
        self.driver.maximize_window()
        self.driver.get(data.Hrm2_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Hrm2_Locators().username_inputBox).send_keys(data.Hrm2_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Hrm2_Locators().password_inputBox).send_keys(data.Hrm2_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm2_Locators().LoginButton).click()
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm2_Locators().pimbutton).click()     
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm2_Locators().add_employee).click() 
        sleep(2)
        self.driver.find_element(by=By.NAME, value=locators.Hrm2_Locators().employee_fullname).send_keys(data.Hrm2_Data().name)
        self.driver.find_element(by=By.NAME, value=locators.Hrm2_Locators().employee_lastname).send_keys(data.Hrm2_Data().lastname)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm2_Locators().save_button1).click() 
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS : Add new Employee Employee_name {a} and lastname {b}". format(a=data.Hrm2_Data.name, b=data.Hrm2_Data.lastname))

class Test_Hrm3:
   
    # Generator function
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        
                
# Code for Test case ID: Tc_PIM_02

    def test_edit_employee(self,booting_function):
        self.driver.maximize_window()
        self.driver.get(data.Hrm3_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Hrm3_Locators().username_inputBox).send_keys(data.Hrm3_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Hrm3_Locators().password_inputBox).send_keys(data.Hrm3_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm3_Locators().LoginButton).click()
        sleep(3)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm3_Locators().pimbutton).click() 
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm3_Locators().employee_name).send_keys(data.Hrm3_Data().employee_name)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm3_Locators().search_button).click()
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm3_Locators().click_button).click() 
        sleep(2)
        self.driver.find_element(by=By.NAME, value=locators.Hrm3_Locators().midname_box).send_keys(data.Hrm3_Data().midname)  
        self.driver.find_element(by=By.XPATH, value=locators.Hrm3_Locators().saveicon).click()
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS : Edit in with employeename midname {a}". format(a=data.Hrm3_Data.midname))

class Test_Hrm4:
   
    # Generator function
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        
                
# Code for Test case ID: Tc_PIM_03

    def test_delete(self,booting_function):
        self.driver.maximize_window()
        self.driver.get(data.Hrm4_Data().url)
        sleep(5)
        self.driver.find_element(by=By.NAME, value=locators.Hrm4_Locators().username_inputBox).send_keys(data.Hrm4_Data().username)
        self.driver.find_element(by=By.NAME, value=locators.Hrm4_Locators().password_inputBox).send_keys(data.Hrm4_Data().password)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm4_Locators().LoginButton).click()
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm4_Locators().pimbutton).click()    
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm4_Locators().employee_name).send_keys(data.Hrm4_Data().employee_name)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm4_Locators().search_button).click()    
        sleep(5)
        self.driver.find_element(by=By.XPATH, value=locators.Hrm4_Locators().delete_button).click() 
        self.driver.find_element(by=By.XPATH, value=locators.Hrm4_Locators().yes_button).click() 
        assert self.driver.title == 'OrangeHRM'
        print("SUCCESS: Employee information successfully delete")




   

