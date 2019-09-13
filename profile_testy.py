# -*- coding: utf-8 -*-
#Scenariusz:
#Zaciganie danych z bazy Regon
#
# Przypadki testowe:
#
# Rejestracja pierwszego użytkownika na fakowych danych
#
# Kroki:
# 1. Otworzy przegldarke Firefox
# 2. Wejść na stronę https://lsi-szkol.slaskie.pl
# 3. Wprowadzamy login i haslo
# 4. Klikamy Zaloguj sie
# 5. Z listy rozwijanej (w prawym grnym rogu ikona klucza) wybieramy 'Utworz wlasny nowy profil'
# 6. Wprowadzamy numer REGON
# 7. Klikamy 'Aktualizyj z Regon'
#
# Oczekiwany rezultat:
# User otrzymuje informację, że podany email jest ju wykorzystywany

import unittest
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select
import test_data
import log

class ProfilTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://lsi-szkol.slaskie.pl/")
#dać time sleep aby www zdazy sie zaladowac  time.sleep(2)
        self.driver.implicitly_wait(20)
    def tearDown(self):
        self.driver.quit()
    def test_register_wrong_email_(self):
        driver = self.driver
# """
#         zaloguj_btns = driver.find_elements_by_class_name('navigation__button')
#         zaloguj_btns[28].click() #najgorsze praktyki
#  2 najgorsze praktyki dostanie się poprzez XPATH
#  3 najgorsze praktyki dostanie się poprzez CSS sleector
#
# """
        # zaloguj_btn = self.driver.find_element_by_class_name('navigation__button navigation__button--simple')
        # zaloguj_btn.click()
#        zaloguj_btn = driver.find_element_by_css_selector("#app > header > div.header__inner > div > nav > ul > li:nth-child(7) > button")
#        zaloguj_btn.click()
#        zaloguj_btn = driver.find_element_by_xpath("//button[@data-test='navigation-menu-signin']")
#        zaloguj_btn.click()



#aby napisać własnego xPath wpisujemy w kodzie strony //<tag>[@]<nazwa zmiennej i wartość> np //button[@data-test='navigation-menu-signin']
#        register = driver.find_element_by_xpath('//*[@id="login-modal"]/form/div/p/button')#wlasny xpath //button[text()='Rejestracja']
#        register.click()

#Wypenienie loginu i hasla
        name = driver.find_element_by_id('username')
        name.send_keys(log.log_value)
        passwd = driver.find_element_by_id('password')
        passwd.send_keys(log.pass_value)
        zaloguj_btn = driver.find_element_by_xpath("//button[@id='btn-submit']")
        zaloguj_btn.click()

#Utworzenie nowego profilu



#        surname = driver.find_element_by_xpath('//input[@data-test="registrationmodal-last-name-input"]')
#        surname.send_keys(test_data.valid_surname)
#        if test_data.sex == 'male':
#            male = driver.find_element_by_xpath('//label[@for="register-gender-male"]')
#            driver.execute_script("arguments[0].click()", male)
#        else:
#            male = driver.find_element_by_xpath('//label[@for="register-gender-female"]')
#            driver.execute_script("arguments[0].click()", male)
#webdriver posiada metode wywolujaca skrypt JS driver.execute.script("argument[0].click", find element ...)
        #male.click() - other element receive the click - jakiś element zakrywa kliknięcie
#        phone = driver.find_element_by_name('mobilePhone')
#        phone.send_keys(test_data.valid_phone)
#        passy = driver.find_element_by_xpath('//input[@type="password"][@data-test="booking-register-password"]')
#        passy.send_keys(test_data.valid_pass)
        # national = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        # #national.send_keys(test_data.valid_nationality)
        # national.click()
        # #możemy wybrać z listy //div[@class="register-form__country-container__locations"]/label[164]
        # national_choose = driver.find_element_by_xpath('//div[@class="register-form__country-container__locations"]/label[164]')
        # national_choose.location_once_scrolled_into_view #scroluje
        # national_choose.click()
        # wyszukiwanie nazwy kraju po zmiennej w test_data
#        national = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
#        national.click()
#        national_choose = driver.find_element_by_xpath('//div[@class="register-form__country-container__locations"]')
#        countries = national_choose.find_elements_by_xpath('label')
#        for label in countries:
#            d=label.find_element_by_tag_name('strong')
            #print(d.text)
#            if d.get_attribute("innerText")==test_data.valid_nationality:
                #print(national_choose)
#                d.location_once_scrolled_into_view #scroluje
#                d.click()
#                break
        menu_key = driver.find_element_by_css_selector('.dropdown:nth-child(1) > .btn')
        menu_key.click()
        menu_choose = driver.find_element_by_link_text('Utwórz własny nowy profil')
        menu_choose.click()

#Wprowadzanie Regon i zaciganie z bazy centralnej
        if test_data.siedziba_poza == 'Nie':
            all_country = driver.find_element_by_id('nie_poza_pl')
            all_country.click()
            regon = driver.find_element_by_id('regon')
            regon.send_keys(test_data.valid_profile_regon)
            nip = driver.find_element_by_xpath("//input[@id='nip']")
            nip.send_keys(test_data.invalid_nip)
            name = driver.find_element_by_xpath("//div[@id='nazwa']/input")
            name.send_keys(test_data.valid_name)
            pkd = driver.find_element_by_xpath("//input[@id='pkd_kod']")
            pkd.send_keys(test_data.valid_PKD)
            pkd_name = driver.find_element_by_xpath("//input[@id='pkd']")
            pkd_name.send_keys(test_data.valid_PKD_name)
            krs = driver.find_element_by_xpath("//input[@id='krs']")
            krs.send_keys(test_data.valid_KRS)
            #city = driver.find_element_by_css_selector('.ng-pristine .btn-primary')
            #city.click()
            #city_search = driver.find_element_by_id('search.nazwa')
            #city_search.send_keys(test_data.city)
            #find_city = driver.find_element_by_css_selector('.btn-sm:nth-child(1)')
            #find_city.click()
            #pagging = driver.find_element_by_id('liczba')
            #pagging_100 = driver.find_element_by_css_selector('option:nth-child(4)')
            #pagging_100.click()
            #city_click = driver.find_element_by_css_selector('.ng-scope:nth-child(20) > .ng-binding')
            #city_click.click()
            #street = driver.find_element_by_css_selector(".form-group:nth-child(5) .btn-primary ")
            #street.click()
            #street_find = driver.find_element_by_xpath("//input[@id='search.value']")
            #street_find.send_keys(test_data.street)
            building = driver.find_element_by_xpath("//div[@id='adr_budynek']/input")
            building.send_keys(test_data.valid_b_number)
            local = driver.find_element_by_xpath("//div[@id='adr_lokal']/input")
            local.send_keys(test_data.valid_l_number)
            zip_code = driver.find_element_by_xpath("//div[@id='adr_kod']/input")
            zip_code.send_keys(test_data.valid_zip_code)
            phone = driver.find_element_by_xpath("//div[@id='telefon']/input")
            phone.send_keys(test_data.valid_pho_num)
            fax = driver.find_element_by_xpath("//div[@id='fax']/input")
            fax.send_keys(test_data.valid_fax)
            email = driver.find_element_by_xpath("//div[@id='email']/input")
            email.send_keys(test_data.valid_email)
            #date_from = driver.find_elements_by_id('data_rozp')
            #date_from.send_keys(test_data.valid_date_from)
            legal_form = driver.find_element_by_id('forma_prawna_id')
            legal_form.click()
            legal_form_click = driver.find_element_by_xpath("//select[@id='forma_prawna_id']/option[7]")
            legal_form_click.click()
            prop_form = driver.find_element_by_id('forma_wlasnosci_id')
            prop_form.click()
            prop_form_click = driver.find_element_by_xpath("//select[@id='forma_wlasnosci_id']/option[3]")
            prop_form_click.click()
            save = driver.find_element_by_xpath("//button[contains(.,'Zapisz i wyjdź')]")
            save.click()
        else:
            all_country = driver.find_element_by_id('tak_poza_pl')
            all_country.click()
            other_id = driver.find_element_by_id('inny_identyfikator')
            other_id.send_keys(test_data.valid_other_id)
            name = driver.find_element_by_xpath("//div[@id='nazwa']/input")
            name.send_keys(test_data.valid_name)
            country = driver.find_element_by_id('adr_kraj')
            country.send_keys(test_.valid_country)
            other_city = driver.find_element_by_id('adr_miejscowosc')
            other_city.send_keys(test_data.valid_other_city)
            other_street = driver.find_element_by_id('adr_ulica_nazwa')
            other_street.send_keys(test_data.valid_other_street)
            building = driver.find_element_by_xpath("//div[@id='adr_budynek']/input")
            building.send_keys(test_data.valid_b_number)
            local = driver.find_element_by_xpath("//div[@id='adr_lokal']/input")
            local.send_keys(test_data.valid_l_number)
            zip_code = driver.find_element_by_xpath("//div[@id='adr_kod']/input")
            zip_code.send_keys(test_data.valid_zip_code)
            phone = driver.find_element_by_xpath("//div[@id='telefon']/input")
            phone.send_keys(test_data.valid_pho_num)
            fax = driver.find_element_by_xpath("//div[@id='fax']/input")
            fax.send_keys(test_data.valid_fax)
            email = driver.find_element_by_xpath("//div[@id='email']/input")
            email.send_keys(test_data.valid_email)
            legal_form = driver.find_element_by_id('forma_prawna_id')
            legal_form.click()
            legal_form_click = driver.find_element_by_xpath("//select[@id='forma_prawna_id']/option[7]")
            legal_form_click.click()
            prop_form = driver.find_element_by_id('forma_wlasnosci_id')
            prop_form.click()
            prop_form_click = driver.find_element_by_xpath("//select[@id='forma_wlasnosci_id']/option[3]")
            prop_form_click.click()
            save = driver.find_element_by_xpath("//button[contains(.,'Zapisz i wyjdź')]")
            save.click()



#Weryfikacja prawidlowego NIPu
        error_notice = driver.find_element_by_xpath("//small[contains(.,' Błędny numer NIP. Sprawdź dane.')]")
        assert error_notice.is_displayed()
        self.assertEqual(error_notice.text, u'Błędny numer NIP. Sprawdź dane.')


#        newsletter = driver.find_element_by_xpath('//label[@for="registration-special-offers-checkbox"][@class="rf-checkbox__label"]')
#        newsletter.click()
#        pol_prv = driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]')
#        pol_prv.click()
#        mail = driver.find_element_by_xpath('//input[@type="email"][@data-test="booking-register-email"]')
#        mail.send_keys(test_data.invalid_email)
#        rejestracja = driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]')
#        rejestracja.click()
#        error_notice = driver.find_element_by_xpath("(//span[contains(text(), 'Nieprawidłowy adres e-mail')])[2]")
        #prawidłowy rezultat jest tutaj - sprawdzamy czy jest nieprawidłowy adres email i czy to jest widoczne is displayed
#        assert error_notice.is_displayed()
#        self.assertEqual(error_notice.text, u'Nieprawidłowy adres e-mail')
        #self.assertIn("Nieprawidłowy adres e-mail".decode("utf-8"), driver.find_element_by_name())
#        driver.save_screenshot('hh.png')
        time.sleep(10)


#różnica miedzy xpath a css selector to //input[@data-test="booking-register-country"] a input[data-test="booking-register-country"]

#       imie = driver.find_element_by_name('firstName')
#       imie.send_keys("Jim")


        # select_city = Select(driver.find_element_by_id("..."))
        # act_option = []
        # for option in select_univercity.options:
        #     print option.get_attribute("text")
        # self.assertEqual(11, len(select_univercity.options))



    # def test_cities_(self):

    #     driver = self.driver
    #     driver.get("http://www.wsb.pl")
    #     select_univercity = Select(driver.find_element_by_id("edit-city"))#obiekt instancji select
    #     act_option = []
    #     exp_option = [u'Wybierz miasto',u'Bydgoszcz',u'Chorzów/Katowice',u'Gdańsk',u'Gdynia',u'Opole',u'Poznań',u'Szczecin',u'Toruń',u'Warszawa',u'Wrocław']#u jako unicode
    #     for option in select_univercity.options:
    #         act_option.append(option.get_attribute("text"))
    #     self.assertEqual(exp_option, act_option)
if __name__ == '__main__':
    unittest.main(verbosity=2)
