import logging

from waitress import serve

from handler import list_handlers, registry, show_banner


def wsgiapp(env, start_response):
    path = env['PATH_INFO']
    method = env['REQUEST_METHOD'].lower()
    data = env['wsgi.input'].read()
    handler = registry.get(path, None)

    if not handler:
        start_response('404 Not Found', [('Content-Type', 'application/json')])
        return [b'no such page "', path.encode('utf-8'), b'"']

    try:
        resp = getattr(handler(), method)(data)
    except NotImplementedError:
        start_response(
            '405 Method Not Allowed', [('Content-Type', 'application/json')]
        )
        resp = f'No such method "{method}"'
    except ValueError as ex:
        start_response(
            '400 Bad Request', [('Content-Type', 'application/json')]
        )
        resp = str(ex)
    else:
        start_response('200 OK', [('Content-Type', 'application/json')])

    return [resp.encode('utf-8')]


def startserver(**kwargs):
    logger = logging.getLogger('waitress')
    logger.setLevel(logging.INFO)
    show_banner()
    list_handlers()
    serve(wsgiapp, **kwargs)
