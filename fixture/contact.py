from model.contact import Contact
from selenium.webdriver.support.ui import Select
import os
import re


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
        self.delete_contact_by_index(0)

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.edit_contact_by_index(new_contact_data, 0)

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

    def change_select_option(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_value(value)

    def change_file_value(self, field_name, value):
        wd = self.app.wd
        if value is not None:
            file_name = value
            file_path = os.path.dirname(os.path.realpath('test_data\\' + file_name)) + '\\' + file_name
            wd.find_element_by_name(field_name).clear()
            print(file_path)
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
                address = element.find_element_by_xpath('td[4]').text
                all_phones = element.find_element_by_xpath('td[6]').text
                all_emails = []
                for email in element.find_element_by_xpath('td[5]').find_elements_by_css_selector('a'):
                    all_emails.append(email.text)
                all_emails = "\n".join(all_emails)
                self.contact_cache.append(
                    Contact(
                        id=id,
                        firstname=firstname,
                        lastname=lastname,
                        all_phones_from_home_page=all_phones,
                        all_emails_from_home_page=all_emails,
                        address=address
                    )
                )
        return list(self.contact_cache)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        # select first contact
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.click_home_page_button()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.go_to_home_page()
        # select first contact
        self.select_contact_by_id(id)
        # submit deletion
        wd.find_element_by_xpath("(//input[@value='Delete'])").click()
        wd.switch_to_alert().accept()
        self.click_home_page_button()
        self.contact_cache = None

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_contact_by_id(self, new_contact_data, id):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        # edition contact form
        self.fill_form(new_contact_data)
        # submit contact edition
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.go_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_element_by_xpath("//input[@id='" + id + "']/../..//img[@alt='Edit']").click()

    def edit_contact_by_index(self, new_contact_data, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        # edition contact form
        self.fill_form(new_contact_data)
        # submit contact edition
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.go_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_element_by_xpath("(//img[@alt='Edit'])[" + str(index + 1) + "]").click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.go_to_home_page()
        wd.find_element_by_xpath("(//img[@alt='Details'])[" + str(index + 1) + "]").click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute('value')
        id = wd.find_element_by_name("id").get_attribute("value")
        home = wd.find_element_by_name("home").get_attribute("value")
        mobile = wd.find_element_by_name("mobile").get_attribute("value")
        work = wd.find_element_by_name("work").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home=home, mobile=mobile, work=work, phone2=phone2,
                       email=email, email2=email2, email3=email3, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        home = ''
        mobile = ''
        work = ''
        phone2 = ''
        if re.search("H: (.*)", text):
            home = re.search("H: (.*)", text).group(1)
        if re.search("M: (.*)", text):
            mobile = re.search("M: (.*)", text).group(1)
        if re.search("W: (.*)", text):
            work = re.search("W: (.*)", text).group(1)
        if re.search("P: (.*)", text):
            phone2 = re.search("P: (.*)", text).group(1)

        return Contact(home=home, mobile=mobile, work=work, phone2=phone2)

    def add_contact_to_group(self, contact, group_id):
        wd = self.app.wd
        self.go_to_home_page()
        self.select_contact_by_id(contact.id)
        self.change_select_option("to_group", group_id)
        wd.find_element_by_xpath("(//input[@name='add'])").click()

    def delete_contact_from_group(self, contact, group_id):
        wd = self.app.wd
        self.go_to_home_page()
        self.change_select_option("group", group_id)
        self.select_contact_by_id(contact.id)
        wd.find_element_by_xpath("(//input[@name='remove'])").click()
        self.go_to_home_page()
        self.change_select_value("group", '[all]')
