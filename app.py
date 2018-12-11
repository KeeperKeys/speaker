from flask import Flask

from auth import bp

app = Flask(__name__)
app.register_blueprint(bp)

POSTGRES = {
    'user': 'speaker',
    'pw': 'speakerp',
    'db': 'speakerdb',
    'host': 'localhost',
    'port': '5432',
}

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

if __name__ == '__main__':
    app.run()
