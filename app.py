from flask import Flask, request

app = Flask(__name__) 


@app.route('/') # when a request is sent to /( This is the home page).
def home_page(): # run this function. 
    html ="""
    <html>
     <body>
      <h1> Home Page </h1>
      <p> Welcome to my Simple App! </p>
     <a href='/hello'> Go to the Hello Page!</a> <br>
      <a href='/goodbye'> Go to the <b>Goodbye Page!</b> </a><br>
      <a href='/search'> Go to the Search Page </a><br>
      <a href='/add-comment'> Add a Comment  </a> <br>
      <a href='/r/<subreddit>'> Go to the subreddit page </a><br>
      <a href='/posts/<int:id>'> Go to the Post Page </a><br>
     </body
    </html> 
    """    
    return html
       
#This is a decorator
@app.route('/hello') # when a request is sent to /hello..  
def say_hello(): # run this function. 
    html = """
    <html>
     <body>
       <h1> Hello! </h1>
       <p> This is the Hello Page </p>
        <a href='/'> Go to the Home Page  </a> | 
      <a href='/goodbye'> Go to the <b>Goodbye Page!</b> </a>
     </body>
    </html>   
    """ 
    return html

@app.route('/goodbye')
def say_bye():
    html = """
    <html>
     <body>
       <h1> PeAcE oUt ! </h1>
       <h1>&#9774</h1>
       <br>
       <br>
       <br>
        <a href='/hello'> Go to the <b>Hello Page!</b> </a> | 
      <a href='/'> Go to the Home Page </a>
     </body>
    </html>   
    """ 
    return html


@app.route('/search')
def search():
    term = request.args["term"]
    sort = request.args["sort"]
    # use term to find db data in db that matches term
    return f"<h1>Search Results For : {term} </h1>  <p>Sorting by: {sort} </p>"

# @app.route("/post", methods=["POST", "GET"])
# def post_demo():
#     return " You made a POST request!"


@app.route('/add-comment')
def add_comment_form():
    return """
        <h1>Add Your Comment</h1>
        <form method="POST"> 
          <input type='text' placeholder='comment....' name='comment'>
          <input type='text' placeholder='what is your username?' name='username'>
          <button>Submit</button>
        </form>
        """
        
@app.route('/add-comment', methods=["POST"])
def save_comment():
    comment = request.form["comment"]
    username = request.form['username']
    print (request.form)
    return f"""
        <h1>YOUR COMMENT HAS BEEN SAVED...</h1>
        <ul>
          <li>Username: {username}</li>
          <li>Comment: {comment}</li>
        <ul>  
        """
        
        
@app.route('/r/<subreddit>') # whatever the variable that is passed in, needs a matching param in the view function 
def show_subreddit(subreddit):  #pass in param that matches the variable
  return f"<h1>Browsing The {subreddit} Subreddit </h1>"

POSTS = {
   1: "I like buffalo wings", 
   2: "Sammie is the cutest dog!", 
   3: "Coffee is my favorite drink", 
   4: "Pepperoni & Pineapple Pizza pleases my palate"
 }

# @app.route('/posts/<id>')
# def find_post(id):
#   post = POSTS[id]
#   return f"<p>{post}</p>"  # returns a string.  we need to retrieve an int.  

@app.route('/posts/<int:id>')  # int: specifies and integer as a variable type for 'id' otherwise it will default to a string.  
def find_post(id):
  post = POSTS.get(id, "POST NOT FOUND!")  # POST.get() will search for the id and if it does not find it, "POST NOT FOUND will be returned."
  return f"<p>{post}</p>"

