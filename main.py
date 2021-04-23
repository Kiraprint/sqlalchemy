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
    job = Jobs(team_leader=1, job='deployment of residential modules 1 and 2', work_size=15, end_date=None,
               is_finished=False)
    db_sess.add(job)
    app.run()


if __name__ == '__main__':
    main()
