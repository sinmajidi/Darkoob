from Darkoob import send_response

# Route functions
def home(request_handler,data,method):
    if method=="POST":
        if 'name' in data:
            send_response(request_handler, 200, {"message": f'hello dear {data["name"]}'})
        else:
            send_response(request_handler, 400, {"message": "bad request"})

    if method=="GET":
        request_handler.render_template('index.html', title='Home Page',message='ss to the Home Page!')

def about(request_handler,data,method):
    request_handler.render_template('about.html', title='About Us')

def contact(request_handler,data,method):
    request_handler.render_template('contact.html', title='Contact Us')

