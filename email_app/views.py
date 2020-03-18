from django.shortcuts import render
from django.core.mail import send_mail
# Create your views here.
def index(request):
    send_mail=('helo from mahadeva',
               'helo there is in corona virus',
               'deykaran07@gmail.com',
               ['deykaran02@gmail.com'],
               )
    return render(request,'email_app/index.html')



print('kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaarrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr')