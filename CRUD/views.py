from django.shortcuts import render, redirect
from website import model


def read(request):
    data = model.Enquiry.object.all()
    context = {'data': data}
    return render(request, 'read.html', context)


def delete(request, pk):
    data = model.Enquiry.object.get(pk=pk)
    data.delete()
    return redirect('read')
