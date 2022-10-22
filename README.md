# flask_blog_October_2022
It is available on GitHub.
It uses the Flask web framework.
It uses at least one module from the Python Standard Library other than the random module (for example, you could use the datetime module.)
It contains at least one class written by you that has both properties and methods (plural!), including instantiating the class and using the methods in your app. Methods that just print something in the terminal will not be considered.
It makes use of JavaScript in the front end and uses the localStorage of the web browser.
It uses modern JavaScript (for example, let and const rather than var.)
It makes use of the writing to and reading from the same file feature.
It contains both conditional statements and loops.
It doesn't generate any error message even if the user enters a wrong input.
It lets the user enter a value in a text box at some point. This value should be received and processed by your back end Python code.
The code follows the code and style conventions we introduced in the course, is fully documented using comments and doesn't contain unused or experimental code. In particular, the code should not use print() or console.log() for any information the app user should see. Instead, all user feedback needs to be visible in the browser.


Run server instructions:
install flask
pip3 install flask

provide the "FLASK_APP" environment variable
$env:FLASK_APP = "example"

for server to restart to each change:
$env:FLASK_DEBUG = "1"

run the server at localhost port 8080
python -m flask run -h localhost -p 8080