from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'Home'}

@view_config(route_name='blog', renderer='templates/blog.pt')
def my_view1(request):
    return {'project': 'blog'}

@view_config(route_name='gis', renderer='templates/gis.pt')
def my_view2(request):
    return {'project': 'gis'}

@view_config(route_name='iMii', renderer='templates/iMii.pt')
def my_view3(request):
    return {'project': 'iMii'}

@view_config(route_name='MiningCycle', renderer='templates/MiningCycle.pt')
def my_view4a(request):
    return {'project': 'MiningCycle'}

@view_config(route_name='TeacherResources', renderer='templates/TeacherResources.pt')
def my_view4b(request):
    return {'project': 'TeacherResources'}

@view_config(route_name='NewsEvents', renderer='templates/NewsEvents.pt')
def my_view4c(request):
    return {'project': 'NewsEvents'}

@view_config(route_name='Discover', renderer='templates/Discover.pt')
def my_view4(request):
    return {'project': 'Discover'}

@view_config(route_name='Plan', renderer='templates/Plan.pt')
def my_view5(request):
    return {'project': 'Plan'}

@view_config(route_name='People', renderer='templates/People.pt')
def my_view6(request):
    return {'project': 'People'}

@view_config(route_name='Curricula', renderer='templates/Curricula.pt')
def my_view7(request):
    return {'project': 'Curricula'}

@view_config(route_name='Mine', renderer='templates/Mine.pt')
def my_view8(request):
    return {'project': 'Mine'}

@view_config(route_name='Reclaim', renderer='templates/Reclaim.pt')
def my_view9(request):
    return {'project': 'Reclaim'}

@view_config(route_name='pythonwebdevelopment', renderer='templates/pythonwebdevelopment.pt')
def my_view10(request):
    return {'project': 'pythonwebdevelopment'}
