from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('blog','/blog')
    config.add_route( 'gis', '/gis' )
    config.add_route( 'iMii', '/iMii' )


    config.add_route( 'MiningCycle', '/MiningCycle' )
    config.add_route( 'TeacherResources', '/TeacherResources' )
    config.add_route( 'NewsEvents', '/NewsEvents' )

    config.add_route( 'Discover', '/Discover' )
    config.add_route( 'Plan', '/Plan' )
    config.add_route( 'People', '/People' )
    config.add_route( 'Curricula', '/Curricula' )
    config.add_route( 'Mine', '/Mine' )
    config.add_route( 'Reclaim', '/Reclaim' )
    config.scan()
    return config.make_wsgi_app()
