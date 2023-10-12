import http.cookiejar
cookie_jar = http.cookiejar.CookieJar()
def home(request_handler, data, method):
    if method == "POST":
        if 'name' in data:
            # Set a cookie named 'username'
            cookie = http.cookiejar.Cookie(version=0, name='username', value=data['name'], port=None, port_specified=False,
                                           domain="", domain_specified=False, domain_initial_dot=False, path="/",
                                           path_specified=True, secure=False, expires=None, discard=True,
                                           comment=None, comment_url=None, rest={'HttpOnly': None}, rfc2109=False)
            cookie_jar.set_cookie(cookie)
            send_response(request_handler, 200, {"message": f'Hello dear {data["name"]}', "cookie_set": True})
        else:
            send_response(request_handler, 400, {"message": "Bad request"})
    elif method == "GET":
        # Check if the 'username' cookie is set
        username = None
        for cookie in cookie_jar:
            if cookie.name == 'username':
                username = cookie.value
                break
        request_handler.render_template('index.html', title='Home Page', message=f'Welcome back, {username or "guest"}!')
