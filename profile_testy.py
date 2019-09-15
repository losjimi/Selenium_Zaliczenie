# -*- coding: utf-8 -*-
#Scenariusz:
# Rejestracja nowego profilu
#
# Przypadki testowe:
#
# Rejestracja nowego profilu z blednym numerem NIP / bez Innego identyfikatora
#
# Kroki:
# 1. Otworzy przeglądarkę Firefox
# 2. Wejść na stronę https://lsi-szkol.slaskie.pl
# 3. Wprowadzamy login i haslo
# 4. Klikamy „Zaloguj się”
# 5. Z listy rozwijanej (w prawym górnym rogu ikona klucza  ) wybieramy „Utwórz własny nowy profil”
# 6. Odpowiadamy na pytanie „Czy podmiot ma siedzibę poza granicami Polski”
# W przypadku odpowiedzi NIE:
# 7. Wprowadzamy numer REGON
# 8. Klikamy aktualizuj z REGON (opcjonalnie)
# 9. Wprowadzamy błędny NIP
# 10. Wprowadzamy nazwę firmy
# 11. Wprowadzamy PKD
# 12. Wprowadzamy Nazwę PKD
# 13. Wprowadzamy kod KRS
# 14. Ze słownika wybieramy Miejscowość
# 15. Ze słownika wybieramy Ulicę (jeśli istnieje)
# 16. Wprowadzamy numer budynku (jeśli istnieje)
# 17. Wprowadzamy numer lokalu (jeśli istnieje)
# 18. Wprowadzamy kod pocztowy
# 19. Wprowadzamy nr telefonu
# 20. Wprowadzamy numer faxu
# 21. Wprowadzamy adres email
# 22. Wybieramy z listy formę prawną podmiotu
# 23. Wybieramy z listy formę własności
# 24. Klikamy „Zapisz i wyjdź”
# W przypadku odpowiedzi TAK:
# 25. Wprowadzamy nazwę firmy
# 26. Wprowadzamy kraj
# 27. Wprowadzamy miejscowość
# 28. Wprowadzamy ulicę
# 29. Wprowadzamy numer budynku (jeśli istnieje)
# 30. Wprowadzamy nr lokalu (jeśli istnieje)
# 31. Wprowadzamy kod pocztowy
# 32. Wprowadzamy nr telefonu
# 33. Wprowadzamy numer faxu
# 34. Wprowadzamy adres email
# 35. Wybieramy z listy formę prawną podmiotu
# 36. Wybieramy z listy formę własności
# 37. Klikamy „Zapisz i wyjdź”


#
# Oczekiwany rezultat:
# User otrzymuje informację, że podany NIP jest nieprawidlowy

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
    def test_register_new_profile_(self):
        driver = self.driver

#Wypenienie loginu i hasla
        name = driver.find_element_by_id('username')
        name.send_keys(log.log_value)
        passwd = driver.find_element_by_id('password')
        passwd.send_keys(log.pass_value)
        zaloguj_btn = driver.find_element_by_xpath("//button[@id='btn-submit']")
        zaloguj_btn.click()

#Utworzenie nowego profilu
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
            city = driver.find_element_by_css_selector('.ng-pristine > .input-group .btn-primary')
            city.click()
            city_search = driver.find_element_by_xpath("//input[@id='search.nazwa']")
            city_search.send_keys(test_data.city)
            find_city = driver.find_element_by_xpath("//button[@type='submit']")
            find_city.click()
            time.sleep(10) #czekamy na wyszukanie miast
            city_click = driver.find_element_by_css_selector('.btn-xs')
            city_click.click()
            # street = driver.find_element_by_css_selector(".form-group:nth-child(5) .btn-primary ")
            # street.click()
            # street_search = driver.find_element_by_xpath("//input[@id='search.value']")
            # street_search.send_keys(test_data.street)
            # find_street = driver.find_element_by_xpath("//button[@type='submit']")
            # find_street.click()
            # time.sleep(10)
            # driver.find_element_by_xpath("(//button[@type='button'])[9]").click()
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
#W przypadku wybrania odpowiedzi TAK Czy podmiot ma siedzibę poza granicami Polski? nie wprowadzamy danych z Regon
#Test sprawdzac bedzie czy wprowadzono wartosc w polu Inny Identyfikator
        else:
            all_country = driver.find_element_by_id('tak_poza_pl')
            all_country.click()
            #other_id = driver.find_element_by_id('inny_identyfikator')
            #other_id.send_keys(test_data.valid_other_id)
            name = driver.find_element_by_xpath("//div[@id='nazwa']/input")
            name.send_keys(test_data.valid_name)
            country = driver.find_element_by_xpath("//input[@id='adr_kraj']")
            country.send_keys(test_data.valid_country)
            other_city = driver.find_element_by_xpath("//input[@id='adr_miejscowosc']")
            other_city.send_keys(test_data.valid_other_city)
            other_street = driver.find_element_by_xpath("//input[@id='adr_ulica_nazwa']")
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
        if test_data.siedziba_poza == 'Nie':
            error_notice = driver.find_element_by_xpath("//small[contains(.,' Błędny numer NIP. Sprawdź dane.')]")
            assert error_notice.is_displayed()
            self.assertEqual(error_notice.text, u'Błędny numer NIP. Sprawdź dane.')
        else:
            error_notice = driver.find_element_by_xpath("//div[@id='inny_identyfikator']/div")
            assert error_notice.is_displayed()
            self.assertEqual(error_notice.text, u'pole nie może być puste')



#Zaczekanie na komunikat
        time.sleep(5)



if __name__ == '__main__':
    unittest.main(verbosity=2)
