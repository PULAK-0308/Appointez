from django.shortcuts import render
from .models import Patient
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
# Create your views here.
def index(request):
  return render(request,'index.html')


def send(request):
  print(request.method)
  # if(request.method!='post'):
  #   print("not post method")
  #   exit()
  if request.method=="POST":
    print("sign func me hsi")
    email=request.POST['email']
    name=request.POST['name']
    # test=Patient.objects.all()
    user = Patient.objects.all().filter(email=email)
    # print(user,email,name)
    print("yaha tak aa gaye ")
    email_subject="Booking Confirmation"
    message=render_to_string('activate.html',{
        'user':user,
        'domain':'https://ppointez--pulak-0308.repl.co',
        

    })
    print("send kar rhe h ")
    email_message =   EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,[email])
    email_message.send()
    # queryset = Patient.objects.all()
    # queryset = queryset.filter(receipe_name__icontains=request.GET.get('search'))
     
     
     # context = {'receipes':queryset} 
    
    
    try:
      dt = str(user).split()
      print(f"dt is: {dt}\n")
      # c = {'name':dt[0],'age':dt[1],'dp_of_doc':dt[2],'doc':dt[3],'ema':dt[4],'date':dt[5]}
      c = {'f':dt[2:]}
      print(f"\n{c}\n")
      # print(context)
      # print("send ho chuka",type(user))
      return render(request,'index.html',context=c)
    except Exception as e:
      print(e,"\n\nerror\n\n")
    # return render(request,'index.html',context=)
  return render(request,'index.html')

