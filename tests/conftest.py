import random

import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope="session")
def driver(request):
	"""Create session browser"""
	print("Browser create")
	options = webdriver.ChromeOptions()
	options.add_argument("--start-maximized")
	options.add_argument("--disable-blink-features=AutomationControlled")
	options.add_experimental_option("excludeSwitches", ["enable-automation"])
	options.add_experimental_option("useAutomationExtension", False)

	driv = browser
	driv.config.driver_options = options
	driv.config.base_url = "https://google.com"
	yield driv
	print("\nBrowser closing")
	driv.close()


@pytest.fixture()
def gen_data():
	return ''.join([str(_i * random.randint(0, 15)) for _i in range(32)])
