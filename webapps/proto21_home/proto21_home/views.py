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