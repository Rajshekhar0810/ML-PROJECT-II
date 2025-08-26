#"stup.py tells setuptools (or sometimes distutils) how to package, distribute, and install your project."

from setuptools import setup, find_packages
from typing import List #typing is a standard Python module (since Python 3.5)
#It provides type hints for Python code → so you can tell other developers (and tools like linters, IDEs, mypy) what kind of data your functions, variables, or classes expect.

def get_requirements()->List[str]:
    """
    This function will return list of requirements
    """
    requirement_lst: List[str] = []
    try:
        with open("requirements.txt") as file:     #In requirements.txt, everything you write is just plain text strings (one per line)
            #Read all lines from the file
            lines = file.readlines()               #In requirements.txt, everything you write is just plain text strings (one per line).["pandas\n", "numpy==1.26.4\n", "scikit-learn>=1.2\n", "torch!=2.0.1\n"]
            #Process each line
            for line in lines:
                requirement = line.strip()          #After applying strip():["pandas", "numpy==1.26.4", "scikit-learn>=1.2", "torch!=2.0.1"]
                # ignore empty lines and -e .
                if requirement and requirement != '-e .':      #Note: Here requirement is a single string not  list of string."pandas\n"->"pandas","numpy\n"->"numpy","/n"->""(empty string)
                       requirement_lst.append(requirement)      #In Python, empty strings are "Falsy" and Any non-empty string is "Truthy",So if requirement: automatically ignores empty strings

    except FileNotFoundError:
        print("requirements.txt file not found.")

    return requirement_lst

setup(
     name = "Network Security",
     version = "0.0.1",
     author = "Raj shekhar",
     author_email= "rajshekhar0810@gmail.com",
     packages = find_packages(),  #find_packages() automatically discovers all packages and sub-packages
     install_requires = get_requirements(),  #This will call the function get_requirements() and assign its return value to install_requires

)














#from typing import List, Dict, Tuple, Set,Literal, Final, TypedDict
# List[int]          # list of integers
# Dict[str, int]     # dict with string keys and int values
# Tuple[str, int]    # tuple of (string, integer)
# Set[float]         # set of floats
# Literal["red", "blue", "green"]  # only one of these strings allowed
#   (class User(TypedDict):           # dict with fixed keys
#        id: int
#        name: str     )

#  ( def add(a: int, b: int) -> int:
#           return a + b              )
# a: int → parameter a should be an integer, b: int → parameter b should be an integer
# -> int → the function is expected to return an integer
# So, the whole signature means:“add takes two integers and returns an integer.”
