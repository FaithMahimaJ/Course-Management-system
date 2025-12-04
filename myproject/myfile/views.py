from django.shortcuts import render,HttpResponse

# Create your views here.
days={
    'monday':'go to college',
    'tuesday':'go to church',
    'wednesday':'go to temple',
    'thursday':'go to movie',
    'friday':'go to park',
    'saturday':'go to beach',
    'sunday':'nothing.. just sleep'
}
def day(request):
    return HttpResponse('Welcome Everyone!!!')

def weekday(request,day):
    return HttpResponse({days.get(day.lower(),'invalid day')})