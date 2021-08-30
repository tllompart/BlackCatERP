# Django Library
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Localfolder Library
from ..models import Company
from .bi import Bi
from .wparameter import parameter


def _web_parameter():
    web_parameter = {}
    for parametro in parameter.objects.all():
        web_parameter[parametro.name] = parametro.value
    return web_parameter


#@login_required()
def erp_home(request):
    """Vista para renderizar el dasboard del erp
    """

    bi_list = Bi.objects.filter(dashboard='home', type='indicator')
    if bi_list:
        for bi in bi_list:
            if bi.model:
                from ..models import Partner
                # print(bi.model)
    value = {
        'bi': bi_list,
        'web_parameter': _web_parameter(),
        'company': Company.objects.filter(active=True)
    }
    return render(request, "home.html", value)
