'''
Role1.py is the first role. It simply contains the hardcoded values, and the sum of all attributes equate to roughly 0 to keep it fair.

initialize_role()
- pretty much returns the role to allow the user to use it
'''
def initialize_role():
    # Create a dictionary to store attributes
    role = {
        'name': 'Jock',
        'strength': 2,
        'dexterity': -1,
        'intelligence': -2,
        'luck': 1
    }

    return role