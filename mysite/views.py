from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .send_email import send_email


# Create your views here.
@csrf_exempt
def one_page(request):
    return render(request, 'onepage/index.html')


@csrf_exempt
@require_http_methods(["POST"])
def handle_ajax_form(request):
    data = request.POST

    name = data.get('Name')
    last_name = data.get('lastName')
    middle_name = data.get('middleName')
    email = data.get('email')
    phone_number = data.get('phoneNumber')
    city = data.get('city')
    nova_poshta_number = data.get('novaPoshtaNumber')
    feet_back = data.get('feetBack')

    if feet_back:
        call = 'No'
    else:
        call = 'Yes'

    msg = f'Name: {name} \nMiddleName: {middle_name} \nLastName: {last_name} \nEmail: {email}  \nPhone: {phone_number} \nCity: {city} \nPost: {nova_poshta_number} \nCall: {call}'
    send_email(msg)

    return JsonResponse({"message": "Form data received successfully!"})

