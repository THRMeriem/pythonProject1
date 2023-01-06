from django.http import HttpResponse
from django.shortcuts import render
from .models import Dht
import xlwt
def home(request):
    return render(request,'index.html')


def dht11(request):
    tab = Dht.objects.all()
    s = {'tab': tab}
    return render(request, 'pagehtml.html', s)
def tab(request):
    b=len(Dht.objects.all())
    tab = Dht.objects.all()[b-3:b]
    s1 = {'tab': tab}
    return render(request, 'tab.html', s1)

def alerte(request):
    alerte = Dht.objects.all()
    s2 = {'alerte': tab}
    return render(request, 'alerte.html', s2)

def graphe(request):
    tab = Dht.objects.all()
    s3 = {'tab': tab}
    return render(request, 'listing-page.html', s3)

def historique(request):
    tab = Dht.objects.all()
    s4 = {'tab': tab}
    return render(request, 'historique.html', s4)

def export_xls24h(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Dht24h.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Dht')
    data = []
    labels = []
    alldata = []
    queryset = Dht.objects.all()[0:10]
    for i in queryset:
        data.append(str(i.temp))
        labels.append(str(i.dt.strftime("%Y-%m-%d %H:%M")))
        alldata.append((i.temp, str(i.dt.strftime("%Y-%m-%d %H:%M"))))

    DATE = labels
    TEMP = data
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Temperatures', 'Dates', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = alldata
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
def export_xls48h(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Dht28h.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Dht')
    data = []
    labels = []
    alldata = []
    queryset = Dht.objects.all()[0:20]
    for i in queryset:
        data.append(str(i.temp))
        labels.append(str(i.dt.strftime("%Y-%m-%d %H:%M")))
        alldata.append((i.temp, str(i.dt.strftime("%Y-%m-%d %H:%M"))))

    DATE = labels
    TEMP = data
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Temperatures', 'Dates', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = alldata
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response
def export_xlsweek(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Dhtweek.xls"'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Dht')
    data = []
    labels = []
    alldata = []
    queryset = Dht.objects.all()
    for i in queryset:
        data.append(str(i.temp))
        labels.append(str(i.dt.strftime("%Y-%m-%d %H:%M")))
        alldata.append((i.temp, str(i.dt.strftime("%Y-%m-%d %H:%M"))))

    DATE = labels
    TEMP = data
    # Sheet header, first row
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    columns = ['Temperatures', 'Dates', ]
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = alldata
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)
    return response