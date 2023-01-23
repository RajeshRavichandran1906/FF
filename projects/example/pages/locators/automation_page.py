from selenium.webdriver.common.by import By


class AutomationPage:

    parent = (By.CSS_SELECTOR, "main#content")
    texts = (By.CSS_SELECTOR, parent[1] + " div#mw-content-text")