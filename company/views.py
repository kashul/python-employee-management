from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CompanyForms
from .models import Company
from django.http import HttpResponseRedirect


# company = Company.objects.create(name=request.POST['name'], email=request.POST['email'],
#                                  logo=request.POST['logo'], website=request.POST['website'])
# company.save()
# Create your views here.


def lists(request):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000')

    companies = {"companies": Company.objects.all()}

    return render(request, "company/list.html", companies)


def forms(request, id=0):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000')

    if request.method == 'GET':
        if id == 0:

            class Dummy:
                pk = 0
            company = Dummy()

            form = CompanyForms()

            return render(request, "company/register.html", {"forms": form, "company": company})
        else:
            company = Company.objects.get(pk=id)
            form = CompanyForms(instance=company)
        return render(request, "company/register.html", {"forms": form, "company": company})
    else:
        if id == 0:

            company = CompanyForms(request.POST, request.FILES)

            # print(request.POST["email"])
            # print(request.POST["logo"])
            # if company.is_valid():
            company.save()
            return redirect('http://127.0.0.1:8000/company/list')
            # else:
            # return redirect('http://127.0.0.1:8000/company/form/0')
        else:
            print(id)
            company = Company.objects.get(pk=id)
            form = CompanyForms(request.POST, request.FILES, instance=company)
            if form.is_valid():
                form.save()
                print('wada')
                return redirect('http://127.0.0.1:8000/company/list')

            else:
                print('wada na')
            return redirect('http://127.0.0.1:8000/company/list')


def delete(request, id):
    if not request.user.is_authenticated:
        return redirect('http://127.0.0.1:8000')
    if not request.user.is_authenticated:
        return render(request, 'log/log.html')
    company = Company.objects.get(pk=id)
    # form = CompanyForms(request.POST, instance=company)
    if company is not None:
        company.delete()
    return redirect('http://127.0.0.1:8000/company/list')
