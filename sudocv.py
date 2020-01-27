# -*- coding: utf-8 -*-
__version__ = '0.1.0'

import click

#from document import Doc
from lib.collector import Collector
from lib.document import Doc
from getpass import getpass
from github import GithubException


@click.command()
@click.option('--username', default=None, help='Output file')
@click.option('--password', default=None, help='Password')
@click.option('--output', default='output.docx', help='Output file (output.docx)')
def main(username, password, output):
    if username == None:
        username = input('Github Username: ')
    
    if password == None:
        password = getpass('Github Password: ')
    
    try:
        gh = Collector(username, password)
        docx = Doc(gh)
        docx.save(output)
    except GithubException as Error:
        print(Error.args[1]['message'])
    except Exception:
        print('An error occured while generating report.')

if __name__ == '__main__':
    main()
    