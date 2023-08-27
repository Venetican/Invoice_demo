from pathlib import Path
import sys

DIRECTORY_PATH = Path('C:/Users/Danie/Desktop/Projekty/invoice_test/config/config.py')
from config import settings
class PrePro:
    def __init__(self,var):
        self.var = var 
    
    def append_path(self):
        sys.path()

for x in sys.path