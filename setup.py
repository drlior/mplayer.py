from distutils.core import setup

setup (
	name='PyMPlayer',
	version='20070818',
	description='MPlayer wrapper for Python',
	author='Darwin Bautista',
	author_email='djclue917@gmail.com',
	url='http://bbs.eee.upd.edu.ph/',
	license='GPL3',
	py_modules=['pymplayer'],
	scripts=['server.py', 'client.py']
)