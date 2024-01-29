"""
Role2 Module

This module defines the data and logic associated with the role in the adventure game.
Each role has attributes such as Strength, Dexterity, Intelligence, and Health.

Functions:
- initialize_role(): Sets initial values for role attributes.
- get_attribute_value(attribute): Retrieves the current value of a specific attribute for the role.
"""
# Role2.py
import random

def initialize_role():
    # Create a dictionary to store attributes
    role = {
        'name': 'Role2',
        'strength': 1,
        'dexterity': 1,
        'intelligence': 1,
        'health': 1
    }

    return role
