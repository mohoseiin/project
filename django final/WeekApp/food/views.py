from django.shortcuts import redirect,render
from food.Converter import Nowweek
from .models import buylist, material, reqq, week,food


def foodview(request):
    data = Nowweek().getnow()
    database = [None,None,None,None,None,None,None]
    foods = food.objects.all().values_list('id','name')
    for x in range(7):
        database[x] = week.objects.filter(year=data[x][0] , month=data[x][1] , day=data[x][2] ,status=True).values_list('type','food')

    finaldata = [None,None,None,None,None,None,None]

    for x in range(7):

        sob = []
        nahar = []
        sham = []
        
        for y in database[x]:
            if y[0] == "صبحانه":
                for z in foods:
                    if z[0] == y[1]:
                        sob.append(z[1])
            if y[0] == "ناهار":
                for z in foods:
                    if z[0] == y[1]:
                        nahar.append(z[1])
            if y[0] == "شام":
                for z in foods:
                    if z[0] == y[1]:
                        sham.append(z[1])

        finaldata[x] = [sob , nahar , sham]
    
    return render(request, 'index.html', {
        'database' : finaldata,
        'day1' : data[0],
        'day2' : data[1],
        'day3' : data[2],
        'day4' : data[3],
        'day5' : data[4],
        'day6' : data[5],
        'day7' : data[6],
    })


# def searchweek(request, year, month, day):
#     time = timedelta(days=7)
#     return render(request, 'index.html', {'year': year, 'month': month, 'day': day})

def updatefood(request,id):
            
    weekdata = week.objects.filter(id=id).values()
    fooddata = food.objects.filter(id=weekdata[0]['food_id']).values()

    reqqs = reqq.objects.all()
    reqqdata = []
    for x in reqqs:
        data = food.objects.filter(foodreqq=x.id)
        for y in data:
            if y.id == weekdata[0]['food_id']:
                reqqdata.append(x)

    materialdata = []
    for x in reqqdata:
        data = material.objects.filter(id=x.material.id)
        materialdata.append(data)

    access = False
    status = []
    for x in reqqdata:
        for y in materialdata:
            for z in y:
                if x.material.id == z.id:
                    data = int(z.count) - (x.count)
                    if data < 0:
                        access = True
                    status.append((z.id,data))

    return render(request, 'updatefood.html', {'week': weekdata,'food':fooddata,'reqq': reqqdata,'material': materialdata,'status': status,'access' : access})

def accessupdatefood(request,id):

    weekdata = week.objects.filter(id=id).values()
    fooddata = food.objects.filter(id=weekdata[0]['food_id']).values()

    reqqs = reqq.objects.all()
    reqqdata = []
    for x in reqqs:
        data = food.objects.filter(foodreqq=x.id)
        for y in data:
            if y.id == weekdata[0]['food_id']:
                reqqdata.append(x)

    materialdata = []
    for x in reqqdata:
        data = material.objects.filter(id=x.material.id)
        materialdata.append(data)

    final = []
    for x in reqqdata:
        for y in materialdata:
            for z in y:
                if x.material.id == z.id:
                    data = int(z.count) - (x.count)
                    if data < 0:
                        access = True
                    final.append((z.id,data))
    for x in final:
        material.objects.filter(id=x[0]).update(count=x[1])

    week.objects.filter(id=id).update(status=True)

    return redirect('/admin/food/week/')

def buylistshow(request,id):
    buylistdata = buylist.objects.filter(id=id).values()

    startdate = str(buylistdata[0]['s_year']) +'-'+ str(buylistdata[0]['s_month']) +'-'+ str(buylistdata[0]['s_day'])
    enddate = str(buylistdata[0]['e_year']) +'-'+ str(buylistdata[0]['e_month']) +'-'+ str(buylistdata[0]['e_day'])

    listdate = Nowweek().listdate(buylistdata[0]['s_day'] ,buylistdata[0]['s_month'] ,buylistdata[0]['s_year'] ,buylistdata[0]['e_day'] ,buylistdata[0]['e_month'] ,buylistdata[0]['e_year'])
    
    final = []
    for x in listdate:
        dataw = week.objects.filter(year=x[0],month=x[1],day=x[2]).values()
        if not dataw:
            continue

        dataf = food.objects.filter(id=dataw[0]['food_id']).values()

        reqqs = reqq.objects.all()
        reqqdata = []
        for x in reqqs:
            data = food.objects.filter(foodreqq=x.id)
            for y in data:
                if y.id == dataw[0]['food_id']:
                    reqqdata.append(x)

        materialdata = []
        for x in reqqdata:
            data = material.objects.filter(id=x.material.id)
            materialdata.append(data)
        
        status = []
        for x in reqqdata:
            for y in materialdata:
                for z in y:
                    if x.material.id == z.id:
                        data = int(z.count) - (x.count)
                        if data < 0:
                            status.append((x.material.name,data,x.material.typework))
        if len(status) > 0:
            final.append(status)
        

    return render(request, 'buylist.html', {'id':id,'startdate':startdate ,'enddate':enddate , 'final' : final})

def accessbuylist(request,id):
    
    buylistdata = buylist.objects.filter(id=id).values()


    listdate = Nowweek().listdate(buylistdata[0]['s_day'] ,buylistdata[0]['s_month'] ,buylistdata[0]['s_year'] ,buylistdata[0]['e_day'] ,buylistdata[0]['e_month'] ,buylistdata[0]['e_year'])
    
    final = []
    for x in listdate:
        dataw = week.objects.filter(year=x[0],month=x[1],day=x[2]).values()
        if not dataw:
            continue

        dataf = food.objects.filter(id=dataw[0]['food_id']).values()

        reqqs = reqq.objects.all()
        reqqdata = []
        for x in reqqs:
            data = food.objects.filter(foodreqq=x.id)
            for y in data:
                if y.id == dataw[0]['food_id']:
                    reqqdata.append(x)

        materialdata = []
        for x in reqqdata:
            data = material.objects.filter(id=x.material.id)
            materialdata.append(data)
        
        status = []
        for x in reqqdata:
            for y in materialdata:
                for z in y:
                    if x.material.id == z.id:
                        data = int(z.count) - (x.count)
                        if data < 0:
                            material.objects.filter(id=x.material.id).update(count=(-data + x.material.count))
        buylistdata = buylist.objects.filter(id=id).update(status=True)



    return redirect('/admin/food/buylist/')