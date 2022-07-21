from django.shortcuts import render

projectlist = [
    {
        'id': '1',
        'title': 'Ecommerce Website',
        'description': 'Fully functional ecommerce website',
    },
    {
        'id': '2',
        'title': 'Portfolio Website',
        'description': 'This was a project where I built out my portfol',

    },
    {
        'id': '3',
        'title': 'Social Network',
        'description': 'Awesome open source project I am still working',
    },
]


def projects(request):
    page = 'projects'
    num = 10
    context = {'page': page, 'number': num, 'projectlist': projectlist}
    return render(request, 'projects/project.html', context)


def project(request, pk):
    projectObj = None
    for i in projectlist:
        if i['id'] == pk:
            projectObj = i
    return render(request, 'projects/single project.html', {'project': projectObj})