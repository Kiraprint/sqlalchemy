from flask import Flask, render_template

from data import db_session
from data.jobs import Jobs
from data.users import User

app = Flask(__name__)
db_session.global_init('db/mars_explorer.db')


@app.route('/')
@app.route('/index')
def index():
    session = db_session.create_session()
    jobs = session.query(Jobs).all()
    return render_template('journal.html', jobs=jobs, session=session, User=User)


def main():
    app.run()


if __name__ == '__main__':
    main()
