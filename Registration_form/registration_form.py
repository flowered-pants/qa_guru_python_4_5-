import os
from selene import browser
from selene import have, be
from selenium.webdriver import Keys
from selenium.webdriver.common import keys


def test_registration_form(browser_managment):
    browser.open('/automation-practice-form')
    browser.should(have.title('DEMOQA'))
    browser.element('#firstName').should(be.blank).type('Evgeniia')
    browser.element('#lastName').should(be.blank).type('Belikova')
    browser.element('#userEmail').should(be.blank).type('mur@loc.ru')
    browser.element('[for="gender-radio-1"]').should(be.clickable)
    browser.element('[for="gender-radio-2"]').should(be.clickable).click()
    browser.element('[for="gender-radio-3"]').should(be.clickable)
    browser.element('#userNumber').should(be.blank).type('88002000600')
    browser.driver.execute_script('window.scrollBy(0, 300)')
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="1997"]').click()
    browser.element('.react-datepicker__day--031').click()
    browser.element('#subjectsInput').should(be.blank).type('text')
    browser.element('[for="hobbies-checkbox-1"]').should(be.clickable).click()
    browser.element('[for="hobbies-checkbox-2"]').should(be.clickable).click()
    browser.element('[for="hobbies-checkbox-3"]').should(be.clickable).click()
    browser.element('#uploadPicture').send_keys((os.getcwd()+"/picture/pic.png"))
    browser.element('#currentAddress').should(be.blank).type('Moscow, Russia').press_enter()
    browser.driver.execute_script('window.scrollBy(0, 500)')
    browser.element('#close-fixedban').click()
    browser.element('#state').click()
    browser.element('#react-select-3-option-1').click()
    browser.element('#city').click()
    browser.element('#react-select-4-option-2').click()
    browser.element('#submit').click()
#проверки
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('//tbody/tr[1]/td[2]').should(have.text('Evgeniia Belikova'))
    browser.element('//tbody/tr[2]/td[2]').should(have.text('mur@loc.ru'))
    browser.element('//tbody/tr[3]/td[2]').should(have.text('Female'))
    browser.element('//tbody/tr[4]/td[2]').should(have.text('8800200060'))
    browser.element('//tbody/tr[5]/td[2]').should(have.text('31 March,1997'))
    #browser.element('//tbody/tr[6]/td[2]').should(be.blank)
    browser.element('//tbody/tr[7]/td[2]').should(have.text('Sports, Reading, Music'))
    browser.element('//tbody/tr[8]/td[2]').should(have.text('pic.png'))
    browser.element('//tbody/tr[9]/td[2]').should(have.text('Moscow, Russia'))
    browser.element('//tbody/tr[10]/td[2]').should(have.text('Uttar Pradesh Merrut'))