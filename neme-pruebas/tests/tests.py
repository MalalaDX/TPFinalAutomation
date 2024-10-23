#Punto 3 Trabajo integrador Módulo 3 - QA

import unittest
from selenium.webdriver.common.by import By
from selenium import webdriver
from dotenv import load_dotenv
import os
from selenium.webdriver.firefox.options import Options
from pages.page_login import Page_Login
from pages.page_inventory import Page_Inventory
from pages.page_cart import Page_Cart
from pages.page_checkout import Page_Checkout

class Compras(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        options = Options()
        options.add_argument('--incognito')
        options.add_argument('--headless')
        cls.driver = webdriver.Firefox(options=options)
        
    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()
        cls.driver.quit()
            
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        load_dotenv()
        base_url = os.getenv('BASE_URL')
        user = os.getenv('USER')
        password = os.getenv('PASS')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.driver.get(base_url)
        page_login = Page_Login(self.driver)
        page_login.login(user,password)
        self.page_inventory = Page_Inventory(self.driver)

    def test_order_prices(self):
        self.page_inventory.select_order_by_visible_text('Price (low to high)')
        prices = self.driver.find_elements(By.CLASS_NAME, 'inventory_item_price')
        prices_list = [float(price.text.replace('$', '')) for price in prices]
        self.assertEqual(prices_list, sorted(prices_list))
     
    def test_first_buy(self):
        add_btn = self.driver.find_elements(By.CLASS_NAME, 'btn_inventory')
        for button in add_btn:
               button.click()
        self.page_inventory.go_to_cart()
        page_cart = Page_Cart(self.driver)
        self.driver.find_element(By.ID, 'shopping_cart_container').click()
        products = self.driver.find_elements(By.CLASS_NAME, 'cart_item')
        self.assertEqual(len(products), len(add_btn))
        page_cart.go_to_checkout()
        page_checkout = Page_Checkout(self.driver)
        self.driver.find_element(By.ID, 'first-name').send_keys('María Laura')
        self.driver.find_element(By.ID, 'continue').click()
        message = page_checkout.get_error_message()
        self.assertEqual('Error: Last Name is required', message)
        self.driver.find_element(By.ID, 'last-name').send_keys('Neme')
        self.driver.find_element(By.ID, 'continue').click()
        message = page_checkout.get_error_message()
        self.assertEqual('Error: Postal Code is required', message)
        
    def test_second_buy(self):
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
        self.page_inventory.go_to_cart()
        self.driver.find_element(By.ID, 'remove-sauce-labs-bike-light').click()
        cart_items = self.driver.find_elements(By.CLASS_NAME, 'cart_item')
        self.assertEqual(len(cart_items), 0, 'Aún hay artículos en el carrito.')
        self.driver.find_element(By.ID, 'continue-shopping').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-onesie').click()
        self.driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
        self.page_inventory.go_to_cart()
        cart_items = self.driver.find_elements(By.CLASS_NAME, 'cart_item')
        self.assertEqual(len(cart_items), 2)
        page_cart = Page_Cart(self.driver)
        page_cart.go_to_checkout()
        page_checkout = Page_Checkout(self.driver)
        page_checkout.checkout('María Laura', 'Neme', '6555')
        self.driver.find_element(By.ID, 'finish').click()
        msgerror = page_checkout.get_final_message()
        self.assertEqual('Thank you for your order!', msgerror)



