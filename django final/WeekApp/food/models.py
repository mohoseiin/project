from django.db import models

type = {
    'صبحانه',
    'ناهار',
    'شام',
}
day = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30}
month = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}
year = {1400, 1401, 1402, 1403, 1404, 1405, 1406, 1407, 1408, 1409, 1410, 1411, 1412, 1413, 1414, 1415, 1416, 1417, 1418, 1419, 1420, 1421, 1422, 1423, 1424, 1425, 1426, 1427, 1428, 1429, 1430, 1431, 1432, 1433, 1434, 1435, 1436, 1437, 1438, 1439, 1440, 1441, 1442, 1443, 1444, 1445, 1446, 1447, 1448, 1449}
typework = {
    'کیلوگرم',
    'لیتر',
    'گرم',
    'قاشق غذا خوری'
}

def get_mellll(a):
    if a == 1:
        return {i: i for i in type}
    elif a == 2:
        return {i: i for i in day}
    elif a == 3:
        return {i: i for i in month}
    elif a == 4:
        return {i: i for i in year}
    else:
        return {i: i for i in typework}

class material(models.Model):
    name = models.CharField(max_length=100)
    count = models.IntegerField()
    typework = models.CharField(max_length=100,choices=get_mellll(5))
    url = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id} {self.name} {self.count} {self.typework} {self.url}"
    
class reqq(models.Model):
    count = models.IntegerField()
    material = models.ForeignKey(material, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.id} {self.count} {self.material}"

class food(models.Model):
    name = models.CharField(max_length=100)
    persons = models.IntegerField()
    reqqs = models.ManyToManyField(reqq, through='foodreqq')

    def __str__(self):
        return f"{self.name , self.persons}"

class foodreqq(models.Model):
    reqq = models.ForeignKey(reqq, on_delete=models.CASCADE)
    food = models.ForeignKey(food, on_delete=models.CASCADE)

class week(models.Model):
    day = models.IntegerField(choices=get_mellll(2))
    month = models.IntegerField(choices=get_mellll(3))
    year = models.IntegerField(choices=get_mellll(4))
    type = models.CharField(max_length=100,choices=get_mellll(1))
    food = models.ForeignKey(food, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.type} {self.year} {self.month} {self.day} {self.status}"

class buylist(models.Model):
    s_day = models.IntegerField(choices=get_mellll(2))
    s_month = models.IntegerField(choices=get_mellll(3))
    s_year = models.IntegerField(choices=get_mellll(4))
    e_day = models.IntegerField(choices=get_mellll(2))
    e_month = models.IntegerField(choices=get_mellll(3))
    e_year = models.IntegerField(choices=get_mellll(4))
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.id} {self.s_day} {self.s_month} {self.s_year} {self.e_day} {self.e_month} {self.e_year} {self.status}"

class buylistmaterial(models.Model):
    buylist = models.ForeignKey(reqq, on_delete=models.CASCADE)
    material = models.ForeignKey(food, on_delete=models.CASCADE)