'''
Role2.py is the second role. It simply contains the hardcoded values, and the sum of all attributes equate to roughly 0 to keep it fair.

initialize_role()
- pretty much returns the role to allow the user to use it
'''
import random

def initialize_role():
    # Create a dictionary to store attributes
    role = {
        'name': 'Smarty Pants',
        'strength': -2,
        'dexterity': -2,
        'intelligence': 2,
        'luck': 2
    }

    return role
