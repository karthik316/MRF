from django.shortcuts import render
from .forms import ContactForm
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import redirect

def index(request):
	return render(request,'personal/main.html')
	
def contact(request):
    form_class = ContactForm

    # new logic!
    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            form_content = request.POST.get('content', '')

            # Email the profile with the 
            # contact information
            template = get_template('personal/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "Your website" +'',
                ['1993rsk@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('/contact')

    return render(request, 'personal/contact.html', {
        'form': form_class,
    })
	
def comittee(request):
	return render(request,'personal/comittee.html')
	
def ownerslist(request):
	return render(request,'personal/ownerslist.html')