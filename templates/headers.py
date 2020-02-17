import sys

# set project directory for shared library
PROJECT_DIR='/home/jovyan/work/amazon-review-validator'
if PROJECT_DIR not in sys.path:
    sys.path.insert(0, PROJECT_DIR)
    
from libs.utils import hello
hello()