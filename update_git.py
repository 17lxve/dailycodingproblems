from os import system as do
from os import chdir as cd
import pathlib

path = pathlib.Path(__file__).parent.resolve()
cd(path)
do('git add *')
message = input("Enter message: ")
do(f'git commit -m "{message}"')
do('git push -u origin main')

