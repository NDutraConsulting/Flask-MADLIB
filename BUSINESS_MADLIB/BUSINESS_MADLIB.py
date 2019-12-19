# BUSINESS_MADLIB/BUSINESS_MADLIB.py

import os
from flask import Flask, render_template, g, request, redirect
from sqlite3 import dbapi2 as sqlite3

##### APP SETUP #####
app = Flask(__name__)

##### DB SETUP #####

# Setup the database credentials
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'BUSINESS_MADLIB.db'),
    DEBUG=True,
    SECRET_KEY=b'<SOME HEXADECIMAL SECRET KEY>',
    USERNAME='admin',
    PASSWORD='<SOME PASSWORD>'
))

# Connect to the DB
def connect_db():
    #Connects to the specific database.
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

# Wrap the helper function so we only open the DB once
def get_db():
    #Opens a new database connection if there is none yet for the
    #current application context.
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

# Create the database (we do this via command line!!!)
def init_db():
    #Initializes the database.
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

# Command to create the database via command line
# You call it from command line: flask initdb
@app.cli.command('initdb')
def initdb_command():
    #Creates the database tables.
    init_db()
    print('Initialized the database.')


# Close the database when the request ends
@app.teardown_appcontext
def close_db(error):
    #Closes the database again at the end of the request.
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()

##### ROUTES #####

@app.route('/madlib')
def GET_madlib() :
    return render_template('madlib.html')

@app.route('/Amazon')
def GET_amazon() :
    business_name = "Amazon"
    db = get_db()
    cur = db.execute('SELECT business_name, business_type, market_type, job_to_be_done, revenue_model FROM business_madlib WHERE business_name=\"'+business_name+'\"')
    the_business = cur.fetchall()
    return render_template('business.html', entries=the_business, business_name = business_name)

@app.route('/Apple')
def GET_apple() :
    business_name = "Apple"
    db = get_db()
    cur = db.execute('SELECT business_name, business_type, market_type, job_to_be_done, revenue_model FROM business_madlib WHERE business_name=\"'+business_name+'\"')
    the_business = cur.fetchall()
    return render_template('business.html', entries=the_business, business_name = business_name)

@app.route('/Netflix')
def GET_netflix() :
    business_name = "Netflix"
    db = get_db()
    cur = db.execute('SELECT business_name, business_type, market_type, job_to_be_done, revenue_model FROM business_madlib WHERE business_name=\"'+business_name+'\"')
    the_business = cur.fetchall()
    return render_template('business.html', entries=the_business, business_name = business_name)

@app.route('/Tesla')
def GET_tesla() :
    business_name = "Tesla"
    db = get_db()
    cur = db.execute('SELECT business_name, business_type, market_type, job_to_be_done, revenue_model FROM business_madlib WHERE business_name=\"'+business_name+'\"')
    the_business = cur.fetchall()
    return render_template('business.html', entries=the_business, business_name = business_name)


@app.route('/company_data', methods=['POST'])
def GET_company() :
    business_name = request.form['business_name']
    db = get_db()
    cur = db.execute('SELECT business_name, business_type, market_type, job_to_be_done, revenue_model FROM business_madlib WHERE business_name=\"'+business_name+'\"')
    the_business = cur.fetchall()
    return render_template('company_data.html', entries=the_business, business_name = business_name)


@app.route('/post_example', methods=['POST'])
def POST_Example():
    #init_db()
    db = get_db()

    business_name = request.form['business_name']
    business_type = request.form['business_type']
    market_type = request.form['market_type']
    job_to_be_done = request.form['job_to_be_done']
    revenue_model = request.form['revenue_model']

    db.execute('INSERT INTO business_madlib (business_name, business_type, market_type, job_to_be_done, revenue_model) VALUES (?, ?, ?, ?, ?)',
                 [ business_name, business_type, market_type, job_to_be_done, revenue_model ] )
    db.commit()

    return redirect('/madlib')


@app.route('/populate_madlib')
def populate_madlib():
    init_db()
    db = get_db()
    #for loop -

    #business_name = request.form['business_name']
    #business_type = request.form['business_type']
    #market_type = request.form['market_type']
    #job_to_be_done = request.form['job_to_be_done']
    #revenue_model = request.form['revenue_model']


    #Tesla
    business_name = "Tesla"
    business_type = "tech"
    market_type = "internet users"
    job_to_be_done = "make finding products easier"
    revenue_model = "poop fees"


    db.execute('INSERT INTO business_madlib (business_name, business_type, market_type, job_to_be_done, revenue_model) VALUES (?, ?, ?, ?, ?)',
                 [ business_name, business_type, market_type, job_to_be_done, revenue_model ] )
    db.commit()

    ### AMAZON
    business_name = "Amazon"
    business_type = "tech"
    market_type = "internet users"
    job_to_be_done = "make finding products easier"
    revenue_model = "poop fees"


    db.execute('INSERT INTO business_madlib (business_name, business_type, market_type, job_to_be_done, revenue_model) VALUES (?, ?, ?, ?, ?)',
                 [ business_name, business_type, market_type, job_to_be_done, revenue_model ] )
    db.commit()

    ###APPLE
    business_name = "Apple"
    business_type = "tech"
    market_type = "internet users"
    job_to_be_done = "make finding products easier"
    revenue_model = "poop fees"


    db.execute('INSERT INTO business_madlib (business_name, business_type, market_type, job_to_be_done, revenue_model) VALUES (?, ?, ?, ?, ?)',
                     [ business_name, business_type, market_type, job_to_be_done, revenue_model ] )
    db.commit()


    ### NETFLIX
    business_name = "Netflix"
    business_type = "tech"
    market_type = "internet users"
    job_to_be_done = "make finding products easier"
    revenue_model = "poop fees"


    db.execute('INSERT INTO business_madlib (business_name, business_type, market_type, job_to_be_done, revenue_model) VALUES (?, ?, ?, ?, ?)',
                     [ business_name, business_type, market_type, job_to_be_done, revenue_model ] )
    db.commit()


    return redirect('/madlib')


if __name__ == "__main__":
    app.run()
