# -*- coding: utf-8 -*-


# Create a class that contains the original Orb Effects and Buff Placers.
class OrbSpells():
	# orb_level represents the priority of that spell, orb_type can be 0 (no orb) or 1
	# buff_type can be 0 (no buff placer) or 1 (independent) or 2 (dependent)
	# attack_type is a list that contains all weapon types avaliable for the spell. 
	def __init__(self, name, orb_level, orb_type, buff_type, weapon_type):
		self.name = name
		self.orb_level = orb_level
		self.orb_type = orb_type
		self.buff_type = buff_type
		self.weapon_type = weapon_type


# Orbs
Barrage = OrbSpells(name='Barrage', orb_level=4, orb_type='法球', buff_type='独立类攻击特效', weapon_type=['Missile'])
FlakCannons = OrbSpells(name='Flak Cannons', orb_level=4, orb_type='', buff_type='独立类攻击特效', weapon_type=['Normal','Instant'])
EnvenomedSpears = OrbSpells(name='Envenomed Spears', orb_level=4, orb_type='法球', buff_type='独立攻击特效', weapon_type=['Normal','Instant','Missile'])
Pillage = OrbSpells(name='Pillage', orb_level=1, orb_type='类法球', buff_type='', weapon_type=['Normal','Missile-Line','Missile','Missile-Splash', 'Instant', 'Missile-Bounce', 'Artillery', 'Artillery-Line'])
BurningOil = OrbSpells(name='Burning Oil', orb_level=4, orb_type='法球', buff_type='独立攻击特效', weapon_type=['Missile','Missile-Splash','Artillery'])
LiquidFire = OrbSpells(name='Liquid Fire', orb_level=4, orb_type='', buff_type='独立攻击特效', weapon_type=['Missile','Missile-Splash'])
OrbOfAnnihilation = OrbSpells(name='Orb of Annihilation', orb_level=1, orb_type='法球', buff_type='', weapon_type=['Missile-Splash'])
FrostAttack = OrbSpells(name='Frost Attack', orb_level=5, orb_type='法球', buff_type='独立攻击特效', weapon_type=['Normal','Missile-Line','Missile','Missile-Splash', 'Instant', 'Missile-Bounce', 'Artillery', 'Artillery-Line'])
SlowPoison = OrbSpells(name='Slow Poison', orb_level=3, orb_type='法球', buff_type='独立攻击特效', weapon_type=['Normal','Missile','Instant'])
LightningAttack = OrbSpells(name='Lightning Attack', orb_level=5, orb_type='法球', buff_type='独立类攻击特效', weapon_type=['Normal','Missile-Line','Missile','Missile-Splash', 'Instant', 'Missile-Bounce', 'Artillery', 'Artillery-Line'])
SearingArrows = OrbSpells(name='Searing Arrows', orb_level=1, orb_type='法球', buff_type='', weapon_type=['Normal','Missile-Line','Missile','Missile-Splash', 'Instant', 'Missile-Bounce', 'Artillery', 'Artillery-Line'])
FrostArrows = OrbSpells(name='Frost Arrows', orb_level=1, orb_type='法球', buff_type='非独立攻击特效', weapon_type=['Missile','Missile-Splash'])
PoisonousArrows = OrbSpells(name='Poisonous Arrows', orb_level=1, orb_type='法球', buff_type='非独立攻击特效', weapon_type=['Missile','Missile-Splash'])
Demolish = OrbSpells(name='Demolish', orb_level=4, orb_type='类法球', buff_type='', weapon_type=['Normal','Missile-Line','Missile','Missile-Splash', 'Instant', 'Missile-Bounce', 'Artillery', 'Artillery-Line'])
Incinerate = OrbSpells(name='Incinerate', orb_level=1, orb_type='法球', buff_type='独立攻击特效', weapon_type=['Normal','Missile','Missile-Splash', 'Instant'])
MaskOfDeath = OrbSpells(name='Mask of Death', orb_level=2, orb_type='法球', buff_type='', weapon_type=['Normal','Missile-Line','Missile','Missile-Splash', 'Instant', 'Missile-Bounce', 'Artillery', 'Artillery-Line'])
OrbOfVenom = OrbSpells(name='Orb of Venom', orb_level=3, orb_type='法球', buff_type='非独立攻击特效', weapon_type=['Normal','Instant','Missile','Missile-Splash'])
OrbOfLightning = OrbSpells(name='Orb of Lightning', orb_level=3, orb_type='法球', buff_type='非独立攻击特效', weapon_type=['Normal','Instant','Missile','Missile-Splash'])
OrbOfDeceleration = OrbSpells(name='Orb of Deceleration', orb_level=3, orb_type='法球', buff_type='非独立攻击特效', weapon_type=['Normal','Instant','Missile','Missile-Splash'])
OrbOfCorruption = OrbSpells(name='Orb of Corruption', orb_level=3, orb_type='法球', buff_type='非独立攻击特效', weapon_type=['Normal','Instant','Missile','Missile-Splash'])
OrbOfFrost = OrbSpells(name='Orb of Frost', orb_level=3, orb_type='法球', buff_type='非独立攻击特效', weapon_type=['Normal','Instant','Missile','Missile-Splash'])
OrbOfFire = OrbSpells(name='Orb of Fire', orb_level=3, orb_type='法球', buff_type='非独立攻击特效', weapon_type=['Normal','Instant','Missile','Missile-Splash'])
OrbOfDarkness = OrbSpells(name='Orb of Darkness', orb_level=3, orb_type='法球', buff_type='非独立攻击特效', weapon_type=['Normal','Instant','Missile','Missile-Splash'])


# Special Cases
Bash_Normal = OrbSpells(name='Bash', orb_level=1, orb_type='类法球', buff_type='独立类攻击特效', weapon_type=['Normal','Instant'])
Bash_Missile = OrbSpells(name='Bash', orb_level=1, orb_type='类法球', buff_type='独立攻击特效', weapon_type=['Missile','Missile-Splash'])
CriticalStrike = OrbSpells(name='Critical Strike', orb_level=1, orb_type='类法球', buff_type='', weapon_type=['Normal','Missile-Line','Missile','Missile-Splash', 'Instant', 'Missile-Bounce', 'Artillery', 'Artillery-Line'])
CleavingAttack = OrbSpells(name='Cleaving Attack', orb_level=1, orb_type='', buff_type='独立类攻击特效', weapon_type=['Normal','Instant'])
DrunkenBrawler = OrbSpells(name='Drunken Brawler', orb_level=1, orb_type='类法球', buff_type='', weapon_type=['Normal','Missile-Line','Missile','Missile-Splash', 'Instant', 'Missile-Bounce', 'Artillery', 'Artillery-Line'])
Feedback_Normal = OrbSpells(name='Feedback', orb_level=4, orb_type='法球', buff_type='', weapon_type=['Normal','Instant'])
Feedback_Missile = OrbSpells(name='Feedback', orb_level=4, orb_type='法球', buff_type='非独立攻击特效', weapon_type=['Missile'])
FreezingBreath_Missile = OrbSpells(name='Freezing Breath', orb_level=4, orb_type='法球', buff_type='独立类攻击特效', weapon_type=['Missile'])
FreezingBreath_MissileSplash = OrbSpells(name='Freezing Breath', orb_level=4, orb_type='法球', buff_type='独立攻击特效', weapon_type=['Missile-Splash'])
BlackArrows_Missle = OrbSpells(name='Black Arrows', orb_level=1, orb_type='法球', buff_type='非独立攻击特效', weapon_type=['Missile'])
BlackArrows_Normal = OrbSpells(name='Black Arrows', orb_level=1, orb_type='', buff_type='独立类攻击特效', weapon_type=['Normal','Instant'])


# Create a dictionary that combine the Chinese inputs with the variable names
OrbDictionary = {'Barrage':Barrage, 'Flak Cannons':FlakCannons, 'Envenomed Spears':EnvenomedSpears, 'Pillage':Pillage, 'Burning Oil':BurningOil, \
'Liquid Fire':LiquidFire, 'Orb of Annihilation':OrbOfAnnihilation, 'Frost Attack':FrostAttack, 'Slow Poison':SlowPoison, \
'Lightning Attack':LightningAttack, 'Searing Arrows':SearingArrows, 'Frost Arrows':FrostArrows, 'Poisonous Arrows':PoisonousArrows, 'Demolish':Demolish, \
'Incinerate':Incinerate, 'Mask of Death':MaskOfDeath, 'Orb of Venom':OrbOfVenom, 'Orb of Lightning':OrbOfLightning, 'Orb of Deceleration':OrbOfDeceleration, 'Orb of Corruption':OrbOfCorruption, \
'Orb of Frost':OrbOfFrost, 'Orb of Fire':OrbOfFire, 'Orb of Darkness':OrbOfDarkness, 'Critical Strike':CriticalStrike, \
'Cleaving Attack':CleavingAttack, 'Drunken Brawler':DrunkenBrawler}



# These Orbs are similar to each other and need more exploration.
SimilarOrbs = [Bash_Normal, Bash_Missile, CriticalStrike, DrunkenBrawler]

# Each of these Orbs can perfectly adds up with the same spell.
AdditiveOrbs = [Demolish, CleavingAttack, FreezingBreath_Missile]

# These Orbs work differently under different conditions of the unit's weapon type.
SpecialCases = ['Bash', 'Feedback', 'Freezing Breath', 'Black Arrows']





def Comparason(Spell_1, Spell_2, Weapon_Type):
	SpellOne = None
	SpellTwo = None
	Answer = ''
	
	
	#Dealing with empty inputs
	if Spell_1 == '' or Spell_2 == '':
		if Spell_1 == '':
			Answer = Answer + 'Please input the name of the first spell. '
		if Spell_2 == '':
			Answer = Answer + 'Please input the name of the second spell. '
		return Answer
		
		
	# Check Spell 1 and get it's information
	if (Spell_1 in SpecialCases):
		if Spell_1 == 'Bash':
			if Weapon_Type in ['Normal','Instant']:
				SpellOne = Bash_Normal
			elif Weapon_Type in ['Missile','Missile-Splash']:
				SpellOne = Bash_Missile
			else: Answer = Answer + Spell_1 + ' does not work with this weapon type. '
		if Spell_1 == 'Feedback':
			if Weapon_Type in ['Normal','Instant']:
				SpellOne = Feedback_Normal
			elif Weapon_Type in ['Missile']:
				SpellOne = Feedback_Missile
			else: Answer = Answer + Spell_1 + ' does not work with this weapon type. '
		if Spell_1 == 'Freezing Breath':
			if Weapon_Type == 'Missile':
				SpellOne = FreezingBreath_Missile
			elif Weapon_Type == 'Missile-Splash':
				SpellOne = FreezingBreath_MissileSplash
			else: Answer = Answer + Spell_1 + ' does not work with this weapon type. '
		if Spell_1 == 'Black Arrows':
			if Weapon_Type == 'Missile':
				SpellOne = BlackArrows_Missle
			elif Weapon_Type in ['Normal','Instant']:
				SpellOne = BlackArrows_Normal
			else: Answer = Answer + Spell_1 + ' does not work with this weapon type. '
	
	elif (Spell_1 in OrbDictionary):
		SpellOne = OrbDictionary[Spell_1]
		if not (Weapon_Type in SpellOne.weapon_type):
			Answer = Answer + Spell_1 + ' does not work with this weapon type. '
		
	else: 
		Answer = Answer + 'Please input the correct name of the first spell. '
	
	
	# Check Spell 2 and get it's information	
	if (Spell_2 in SpecialCases):
		if Spell_2 == 'Bash':
			if Weapon_Type in ['Normal','Instant']:
				SpellTwo = Bash_Normal
			elif Weapon_Type in ['Missile','Missile-Splash']:
				SpellTwo = Bash_Missile
			else: Answer = Answer + Spell_2 + ' does not work with this weapon type. '
		if Spell_2 == 'Feedback':
			if Weapon_Type in ['Normal','Instant']:
				SpellTwo = Feedback_Normal
			elif Weapon_Type in ['Missile']:
				SpellTwo = Feedback_Missile
			else: Answer = Answer + Spell_2 + ' does not work with this weapon type. '
		if Spell_2 == 'Freezing Breath':
			if Weapon_Type == 'Missile':
				SpellTwo = FreezingBreath_Missile
			elif Weapon_Type == 'Missile-Splash':
				SpellTwo = FreezingBreath_MissileSplash
			else: Answer = Answer + Spell_2 + ' does not work with this weapon type. '
		if Spell_2 == 'Black Arrows':
			if Weapon_Type == 'Missile':
				SpellTwo = BlackArrows_Missle
			elif Weapon_Type in ['Normal','Instant']:
				SpellTwo = BlackArrows_Normal
			else: Answer = Answer + Spell_2 + ' does not work with this weapon type. '
	
	elif (Spell_2 in OrbDictionary):
		SpellTwo = OrbDictionary[Spell_2]
		if not (Weapon_Type in SpellTwo.weapon_type):
			Answer = Answer + Spell_2 + ' does not work with this weapon type. '
	
	else:
		Answer = Answer + 'Please input the correct name of the second spell. '
	
	
	# Return warning if something get's wrong
	if Answer != '':
		return Answer
	
	
	# Start comparason
	else:
		
		# Dealing with 2 same spells
		if Spell_1 == Spell_2:
			if SpellOne in AdditiveOrbs:
				Answer = Answer + 'The two spells can work together, perfectly additive. '
				return Answer
			elif SpellOne in SimilarOrbs:
				Answer = Answer + 'The two spells can work together, each works independently of the other, but only one works at a time. '
				return Answer
			else: 
				Answer = Answer + 'The two spells cannot work together. '
				return Answer
				
		# Dealing with 2 different spells
		else:
			if SpellOne.orb_level > SpellTwo.orb_level:
				HigherSpell = SpellTwo
				LowerSpell = SpellOne
			elif SpellOne.orb_level < SpellTwo.orb_level:
				HigherSpell = SpellOne
				LowerSpell = SpellTwo
			else: 
				if SpellOne.orb_type == '法球' and SpellTwo.orb_type == '法球':
					if SpellOne.buff_type == '独立攻击特效' and SpellTwo.buff_type == '独立攻击特效':
						Answer = Spell_1 + ' and ' + Spell_2 + ' has same priority. Read the article or test in WorldEditor for more information.'
						return Answer
					elif SpellOne.buff_type == '独立类攻击特效' and SpellTwo.buff_type == '独立攻击特效':
						Answer = Spell_1 + ' may be oppressed by ' + Spell_2 + ', and this depends on how the unit gets these spells. Read the article or test in WorldEditor for more information.'
						return Answer
					elif SpellOne.buff_type == '独立攻击特效' and SpellTwo.buff_type == '独立类攻击特效':
						Answer = Spell_2 + ' may be oppressed by ' + Spell_1 + ', and this depends on how the unit gets these spells. Read the article or test in WorldEditor for more information.'
						return Answer
					elif SpellOne.buff_type == '独立类攻击特效' and SpellTwo.buff_type == '独立类攻击特效':
						Answer = Spell_1 + ' and ' + Spell_2 + ' has same priority, and they can work together.'
						return Answer
					else: 
						Answer = Spell_1 + ' may be oppressed by ' + Spell_2 + ', and this depends on how the unit gets these spells. Read the article or test in WorldEditor for more information.'
						return Answer
				
				elif SpellOne.orb_type == '类法球' and SpellTwo.orb_type == '类法球':
					Answer = Spell_1 + ' and ' + Spell_2 + ' has same priority, and they can work together.'
					return Answer
				
				elif SpellOne.orb_type == '类法球' and SpellTwo.orb_type == '法球':
					Answer = Spell_1 + ' may be oppressed by ' + Spell_2 + ', and this depends on how the unit gets these spells. Read the article or test in WorldEditor for more information.'
					return Answer
				
				elif SpellOne.orb_type == '法球' and SpellTwo.orb_type == '类法球':
					Answer = Spell_2 + ' may be oppressed by ' + Spell_1 + ', and this depends on how the unit gets these spells. Read the article or test in WorldEditor for more information.'
					return Answer
				
				else:
					if SpellOne.buff_type == '独立攻击特效' and SpellTwo.buff_type == '独立攻击特效':
						Answer = Spell_1 + ' and ' + Spell_2 + ' has same priority, and they can work together.'
						return Answer
					elif SpellOne.buff_type == '独立攻击特效' and SpellTwo.buff_type == '独立类攻击特效':
						Answer = Spell_2 + ' may be oppressed by ' + Spell_1 + ', and this depends on how the unit gets these spells. Read the article or test in WorldEditor for more information.'
						return Answer
					elif SpellOne.buff_type == '独立类攻击特效' and SpellTwo.buff_type == '独立攻击特效':
						Answer = Spell_1 + ' may be oppressed by ' + Spell_2 + ', and this depends on how the unit gets these spells. Read the article or test in WorldEditor for more information.'
						return Answer
					else: 
						Answer = Spell_1 + ' and ' + Spell_2 + ' has same priority, and they can work together.'
						return Answer
			
			
			#Dealing with the HigherSpell and the LowerSpell
			if HigherSpell.orb_type == '法球':
				if HigherSpell.buff_type == '独立攻击特效' or '非独立攻击特效':
					Answer = LowerSpell.name + ' will be oppressed by ' + HigherSpell.name + '.'
					return Answer
				else:
					if LowerSpell.buff_type == '独立攻击特效' or '独立类攻击特效':
						Answer = HigherSpell.name + ' and ' + LowerSpell.name + ' can co-exist.'
						return Answer
					else: 
						Answer = LowerSpell.name + ' will be oppressed by ' + HigherSpell.name + '.'
						return Answer
			elif HigherSpell.orb_type == '类法球':
				Answer = HigherSpell.name + ' and ' + LowerSpell.name + ' can co-exist.'
				return Answer
			else: 
				if HigherSpell.buff_type == '独立攻击特效':
					Answer = HigherSpell.name + ' will be oppressed by ' + LowerSpell.name + '.'
					return Answer
				else:
					Answer = HigherSpell.name + ' and ' + LowerSpell.name + ' can co-exist.'
					return Answer	
