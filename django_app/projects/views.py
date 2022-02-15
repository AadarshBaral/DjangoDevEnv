from turtle import title
from django.shortcuts import render
from django.http import HttpResponse

projectsList = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website'
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'A personal website to write articles and display work'
    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'An open source project built by the community'
    }
]


def projects(request):
    msg = "Hello you are in the project page"
    number = 11

    context = {'msg':msg , 'number' : number,'projects' : projectsList}
    return render(request,'projects/projects.html',context)


def project(request,pk):
    projObj = None
    for i in projectsList:
        if i['id'] == pk:
            projObj = i

        
    return render(request,'projects/single_project.html',{'projects' : projObj})