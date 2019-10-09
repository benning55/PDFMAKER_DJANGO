from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
# Create your views here.


def home(request):
    # fake data
    data = {
        "fname": "Sedthawuth",
        "lname": "Maisonti",
        "age": "20",
    }

    # Rendered
    html_string = render_to_string('maker/home.html', {'data': data})
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Creating http response
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=untitle.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    return response
