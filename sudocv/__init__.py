__version__ = '0.1.0'

import click

#from document import Doc
from collector import Collector
from document import Doc
from getpass import getpass

@click.command()
@click.option('--username', default=None, help='Output file')
@click.option('--password', default=None, help='Passworrd')
@click.option('--output', default='output.docx', help='Output file (output.docx)')
def main(username, password, output):
    if username == None:
        username = input('Github Username: ')
    
    if password == None:
        password = getpass('Github Password: ')
    
    gh = Collector(username, password)
    docx = Doc(gh)
    docx.save(output)
    
if __name__ == '__main__':
    main()
    