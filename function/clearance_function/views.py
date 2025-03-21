from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import io

import datetime

class ClearanceMaker(View):
    template_name = 'barangay_form.html'
    pdf_template = 'barangay_clearance.html'

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        # Get data from request
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        age = request.POST.get("age")
        civil_status = request.POST.get("civil_status")
        address = request.POST.get("address")
        captain_name = request.POST.get("captain_name")

        # Validate required fields
        if not all([first_name, last_name, age, civil_status, address, captain_name]):
            return HttpResponse("Missing required fields", content_type="text/plain")

        # Generate the current date
        date_issued = datetime.date.today().strftime("%B %d, %Y")

        # Render the HTML template with context
        html_string = render_to_string(self.pdf_template, {
            'first_name': first_name,
            'last_name': last_name,
            'age': age,
            'civil_status': civil_status,
            'address': address,
            'captain_name': captain_name,
            'date_issued': date_issued,
        })

        # Convert HTML to PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename=Barangay_Clearance_{first_name}_{last_name}.pdf'

        pdf_file = HTML(string=html_string).write_pdf()
        response.write(pdf_file)

        return response

