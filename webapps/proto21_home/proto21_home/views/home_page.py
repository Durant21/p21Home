from pyramid.view import view_config

import os
import uuid
import shutil
from pyramid.response import Response
import sqlite3

from proto21_home.common.logfile import w


@view_config(route_name='home', renderer='proto21_home:templates/mytemplate.pt')
def my_view(request):
    return {'project': 'Home'}


@view_config(route_name='blog', renderer='proto21_home:templates/blog.pt')
def my_view1(request):
    return {'project': 'blog'}


@view_config(route_name='gis', renderer='proto21_home:templates/gis.pt')
def my_view2(request):
    return {'project': 'gis'}


@view_config(route_name='iMii', renderer='proto21_home:templates/iMii.pt')
def my_view3(request):
    return {'project': 'iMii'}


@view_config(route_name='MiningCycle', renderer='proto21_home:templates/MiningCycle.pt')
def my_view4a(request):
    return {'project': 'MiningCycle'}


@view_config(route_name='TeacherResources', renderer='proto21_home:templates/TeacherResources.pt')
def my_view4b(request):
    return {'project': 'TeacherResources'}


@view_config(route_name='NewsEvents', renderer='proto21_home:templates/NewsEvents.pt')
def my_view4c(request):
    return {'project': 'NewsEvents'}


@view_config(route_name='Discover', renderer='proto21_home:templates/Discover.pt')
def my_view4(request):
    return {'project': 'Discover'}


@view_config(route_name='Plan', renderer='proto21_home:templates/Plan.pt')
def my_view5(request):
    return {'project': 'Plan'}


@view_config(route_name='People', renderer='proto21_home:templates/People.pt')
def my_view6(request):
    return {'project': 'People'}


@view_config(route_name='Curricula', renderer='proto21_home:templates/Curricula.pt')
def my_view7(request):
    return {'project': 'Curricula'}


@view_config(route_name='Mine', renderer='proto21_home:templates/Mine.pt')
def my_view8(request):
    return {'project': 'Mine'}


@view_config(route_name='Reclaim', renderer='proto21_home:templates/Reclaim.pt')
def my_view9(request):
    return {'project': 'Reclaim'}


@view_config(route_name='About', renderer='proto21_home:templates/About.pt')
def my_view9a(request):
    return {'project': 'About'}


@view_config(route_name='pythonwebdevelopment', renderer='proto21_home:templates/pythonwebdevelopment.pt')
def my_view10(request):
    return {'project': 'pythonwebdevelopment'}


@view_config(route_name='ParticipatingOrganizations', renderer='proto21_home:templates/ParticipatingOrganizations.pt')
def my_view11(request):
    return {'project': 'ParticipatingOrganizations'}


@view_config(route_name='CareerPathways', renderer='proto21_home:templates/CareerPathways.pt')
def my_view12(request):
    return {'project': 'CareerPathways'}


@view_config(route_name='ContactUs', renderer='proto21_home:templates/ContactUs.pt')
def my_view13(request):
    return {'project': 'ContactUs'}


@view_config(route_name='iMiiMasterHeader1', renderer='proto21_home:templates/iMiiMasterHeader1.pt')
def my_view14(request):
    return {'project': 'iMiiMasterHeader1'}


@view_config(route_name='iMiiMasterFooter1', renderer='proto21_home:templates/iMiiMasterFooter1.pt')
def my_view15(request):
    return {'project': 'iMiiMasterFooter1'}


# @view_config(route_name='store_img1_view', renderer='templates/fileUpload.pt')
@view_config(route_name='store_img1_view', renderer='proto21_home:templates/People.pt',
             request_method='POST')
def my_view16(request):
    store_img1_view(request)
    return {'project': 'People'}


def store_img1_view(request):
    # src:  https://docs.pylonsproject.org/projects/pyramid_cookbook/en/latest/forms/file_uploads.html

    try:

        w('store_img1_view()')

        # ``filename`` contains the name of the file in string format.
        #
        # WARNING: this example does not deal with the fact that IE sends an
        # absolute file *path* as the filename.  This example is naive; it
        # trusts user input.

        filename = request.POST['img1'].filename

        # ``input_file`` contains the actual file data which needs to be
        # stored somewhere.

        input_file = request.POST['img1'].file

        img_id = request.POST['img_id']

        # Note that we are generating our own filename instead of trusting
        # the incoming filename since that might result in insecure paths.
        # Please note that in a real application you would not use /tmp,
        # and if you write to an untrusted location you will need to do
        # some extra work to prevent symlink attacks.
        settings = request.registry.settings
        sRelativePath = settings.get( 'img_path' )
        w('sRelativePath: ' + sRelativePath)

        # print( 'path: {0}'.format( img_path ) )
        # sRelativePath = os.getcwd()
        # print( 'path: {0}'.format( sRelativePath ) )

        # file_path = os.path.join('~/tmp', '%s.mp3' % uuid.uuid4())
        # file_path = os.path.join( '/Users/dantefernandez/Projects/PythonScripts/FileUpload/prjFileUpload/prjFileUpload/tmp', '%s.jpg' % uuid.uuid4() )
        file_path = os.path.join( sRelativePath + '/images/', '%s.jpg' % uuid.uuid4() )


        # We first write to a temporary file to prevent incomplete files from
        # being used.

        temp_file_path = file_path + '~'

        # Finally write the data to a temporary file
        input_file.seek(0)
        with open(temp_file_path, 'wb') as output_file:
            shutil.copyfileobj(input_file, output_file)

        # Now that we know the file has been fully saved to disk move it into place.

        os.rename(temp_file_path, file_path)
        sBaseFileName = os.path.basename( file_path )

        # TODO: "create insert statement for People images"
        sDBPath = settings.get( 'db_path' )
        w('sDBPath: ' + sDBPath)
        db = sqlite3.connect( sDBPath + '/iMii_v3.sqlite' )
        cursor = db.cursor()
        # cursor.execute( '''SELECT * FROM People''' )
        # user1 = cursor.fetchone()  # retrieve the first row
        # print('people: ' + user1[0] )  # Print the first column retrieved(user's name)
        cursor.execute('''UPDATE People SET img1 = ? WHERE id = ?''',(sBaseFileName,img_id))
        db.commit()  # Commit the change
        return Response('OK')
    except OSError as err:
        w("error: store_img1_view - " + err)


@view_config(route_name='store_img2_view', renderer='proto21_home:templates/NewsEvents.pt',
             request_method='POST')
def my_view17(request):
    store_img2_view(request)
    return {'project': 'NewsEvents'}


def store_img2_view(request):
    # src:  https://docs.pylonsproject.org/projects/pyramid_cookbook/en/latest/forms/file_uploads.html

    # ``filename`` contains the name of the file in string format.
    #
    # WARNING: this example does not deal with the fact that IE sends an
    # absolute file *path* as the filename.  This example is naive; it
    # trusts user input.

    filename = request.POST['img1'].filename

    # ``input_file`` contains the actual file data which needs to be
    # stored somewhere.

    input_file = request.POST['img1'].file

    img_id = request.POST['img_id']

    # Note that we are generating our own filename instead of trusting
    # the incoming filename since that might result in insecure paths.
    # Please note that in a real application you would not use /tmp,
    # and if you write to an untrusted location you will need to do
    # some extra work to prevent symlink attacks.
    settings = request.registry.settings
    sRelativePath = settings.get( 'img_path' )

    # print( 'path: {0}'.format( img_path ) )
    # sRelativePath = os.getcwd()
    print( 'path: {0}'.format( sRelativePath ) )

    # file_path = os.path.join('~/tmp', '%s.mp3' % uuid.uuid4())
    # file_path = os.path.join( '/Users/dantefernandez/Projects/PythonScripts/FileUpload/prjFileUpload/prjFileUpload/tmp', '%s.jpg' % uuid.uuid4() )
    file_path = os.path.join( sRelativePath + '/images/', '%s.jpg' % uuid.uuid4() )


    # We first write to a temporary file to prevent incomplete files from
    # being used.

    temp_file_path = file_path + '~'

    # Finally write the data to a temporary file
    input_file.seek(0)
    with open(temp_file_path, 'wb') as output_file:
        shutil.copyfileobj(input_file, output_file)

    # Now that we know the file has been fully saved to disk move it into place.

    os.rename(temp_file_path, file_path)
    sBaseFileName = os.path.basename( file_path )
    # TODO: "create insert statement for People images"
    db = sqlite3.connect( '/Users/dantefernandez/Projects/Proto21/webapps/proto21_home/proto21_home/db/iMii_v3.sqlite' )
    cursor = db.cursor()

    cursor.execute('''UPDATE Events SET img1 = ? WHERE id = ?''',(sBaseFileName,img_id))
    db.commit()  # Commit the change

    # # src:  https://docs.pylonsproject.org/projects/pyramid_cookbook/en/latest/forms/file_uploads.html
    #
    # # ``filename`` contains the name of the file in string format.
    # #
    # # WARNING: this example does not deal with the fact that IE sends an
    # # absolute file *path* as the filename.  This example is naive; it
    # # trusts user input.
    #
    # filename = request.POST['img1'].filename
    #
    # # ``input_file`` contains the actual file data which needs to be
    # # stored somewhere.
    #
    # input_file = request.POST['img1'].file
    #
    # # Note that we are generating our own filename instead of trusting
    # # the incoming filename since that might result in insecure paths.
    # # Please note that in a real application you would not use /tmp,
    # # and if you write to an untrusted location you will need to do
    # # some extra work to prevent symlink attacks.
    #
    # sRelativePath = os.getcwd()
    # print( 'path: {0}'.format( sRelativePath ) )
    #
    # # file_path = os.path.join('~/tmp', '%s.mp3' % uuid.uuid4())
    # # file_path = os.path.join( '/Users/dantefernandez/Projects/PythonScripts/FileUpload/prjFileUpload/prjFileUpload/tmp', '%s.jpg' % uuid.uuid4() )
    # file_path = os.path.join( sRelativePath + '/proto21_home/tmp', '%s.jpg' % uuid.uuid4() )
    #
    # # We first write to a temporary file to prevent incomplete files from
    # # being used.
    #
    # temp_file_path = file_path + '~'
    #
    # # Finally write the data to a temporary file
    # input_file.seek( 0 )
    # with open( temp_file_path, 'wb' ) as output_file:
    #     shutil.copyfileobj( input_file, output_file )
    #
    # # Now that we know the file has been fully saved to disk move it into place.
    #
    # os.rename( temp_file_path, file_path )

    # TODO: "create insert statement for Events images"
    return Response( 'OK' )
#
#
# @view_config(route_name='home', renderer='iMii_v3:templates/mytemplate.pt')
# def my_view(request):
#     return {'project': 'iMii_v3'}
#
#
# @view_config(route_name='people', renderer='iMii_v3:templates/people.pt')
# def people(request):
#     return {'project': 'iMii_v3'}
#
#
# @view_config(route_name='events', renderer='iMii_v3:templates/events.pt')
# def events(request):
#     return {'project': 'iMii_v3'}
#
#
# @view_config(route_name='test', renderer='iMii_v3:templates/test.pt')
# def test(request):
#     return {'project': 'iMii_v3'}
#
#
# @view_config(route_name='generate_table', renderer='iMii_v3:templates/generate_table.pt')
# def generate_table(request):
#     return {'project': 'iMii_v3'}