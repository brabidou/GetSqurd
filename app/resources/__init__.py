from .root import RootResources, RootNameResources
import os


def setup_routes(app):
    # Find the static file folder

    app.add_route("/", RootResources())
    app.add_route("/{name}", RootNameResources())

    base_static_file_folder = os.getcwd() + '/static'
    app.add_static_route('/static', base_static_file_folder)

