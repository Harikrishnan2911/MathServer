from django.shortcuts import render
def mileage_calc(request):
    d = int(request.POST.get('distance', 0))
    f = int(request.POST.get('liters', 0))
    mileage = d / f if request.method == 'POST' and f != 0 else 0
    print("kilometers =", d)
    print("liters =", f)
    print("Mileage =", mileage)
    return render(request, 'mathapp/math.html', {'d': d, 'f': f, 'mileage': mileage})