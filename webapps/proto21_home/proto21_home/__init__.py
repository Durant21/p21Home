from pyramid.config import Configurator
from pyramid.events import NewRequest

from pyramid.renderers import JSON

# Following references needed for Sqlite creation
from proto21_home.data.Car import Car
from proto21_home.data.People import Person
from proto21_home.data.Event import Event
from proto21_home.data.User import User
from proto21_home.data.db_factory import DbSessionFactory
from proto21_home.renderers.csv_renderer import CSVRendererFactory
from proto21_home.data.repository import Repository

import os
import sys

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """

    # import logging
    # logging.basicConfig( filename='example.log', level=logging.DEBUG )
    # logging.debug( 'This message should go to the log file' )
    # logging.info( 'So should this' )
    # logging.warning( 'And this, too' )

    # new_path = 'init1.txt'
    # new_days = open( new_path, 'w' )
    # new_days.write('test2')
    #
    # f = open( "/Users/dantefernandez/Projects/Proto21/webapps/proto21_home/proto21_home/logs/guru97.txt", "w+" )
    # for i in range( 10 ):
    #     f.write( "This is line %d\r\n" % (i + 1) )
    # logger.handlers  # you should have one FileHandler object

    config = Configurator(settings=settings)
    config.include('pyramid_chameleon')

    allow_cors( config )
    init_db( config )
    configure_renderers( config )

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_static_view( 'scripts', 'static/scripts' )
    config.add_static_view( 'images', 'static/images' )
    config.add_static_view( 'graphics', 'static/graphics' )
    config.add_route('home', '/')
    config.add_route('blog','/blog')
    config.add_route( 'gis', '/gis' )
    config.add_route( 'iMii', '/iMii' )
    config.add_route( 'about_author', '/about_author' )
    config.add_route( 'pythonwebdevelopment', '/pythonwebdevelopment' )
    config.add_route( 'restfulservices', '/restfulservices' )
    config.add_route( 'sqliteDB', '/sqliteDB' )

    config.add_route( 'MiningCycle', '/MiningCycle' )
    config.add_route( 'TeacherResources', '/TeacherResources' )
    config.add_route( 'ParticipatingOrganizations', '/ParticipatingOrganizations' )
    config.add_route( 'OurProjects', '/OurProjects' )
    config.add_route( 'WomenInMining', '/WomenInMining' )
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
    config.add_route( 'store_img3_view', '/store_img3_view' )


    # register_routes( config )

    config.add_route( 'autos_api', '/api/autos' )
    config.add_route( 'auto_api', '/api/auto/{car_id}' )

    config.add_route( 'people_api', '/api/people' )
    config.add_route( 'people_interviewed_api', '/api/people/{interviewed}' )
    config.add_route( 'person_api', '/api/person/{person_id}' )

    config.add_route( 'events_api', '/api/events' )
    config.add_route( 'event_api', '/api/event/{event_id}' )

    config.add_route('login_api','/api/login')



    config.scan()

    return config.make_wsgi_app()


def init_db(config):
    settings = config.get_settings()
    db_file = settings.get('db_filename')

    DbSessionFactory.global_init(db_file)
    # Repository.create_user('jeff')
    # Repository.create_user( 'chloe' )
    # Repository.create_user( 'sarah' )
    # Repository.create_user( 'mike' )
    # Repository.create_user( 'Debra' )
    # Repository.create_user( 'Dante' )
    # Repository.create_user( 'Laura' )
    # Repository.create_user( 'Chad' )
    # Repository.create_user( 'Jon' )
    # Repository.create_user( 'Joan' )
    # Repository.create_user( 'Admin' )



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
    # csv_renderer.add_adapter(Person, lambda p, _: p.to_dict() )
    config.add_renderer('csv', csv_renderer)
