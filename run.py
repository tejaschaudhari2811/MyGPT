from backend.app  import app
from backend.website import Website

if __name__ == "__main__":
    site = Website(app)
    for route in site.routes:
        print(route)
        app.add_url_rule(
            route,
            view_func=site.routes[route]["function"],
            methods = site.routes[route]["methods"]
        )
    app.run(debug=True)