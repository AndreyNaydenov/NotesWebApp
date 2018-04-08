from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    string = r"""
    <form action="/5">
        <input type="text" name="num">
        <button type="submit">Submit</button>
    </form>
    """
    return Response('Enter a number!\n'+ string)

def kek(request):
    query = request.GET['num']
    try:
        n = int(query)
    except Exception:
        return Response('Invalid request.')
    return Response(str(n * 5))

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_route('xfive', '/5')
        config.add_view(hello_world, route_name='hello')
        config.add_view(kek, route_name='xfive')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 80, app)
    server.serve_forever()
