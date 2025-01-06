class Locators:
    # Define the locators as class-level attributes or static methods
    @staticmethod
    def username():
        return "//input[@id='input28']"  # Correct XPath for the username input field

    @staticmethod
    def password():
        return "//input[@name='credentials.passcode']"  # Correct XPath for the password input field

    @staticmethod
    def security_question():
        return "//input[@id='input88']"  #Correct XPath for the Security Question input field

    @staticmethod
    def submit_button():
        return "//input[@type='submit']"  # XPath for the submit button

    @staticmethod
    def sign_in_button():
        return "//button[@aria-label='Sign In Button']"  # XPath for the sign-in button

    @staticmethod
    def password_verify_button():
        return "//input[@value='Verify']"
    @staticmethod
    def click_buttonSQ():
        return "//input[@data-type='save']"

