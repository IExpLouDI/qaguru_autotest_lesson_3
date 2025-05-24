from selene import be, have


def test_page(driver):
	driver[0].open('/ncr')
	driver[0].element('textarea[aria-label]').set_value(f"{driver[1]}").press_enter()
	assert driver[0].element('p[aria-level="3"]').should(have.text('did not match any documents.'))


def test_google_search(driver):
	driver[0].element('[name="q"]').clear().type('yashaka/selene').press_enter()
	driver[0].element('a[href="https://github.com/yashaka"] h3').should(have.text('Iakiv Kramarenko yashaka'))
