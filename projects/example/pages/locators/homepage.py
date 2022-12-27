from selenium.webdriver.common.by import By


class Homepage:

    parent = (By.CSS_SELECTOR, "body#www-wikipedia-org")
    search_input_box = (By.CSS_SELECTOR, parent[1] + " input#searchInput")
    search_button = (By.CSS_SELECTOR, "button.pure-button")
    email_text_box = (By.CSS_SELECTOR, "input[type='email']")
    password_text_box = (By.CSS_SELECTOR, "input[name='passwd']")
    submit_button = (By.CSS_SELECTOR, "div.inline-block input[type='submit']")
