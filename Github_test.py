"""Prerequisite- Make sure Python,Selenium,Firefox is installed in machine to run the code,In this program directly I am passing the
web elements, but while developing some package we used to keep those web elements in a separate file.
Currently everything is written in a single file"""

from selenium import webdriver
import os
import sys

class Github_test:
    def __init__(self):
        """Initialization of firefox driver"""
        self.browser = ''
        self.url="https://github.com/"
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(10)

    def open_github_page(self):
        """This method will load the Github page on web browser, currently I am writing for Firefox browser"""

        self.driver.get(self.url)
        print("Navigated to the url" , self.url)
        #To run test on Chrome browser
        # if self.browser == 'chrome':
        #     path = os.path.dirname(os.path.abspath(__file__))
        #     self.driver = webdriver.Chrome(os.path.join(path, "win_chromedriver"))

    def close_github_page(self):
        """This method will close the opened browser"""

        self.driver.quit()

    def validate_signin_button(self):
        """Verify that by clicking on "Sign in" button user is redirected to Github login page"""
        try:
            self.open_github_page()
            self.driver.find_element_by_link_text("Sign in").click()
            element=self.driver.find_element_by_xpath("//h1[contains(.,'Sign in to GitHub')]")
            if element.text == "Sign in to GitHub":
                print("Successfully launched Github login page")
            else:
                raise AssertionError("Current page is not Github login page")
            #Other way
            #title_page=self.driver.title
            #if title_page=="Sign in to GitHub · GitHub":
            #print("Current page is Github login page")
        except:
            raise AssertionError("Unable to validate the signin button")

    def validate_error_prompt_for_blank_username_password(self):
        """Verify that username and password fields are mandatory in login page"""
        try:
            self.open_github_page()
            self.validate_signin_button()
            element = self.driver.find_element_by_xpath("//input[contains(@type,'submit')]").click()
            error = self.driver.find_element_by_xpath("//div[@class='container'][contains(.,'Incorrect username or password.')]")
            if error.text == "Incorrect username or password.":
                print("Please enter valid username and password")
            else:
                raise AssertionError("Error message didnt displayed for blank username and password, which is not expected ")
        except:
            raise AssertionError("Unable to validate error prompt for black Username and password")
        finally:
            self.close_github_page()

    def validate_mandate_password(self):
        """Verify password field is mandatory for login in to Github"""
        try:
            self.open_github_page()
            self.validate_signin_button()
            self.driver.find_element_by_id("login_field").clear()
            self.driver.find_element_by_id("login_field").send_keys("aryaabinash@gamil.com")
            self.driver.find_element_by_name("commit").click()
            error_prompt = self.driver.find_element_by_xpath("//div[@class='container'][contains(.,'Incorrect username or password.')]")
            if error_prompt.text == "Incorrect username or password.":
                print("Please enter valid password which is mandatory")
                self.driver.find_element_by_id("login_field").clear()
            else:
                raise AssertionError("Password is not mandate")
        except:
            raise AssertionError("Unable to validate error prompt for empty password")
        finally:
            self.close_github_page()

    def validate_mandate_username(self):
        """Verify Username field is mandatory for login in to Github"""
        try:
            self.open_github_page()
            self.validate_signin_button()
            self.driver.find_element_by_id("password").clear()
            self.driver.find_element_by_id("password").send_keys("arya123")
            self.driver.find_element_by_name("commit").click()
            error_prompt = self.driver.find_element_by_xpath("//div[@class='container'][contains(.,'Incorrect username or password.')]")
            if error_prompt.text == "Incorrect username or password.":
                print("Please enter valid Username which is mandatory")
                self.driver.find_element_by_id("password").clear()
            else:
                raise AssertionError("Username is not mandate")
        except:
            raise AssertionError("Unable to validate error prompt for black Username")
        finally:
            self.close_github_page()


    def validate_invalid_email(self):
        """Verify that inserting m.ie into email field in reset_password page displays message "Can't find that email, sorry.
        For fourth condition(in assignment) i.e. Verify that inserting empty value into email field in reset_password page displays message "Can't find that email, sorry."
        comment the line i.e. self.driver.find_element_by_id("email_field").send_keys("m.ie") or if we are not commenting then pass a space instead of m.ie"""
        try:
            self.open_github_page()
            self.validate_signin_button()
            self.driver.find_element_by_link_text("Forgot password?").click()
            self.driver.find_element_by_id("email_field").send_keys("m.ie")
            self.driver.find_element_by_name("commit").click()
            retrived_value=self.driver.find_element_by_xpath("//div[@class='container']")
            if retrived_value.text == "Can't find that email, sorry.":
                print("Successfully validtaed the error message for invalid email address, Please enter a valid email address")
            else:
                raise AssertionError("Invalid email is also accepting, which is not expected")
            return retrived_value.text

        except:
            raise AssertionError("Validation for invalid email didnt happened successfully")
        finally:
            self.close_github_page()

    def verify_first_word_of_error_message(self):
        """Verify that the first word in error message in reset_password page is "Can't"""
        try:
            message=self.validate_invalid_email()
            message=message.split()
            if message[0]!="Can't":
                raise AssertionError("First word of error message is not Can't")
        except:
            raise AssertionError("Unable to validate the first word from the error message")
        finally:
            self.close_github_page()

    def verify_sign_up_button(self):
        """Verify that clicking on "Sign up" button will redirect user into "join github" page"""
        try:
            self.open_github_page()
            self.driver.find_element_by_link_text("Sign up").click()
            expected_word=self.driver.find_element_by_xpath("//h1[contains(.,'Join GitHub')]")
            if expected_word.text == "Join GitHub":
                print("Navigated to Join git hub page successfully")
            else:
                raise AssertionError("Unable to navigate to Github page")
        except:
            raise AssertionError("Unable to navigate to Sign Up page")

    def verify_create_your_personal_account(self):
        """Verify that "join github" page contains text "Create your personal account"""
        try:
            self.open_github_page()
            self.verify_sign_up_button()
            element = self.driver.find_element_by_xpath("//h2[@class='f2-light mb-1'][contains(.,'Create your personal account')]")
            if element.text == "Create your personal account":
                print("create your personal accout text is visible")
            else:
                raise AssertionError("Create your personal account is not visible")
        except:
            raise AssertionError("Unable to verify Create Your Personal Account option")
        finally:
            self.close_github_page()

    def buttonstate_validation(self):
        """Verify that "Create an account" button is grayed when an existing email address is inserted in "join github" page,
        this scenario is not clear to me,so the below code may not correct"""
        try:
            self.open_github_page()
            self.driver.find_element_by_id("user_login").send_keys("arya")
            if self.driver.find_element_by_id("signup_button").is_enabled():
                raise AssertionError("button color not grayed")
            else:
                print("Button Color is grayed")
        except:
            raise AssertionError("Unable to validate button state")
        finally:
            self.close_github_page()



#Creating object of the class in order to access the methods, this could be different while writng a packages,with framework and test cases
"""Or we can use if __name__ == "__main__": 
    my_function() """
#As per the requirement we can call the respective function
obj=Github_test()
obj.open_github_page()
obj.validate_signin_button()
obj.validate_error_prompt_for_blank_username_password()
obj.validate_mandate_password()
obj.validate_mandate_username()
obj.validate_invalid_email()
obj.verify_first_word_of_error_message()
obj.verify_sign_up_button()
obj.verify_create_your_personal_account()
obj.buttonstate_validation()

