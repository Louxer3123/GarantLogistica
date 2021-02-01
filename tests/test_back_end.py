import unittest
import os

from flask import abort, url_for
from flask_testing import TestCase

from app import app, db
from UserData import UserLogin


class TestBase(TestCase):

    def create_app(self):
        config_name = 'testing'
        new_app = app(config_name)
        new_app.config.update(dict(db=os.path.join(app.root_path, 'test.db')))
        return new_app

    def setUp(self):
        db.session.commit()
        db.drop_all()
        db.create_all()

        users = UserLogin(login='test_user', psw='test_123')

        db.session.add(users)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):

    def test_index_view(self):
        response = self.client.get(url_for('index'))
        self.assertEqual(response.status_code, 200)

    def test_reg_view(self):
        response = self.client.get(url_for('reg'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(url_for('log'))
        self.assertEqual(response.status_code, 200)

    # def test_logout_view(self):
    #  target_url = url_for('logout')
    #  redirect_url = url_for('log', next=target_url)
    #  response = self.client.get(target_url)
    #  self.assertEqual(response.status_code, 302)
    #  self.assertRedirects(response, redirect_url)


if __name__ == '__main__':
    unittest.main()
