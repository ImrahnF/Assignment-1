"""
Role1 Module

This module defines the data and logic associated with the role in the adventure game.
Each role has attributes such as Strength, Dexterity, Intelligence, and Health.

Functions:
- initialize_role(): Sets initial values for role attributes.
"""
# Role1.py
import random

def initialize_role():
    # Create a dictionary to store attributes
    role = {
        'name': 'Barbarian',
        'strength': 2,
        'dexterity': -2,
        'intelligence': 0,
        'luck': 0
    }

    return role