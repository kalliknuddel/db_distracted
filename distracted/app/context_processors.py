from distracted.models import Series, Episode

def series_count(request):
    return {'series_count': Series.objects.count}

def series_data(request):
    return {'series_data': Series.objects.order_by('name')}
