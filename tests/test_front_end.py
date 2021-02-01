import unittest
import urllib3
import os
import time

from flask_testing import LiveServerTestCase
from selenium import webdriver

from app import app, db
from UserData import UserLogin
from tests.test_back_end import TestBase


class TestLogin(TestBase):

    def test_login(self):
        self.driver.find_element_by_id('нажатие на кнопку вход').click()
        time.sleep(1)

        self.driver.find_element_by_id('email').sends_keys(test_users_email)


class TestBase(LiveServerTestCase):

    def create_app(self):
        config_name = 'testing'
        new_app = app(config_name)
        new_app.config.update(dict(db=os.path.join(app.root_path, 'test.db', LIVESERVER_PORT=8943)))
        return new_app

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.get_server_url())

        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test user
        self.user = ''
        db.session.add(self.user)
        db.session.commit()

    def tearDown(self):
        self.driver.quit()

    def test_server_is_up_and_running(self):
        response = urllib3.urlopen(self.get_server_url())
        self.assertEqual(response.code, 200)


if __name__ == '__main__':
    unittest.main()
