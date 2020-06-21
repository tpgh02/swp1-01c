from cgi import parse_qs
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
from template import html

def application(environ, start_response):
    d = parse_qs(environ['QUERY_STRING'])
    a = d.get('a', [''])[0]
    b = d.get('b', [''])[0]
    x = ''
    y = ''

    try:
      if a == '' or b == '':
        response_body = html % {
            'x' : 'Please Enter the Value',
            'y' : 'Please Enter the Value',
            'a' : a,
            'b' : b
        }

      else:
        if '' not in [a, b]:
            a, b = int(a), int(b)
            global x 
            global y
            x = a + b
            y = a * b

        response_body = html % {
             'x' : x,
             'y' : y,
	     'a' : a,
	     'b' : b 
        }
    except ValueError:
       response_body = html % {
             'x' : 'Please Enter the Integer',
             'y' : 'Please Enter the Integer',
             'a' : a,
             'b' : b
        }
    start_response('200 OK', [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ])
    return [response_body]
