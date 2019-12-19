# REST & Flask

In this assignment, we will be taking the previous Mad-lib+Flask Assignment and adding RESTful calls to specify paths to the resources.

You will be writing a single REST call with the signature:

`GET /horseman/<name>`

This will return the block of text associated with one of the four companies we have been looking at (as JSON data). The “name” variable will refer to the name of the company you are requesting (Tesla, Apple, etc). So a route for Tesla should look like:

`GET /horseman/tesla`

Here is the information flow that will happen:

1) A user clicks one of your four buttons
2) Javascript intercepts the button click and sends an **XHR** request to the server to retrieve the block of text
3) Javascript inserts the text into a container on your page (such as a \<div>\</div>).
    - For example, if your container is a div as such:
        \<div id=‘rest_div’>\</div>
    - Then, assuming your data is retrieved in ‘my_data’, you could add the text into your container with Javascript like this:
        document.getElementById(‘rest_div’).innerHTML = my_data;

This assignment should require you to write very little code! It’s all about understanding the structure of REST, so if you are confused, please come to office hours!

Use the same code from the previous assignment and copy it to this repository. Then, modify that to include your XHR+REST structure. Make sure to work on this repository!
# Flask-MADLIB
# Flask-MADLIB
