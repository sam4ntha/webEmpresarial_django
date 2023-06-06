from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage #Crear estructura de un mensaje e incluye un metodo para enviarlo
from .forms import ContactForm

# Create your views here.
def contact(request):
    #print("Tipo de peticion: {}".format(request.method)) Saber que tipo de petición recibe
    contact_form = ContactForm() #Creacion de plantilla vacia

    if request.method == "POST": #Detectar si se ha enviado  por el metodo POST algun dato
        contact_form = ContactForm(data=request.POST) #Si se envio, se rellena la plantilla con esa informacion
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')
            #Si todo va bien, se redirecciona a contact
            #Enviamos el correo y redireccionamos 
            email = EmailMessage(
                "PixSoft: Nuevo mensaje de contacto", 
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["airq9496@gmail.com"],
                reply_to=[email]
            )

            try:
                email.send()
                #Todo ha ido bien y redirecciona a OK
                return redirect(reverse('contact')+"?ok")
            except:
                #Algo no ha ido bien y redirecciona a FAIL
                return redirect(reverse('contact')+"?fail")

    return render(request, 'contact/contact.html', {'form':contact_form})