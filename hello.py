from flask import Flask, render_template, redirect, url_for
app = Flask(__name__)  # constructor, create an application object

@app.route('/hello/<name>')   # a decorator
# routing helps a user remember application URLs
# build url dynamically
def hello_world(name):
    return 'Hello %s' % name

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %s as guest' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name == 'admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest', guest = name))
# url_for accepts the name of a function as first argument, 
# and one or more keyword arguments, each corresponding to the variable part of URL.

# @app.route('/')
# def index():
#     return <html><body><h1>Hello World</h1></body></html>
# return the output of a function associated with a url in the form of html
# generating html from python can be cumbersome
# here we take advantage of jinja template engine
# instead of returning html code, a html file can be rendered
# by render_template()

# flask will try to find the html file in the templates folder
# in the same folder in which this script is present
@app.route('/hello/<user>')
def hello_name(user):
    return render_template('hello.html', name = user)

# insert the variable (user) into the placeholder (name)

if __name__ == '__main__':
    app.run(debug = True)

# app.route(rule, options)
# The rule parameter represents URL binding with the function.
# The options is a list of parameters to be forwarded to the underlying Rule object.

# The jinja2 template engine uses the following delimiters for escaping from HTML.
# {% ... %} for Statements
# {{ ... }} for Expressions to print to the template output
# {# ... #} for Comments not included in the template output
# # ... ## for Line Statements