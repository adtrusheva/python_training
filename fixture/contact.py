from model.contact import Contact
from selenium.webdriver.support.ui import Select
import os
class ContactHelper:

    def __init__(self, app):
        self.app = app

    def go_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/") and len(wd.find_elements_by_id("maintable")) > 0):
            self.click_home_page_button()

    def click_home_page_button(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def create(self, contact):
        wd = self.app.wd
        self.go_to_home_page()
        # init contact creation
        wd.find_element_by_id("header").click()
        wd.find_element_by_link_text("add new").click()
        # edit contact form 'Upload photo file'
        self.fill_form(contact)
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.go_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.go_to_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.click_home_page_button()
        self.contact_cache = None

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.go_to_home_page()
        # submit edition
        wd.find_element_by_xpath("(//img[@alt='Edit'])[1]").click()
        # edition contact form
        self.fill_form(new_contact_data)
        # submit contact edition
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.go_to_home_page()
        self.contact_cache = None

    def fill_form(self, contact):
        wd = self.app.wd
        self.change_file_value("photo", contact.photo)
        # edition contact form 'Full Name and Job'
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        # edition contact form 'Telephone'
        self.change_field_value("home", contact.home)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("work", contact.work)
        self.change_field_value("fax", contact.fax)
        # edition contact form 'Email and B-day'
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_select_value("bday", contact.bday)
        self.change_select_value("bmonth", contact.bmonth)
        self.change_field_value("byear", contact.byear)
        self.change_select_value("aday", contact.aday)
        self.change_select_value("amonth", contact.amonth)
        self.change_field_value("ayear", contact.ayear)
        # edition contact form 'Secondary'
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_select_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(value)

    def change_file_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            file_name = value
            file_path = os.path.dirname(os.path.realpath('../test_data/' + file_name)) + '\\' + file_name
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(file_path)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.go_to_home_page()
        return len(wd.find_elements_by_xpath("(//img[@alt='Edit'])"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.go_to_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_css_selector('tr[name="entry"]'):
                id = element.find_element_by_name("selected[]").get_attribute('value')
                firstname = element.find_element_by_xpath('td[3]').text
                lastname = element.find_element_by_xpath('td[2]').text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)
