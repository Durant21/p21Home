from pyramid.config import Configurator
from pyramid.events import NewRequest

from pyramid.renderers import JSON

# Following references needed for Sqlite creation
from proto21_home.data.Car import Car
from proto21_home.data.People import Person
from proto21_home.data.Event import Event
from proto21_home.data.db_factory import DbSessionFactory
from proto21_home.renderers.csv_renderer import CSVRendererFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')

    allow_cors( config )
    init_db( config )
    configure_renderers( config )

    config.add_static_view('static', '/static', cache_max_age=3600)
    config.add_static_view( 'scripts', 'static/scripts' )
    config.add_static_view( 'images', 'static/images' )
    config.add_route('home', '/')
    config.add_route('blog','/blog')
    config.add_route( 'gis', '/gis' )
    config.add_route( 'iMii', '/iMii' )
    config.add_route( 'pythonwebdevelopment', '/pythonwebdevelopment' )

    config.add_route( 'MiningCycle', '/MiningCycle' )
    config.add_route( 'TeacherResources', '/TeacherResources' )
    config.add_route( 'ParticipatingOrganizations', '/ParticipatingOrganizations' )
    config.add_route( 'NewsEvents', '/NewsEvents' )
    config.add_route( 'About', '/About' )
    config.add_route( 'Discover', '/Discover' )
    config.add_route( 'Plan', '/Plan' )
    config.add_route( 'People', '/People' )
    config.add_route( 'Curricula', '/Curricula' )
    config.add_route( 'Mine', '/Mine' )
    config.add_route( 'Reclaim', '/Reclaim' )
    config.add_route( 'CareerPathways', '/CareerPathways' )
    config.add_route( 'ContactUs', '/ContactUs' )
    config.add_route( 'iMiiMasterHeader1', '/iMiiMasterHeader1' )
    config.add_route( 'iMiiMasterFooter1', '/iMiiMasterFooter1' )
    config.add_route( 'store_img1_view', '/store_img1_view' )  # http://localhost:6543/store_img1_view
    config.add_route( 'store_img2_view', '/store_img2_view' )


    # register_routes( config )

    config.add_route( 'autos_api', '/api/autos' )
    config.add_route( 'auto_api', '/api/auto/{car_id}' )

    config.add_route( 'people_api', '/api/people' )
    config.add_route( 'person_api', '/api/people/{person_id}' )

    config.add_route( 'events_api', '/api/events' )
    config.add_route( 'event_api', '/api/event/{event_id}' )



    config.scan()

    return config.make_wsgi_app()


def init_db(config):
    settings = config.get_settings()
    db_file = settings.get('db_filename')

    DbSessionFactory.global_init(db_file)


def register_routes(config):
    # config.add_static_view( 'static', 'static', cache_max_age=3600 )
    # config.add_route( 'home', '/' )
    # config.add_route( 'people', '/People' )
    # config.add_route( 'events', '/Events' )
    # config.add_route( 'test', '/test' )
    # config.add_route( 'generate_table', '/generate_table' )

    config.add_route( 'autos_api', '/api/autos' )
    config.add_route( 'auto_api', '/api/auto/{car_id}' )

    config.add_route( 'people_api', '/api/people' )
    config.add_route( 'person_api', '/api/people/{person_id}' )

    config.add_route( 'events_api', '/api/events' )
    config.add_route( 'event_api', '/api/event/{event_id}' )



    # config.add_route( 'iMiiMasterHeader1', '/iMiiMasterHeader1' )
    # config.add_route( 'iMiiMasterFooter1', '/iMiiMasterFooter1' )
    # config.scan()


def allow_cors(config):
    def add_cors_headers_response_callback(event):
        def cors_headers(_, response):
            response.headers.update({
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Methods': 'POST,GET,DELETE,PUT,OPTIONS',
                'Access-Control-Allow-Headers': 'Origin, Content-Type, Accept, Authorization',
                'Access-Control-Allow-Credentials': 'true',
                'Access-Control-Max-Age': '1728000',
            })

        event.request.add_response_callback(cors_headers)

    config.add_subscriber(add_cors_headers_response_callback, NewRequest)


def configure_renderers(config):
    json_renderer = JSON(indent=4)
    json_renderer.add_adapter(Car, lambda c, _: c.to_dict())
    json_renderer.add_adapter(Person, lambda p, _: p.to_dict() )
    json_renderer.add_adapter(Event, lambda e, _: e.to_dict() )
    config.add_renderer('json', json_renderer)

    csv_renderer = CSVRendererFactory()
    csv_renderer.add_adapter(Car, lambda c, _: c.to_dict())
    config.add_renderer('csv', csv_renderer)
