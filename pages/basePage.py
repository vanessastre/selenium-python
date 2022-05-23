from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def get_element(driver, by_locator):
    return WebDriverWait(driver, 10).until(EC.presence_of_element_located(by_locator))

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)
    
    def back_page(self):
        self.driver.back()

    def close_page(self):
        self.driver.close()

    def quit_page(self):
        self.driver.quit()

    def reload_page(self):
        self.driver.refresh()

    def type_element(self, by_locator, text):
        self.get_element(by_locator).clear()
        self.get_element(by_locator).send_keys(text)

    def click_element(self, by_locator):
        self.get_element(by_locator).click()

    def is_element_visible(self, by_locator):
        return self.get_element(by_locator).is_displayed()
    
    def is_element_enabled(self, by_locator):
        return self.get_element(by_locator).is_enabled()

    def get_title(self):
        return self.driver.title

    def get_url(self):
        return self.driver.current_url

    def get_element(self, by_locator):
        return get_element(self.driver, by_locator)

    def get_elements(self, by_locator):
        return self.driver.find_elements(by_locator)

    def get_element_text(self, by_locator):
        return self.get_element(by_locator).text

    def get_element_attribute(self, by_locator, attribute):
        return self.get_element(by_locator).get_attribute(attribute)

    def get_element_property(self, by_locator, property):
        return self.get_element(by_locator).get_property(property)

    def get_element_tag_name(self, by_locator):
        return self.get_element(by_locator).tag_name
