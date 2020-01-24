__version__ = '0.1.0'

import click

#from document import Doc
from collector import Collector
from document import Doc

@click.command()
@click.option('--test', default=1, help='Test command')
def main(test):
    gh = Collector('jabernardo', 'ca64613debbd02eb13ade603bcc48b8396583722')
    docx = Doc(gh)
    docx.save('output.docx')
    
#    print(gh.getName())
#    
#    for repo in gh.getRepositories():
#        print(repo.language)
    
if __name__ == '__main__':
    main()
    