from Darkoob import add_route, run_server
from views import home,about,contact

# Add routes

add_route('/', home,methods=['GET','POST','PUT'])
add_route('/about', about,methods=['GET','POST'])
add_route('/contact', contact)

# Start the server with custom host and port
if __name__ == "__main__":
    run_server(host="127.0.0.1", port=8080)