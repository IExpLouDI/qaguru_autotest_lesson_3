from selene import have


def test_page(driver, gen_data):
	driver.open('/ncr')
	driver.element('textarea[aria-label]').set_value(f"{gen_data}").press_enter()
	assert driver.element('p[aria-level="3"]').should(have.text('did not match any documents.'))


def test_google_search(driver):
	driver.open('/ncr')
	driver.element('[name="q"]').clear().type('yashaka/selene').press_enter()
	driver.element('a[href="https://github.com/yashaka"] h3').should(have.text('Iakiv Kramarenko yashaka'))
