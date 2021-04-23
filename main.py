from flask import Flask, redirect
from flask import render_template

from data import db_session
from data.jobs import Jobs
from data.users import User

from forms.user import RegisterForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    db_sess = db_session.create_session()
    user = User(surname='Scott', name='Ridley', age=21, position='captain', speciality='research engineer',
                address='module_1', email='scott_chief@mars.org')
    user2 = User(surname='Scot', name='Idley', age=22, position='warrior', speciality='sniper',
                 address='module_2', email='scot_chief@mars.org')
    user3 = User(surname='Cott', name='Dley', age=23, position='pilot', speciality='pilot',
                 address='module_3', email='cott_chief@mars.org')
    user4 = User(surname='Ott', name='Ley', age=24, position='chef', speciality='chef',
                 address='module_4', email='ott_chief@mars.org')
    db_sess.add(user)
    db_sess.add(user2)
    db_sess.add(user3)
    db_sess.add(user4)
    app.run()


if __name__ == '__main__':
    main()
