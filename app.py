from flask import Flask, request

app = Flask(__name__) 


@app.route('/') # when a request is sent to /( This is the home page).
def home_page(): # run this function. 
    html ="""
    <html>
     <body>
      <h1> Home Page </h1>
      <p> Welcome to my simple App! </p>
      <a href='/hello'> Go to the <b>Hello Page!</b> </a> | 
      <a href='/goodbye'> Go to the <b>Goodbye Page!</b> </a>
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