from django.shortcuts import render
from django.http import HttpResponse
import datetime
from datetime import datetime

from .models import users, leave_application
# Create your views here.

# super user id 'Anubha' password 'manager123'
def home(req):
    return render(req, 'index.html',{'err':''})

def authenticate(req):
    unm = req.POST['uname']
    upwd = req.POST['upassword']
    res_set = users.objects.all()

    log = 0
    access = ""

    for rec in res_set:
        nm = rec.u_name
        pwd = rec.u_pwd
        if (unm == nm) & (upwd == pwd) :
            log = 1
            access = rec.u_type
    
    if log == 1:
        if (access == "admin"):
            return render(req, 'main.html',{'nm':unm})
        elif (access == "manager"):
            return render(req, 'manager.html',{'nm':unm})
        elif (access == "employee"):
            return render(req, 'employee.html',{'nm':unm})
    else:
        return render(req, 'index.html',{'err':'Wrong Credentials'})
        

        
def leave(req):
    # form fields (eid, enm, appli, LFrom, Ltill)
    # database field names (e_id, e_name, e_desig, e_application, f_date, t_date, status)
    # date_dt3 = datetime.strptime(date_str3, '%m-%d-%Y')
    i_d = req.POST['eid']
    e_nm = req.POST['enm']
    e_app = req.POST['appli']
    e_frm = datetime.strptime(req.POST['LFrom'],'%Y-%m-%d')
    e_til = datetime.strptime(req.POST['Ltill'],'%Y-%m-%d')

    print("From Date",e_frm)

    rec = leave_application(e_id = i_d, e_name = e_nm, e_desig = "Employee", f_date=datetime.date(e_frm), t_date = datetime.date(e_til),  e_application = e_app, status = "")
    rec.save()
    return HttpResponse("Leave Application Submitted")
    


    
