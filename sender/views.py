from django.shortcuts import render, redirect
from .models import ModelFile, EmailTemplate
from .forms import EmailForm
from django.core.mail import send_mail
from django.template import Template, Context
import pandas as pd
import os
from django.conf import settings


def Tempalte_list(request):
    tempalte = EmailTemplate.objects.all()
    return render(request,'template_list.html',{'tempalte':tempalte})

def template_edit(request, pk):
    template_obj = EmailTemplate.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = EmailForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save()
            file_path = file_instance.file.path
            extension = os.path.splitext(file_path)[1].lower()

            if extension in ['.xls', '.xlsx']:
                df = pd.read_excel(file_path)
            elif extension == '.csv':
                df = pd.read_csv(file_path)
            else:
                df = None
                print("Unsupported file format")

            if df is not None:
                records = df.to_dict(orient='records') 

                for data in records:
                    subject_template = Template(template_obj.subject)
                    body_template = Template(template_obj.body)

                    subject = subject_template.render(Context(data))
                    body = body_template.render(Context(data))

                    recipient_email = data.get('email')
                    if recipient_email:
                        # Send email via Gmail SMTP
                        send_mail(
                            subject,
                            '',  # Empty string because we are sending HTML in html_message
                            settings.EMAIL_HOST_USER,
                            [recipient_email],
                            fail_silently=False,
                            html_message=body
                        )
                        print(f"Email sent to {recipient_email}")

            return redirect('home')
    else:
        form = EmailForm()

    return render(request, 'emailform.html', {
        'form': form,
        'template_obj': template_obj
    })
