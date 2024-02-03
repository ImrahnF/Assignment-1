"""
Role2 Module

This module defines the data and logic associated with the role in the adventure game.
Each role has attributes such as Strength, Dexterity, Intelligence, and Health.

Functions:
- initialize_role(): Sets initial values for role attributes.
"""
# Role2.py
import random

def initialize_role():
    # Create a dictionary to store attributes
    role = {
        'name': 'Wizard',
        'strength': 1,
        'dexterity': 1,
        'intelligence': 1,
        'luck': 2
    }

    return role
