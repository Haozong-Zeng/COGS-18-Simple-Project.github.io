
# coding: utf-8


import sys
sys.path.append('../')
from my_module.functions import *
import random

# Test the dictionary
for key in OrbDictionary:
	assert isinstance(OrbDictionary[key].name, str)
	assert isinstance(OrbDictionary[key].orb_level, int)
	assert isinstance(OrbDictionary[key].orb_type, str)
	assert isinstance(OrbDictionary[key].buff_type, str)
	assert isinstance(OrbDictionary[key].weapon_type, list)

# Empty entries
assert Comparason(Spell_1='', Spell_2='', Weapon_Type='Normal') == 'Please input the name of the first spell. Please input the name of the second spell. '

#Test the comparason function
lis=['Normal','Missile','Missile-Splash','Missile-Bounce', 'Artillery', 'Instant', 'Missile-Line', 'Artillery-Line']
for key_1, key_2 in zip(OrbDictionary, OrbDictionary):
	assert isinstance(Comparason(Spell_1=key_1, Spell_2=key_2, Weapon_Type=random.sample(lis, 1), str)
	assert Comparason(Spell_1=key_1, Spell_2=key_2, Weapon_Type=random.sample(lis, 1)) != None
