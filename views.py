from Darkoob import send_response,cookie_set,cookie_get,cookie_delete

# Route functions
def home(request_handler,data,method):
    if method=="POST":
        if 'name' in data:
            send_response(request_handler, 200, {"message": f'hello dear {data["name"]}'})
        else:
            send_response(request_handler, 400, {"message": "bad request"})

    if method=="GET":
        request_handler.render_template('index.html', title='Home Page',message='ss to the Home Page!')


def redirect_test(request_handler,data,method):
    request_handler.redirect("/")


def about(request_handler,data,method):
    request_handler.render_template('about.html', title='About Us')


def contact(request_handler,data,method):
    request_handler.render_template('contact.html', title='Contact Us')



def cookiestest(request_handler, data, method):
    if method == "POST":
        if 'name' in data:
            headers = cookie_set(request_handler, 'user_name', data['name'],age=3600)
            send_response(request_handler, 200, {"message": f'Hello dear {data["name"]}'}, headers=headers)
        else:
            send_response(request_handler, 400, {"message": "Bad request"})

    if method == "GET":
        user_name = cookie_get(request_handler, 'user_name')
        if user_name:
            send_response(request_handler, 200, {"message": f'Hello, {user_name}!'})
        else:
            send_response(request_handler, 200, {"message": "Cookie not found"})
    if method=="DELETE":
        headers = cookie_delete(request_handler, 'user_name')
        send_response(request_handler, 200, {"message": f' cookie deleted'}, headers=headers)