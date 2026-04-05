"""
conda install frozen-flask


"""
from flask_frozen import Freezer
from flaskportfolio import app

app.config['FREEZER_RELATIVE_URLS'] = True

freezer = Freezer(app)

if __name__ == '__main__':
    app.testing = True
    freezer.freeze()