from selene import browser
from selene import have, be
from selenium.webdriver.common import keys
import pytest

def test_registration_form(test_browser_managment):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.should(have.title('DEMOQA'))
    browser.element('[id="firstName"]').should(be.blank).type('Evgeniia')
    browser.element('[id="lastName"]').should(be.blank).type('Belikova')
    browser.element('[id="userEmail"]').should(be.blank).type('mur@loc.ru')
    browser.element('[for="gender-radio-1"]').should(be.clickable)
    browser.element('[for="gender-radio-2"]').should(be.clickable).click()
    browser.element('[for="gender-radio-3"]').should(be.clickable)
    browser.element('[id="userNumber"]').should(be.blank).type('88002000600')
    browser.element('[id= "dateOfBirthInput"]').type(keys.COMMAND + 'a' + keys.NULL + '31.03.1997').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').should(be.clickable).click()
    browser.element('[for="hobbies-checkbox-2"]').should(be.clickable).click()
    browser.element('[for="hobbies-checkbox-3"]').should(be.clickable).click()
    browser.element('[id="currentAddress"]').should(be.blank).type('Moscow, Russia').press_enter()
    browser.element('[id="close-fixedban"]').click()
    browser.element('[id="submit"]').click()
    browser.element('[id="example-modal-sizes-title-lg"]').should(have.text('Thanks for submitting the form'))

def one_more():
    browser.open()