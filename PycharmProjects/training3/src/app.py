from flask import Flask, render_template, request, session
from src.database import Database
from src.blog import Blog
from src.user import User


#blog1 = Blog('SDN Futures', 'Software defined predictions', 'Everyone is waxing lirical about software defined everything.. blah blah blah', 'Harry Schlong')
#blog1.save_to_mongo()
#blogs = Blog.get_data()
#for blog in blogs:
 #   print("=====================")
  #  for a, b in blog.items():
   #     print(a, b)
#print()
################################
#author_search = Blog.get_by_author('Harry Schlong')
#print(author_search.content)
################################
#numbers = Blog.list_comp()
#print(numbers)
################################

app = Flask(__name__)
app.secret_key = "Matt"

@app.before_first_request
def initialize():
    Database.initialize()

@app.route('/')  # for example could have www.mesapro.uk/api/, the '/' indicates localhost 127.0.0.1
def hello_method():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login_user():
    email = request.form['email']
    password = request.form['password']

    if User.login_valid(email, password):
        User.login(email)
    else:
        session['email'] = None

    return render_template("profile.html", email=session['email'])


if __name__ == '__main__':
    app.run(port=4995) # port number is optional

