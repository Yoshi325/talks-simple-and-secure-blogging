import os
import sys
import shutil
import datetime

from invoke import task


INVOKE_CONFIG = {
    # Local path configuration (can be absolute or relative to tasks.py)
    'deploy_path': 'output',

    # Github Pages configuration
    'github_pages_branch': 'gh-pages',
    'commit_message': "':rocket: Publish site on {}'".format(datetime.date.today().isoformat()),

    # Port for `serve` task below
    'port': 8000,
}

@task
def clean(c):
    """Remove generated files"""
    if os.path.isdir(INVOKE_CONFIG['deploy_path']):
        shutil.rmtree(INVOKE_CONFIG['deploy_path'])
        os.makedirs(INVOKE_CONFIG['deploy_path'])

@task
def build(c):
    """Build local version of site"""
    c.run('pelican --settings pelicanconf.py')

@task
def rebuild(c):
    """`build` with the delete switch"""
    c.run('pelican --delete-output-directory --settings pelicanconf.py')

@task
def regenerate(c):
    """Automatically regenerate site upon file modification"""
    c.run('pelican --autoreload --settings pelicanconf.py')

@task
def serve(c):
    """Serve site locally"""

    from pelican.server import RootedHTTPServer
    from pelican.server import ComplexHTTPRequestHandler

    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        INVOKE_CONFIG['deploy_path'],
        ('', INVOKE_CONFIG['port']),
        ComplexHTTPRequestHandler,
    )

    sys.stderr.write('Serving on port {port} ...\n'.format_map(INVOKE_CONFIG))
    server.serve_forever()

@task
def publish(c):
    """Publish to GitHub Pages"""
    c.run('pelican --settings publishconf.py')
    c.run('ghp-import -b {github_pages_branch} -m {commit_message} {deploy_path} -p'.format_map(INVOKE_CONFIG))
