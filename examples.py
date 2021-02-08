# IndySim Project
# Copyright (C) 2021 Drake Andersen
# Functions for simulating performances of indeterminate music for analysis

####################
####  EXAMPLES  ####
####################

# import file (imports random and music21 as m21)
exec(open('/Users/User/indysim.py').read())

# import a melody from an XML file
my_melody = import_score('/Users/User/sample_score.xml')

# import a second melody using optional parts arg (part = 0 by default)
my_melody2 = import_score('/Users/User/sample_score.xml', part=1)

# you can also enter a melody as a list of MIDI note numbers
my_melody3 = [72, 71, 69, 67, 65, 62]

# one virtual performance, length = 50, no leading silence
perf1 = one_perf(my_melody, 100, leading=False)

# simulate ten performances of melody, length = 100, with silences interspersed
sim1 = build_sim(my_melody, 100, 10, between=True)

sim2 = build_sim(my_melody2, 100, 10, between=False)

# organize simulation results by unit time...
sim_by_time = sim_time(sim1)

# ...in order to examine pitch content over time
for elem in sim_by_time:
	print(set(elem))

# combine simulations to get verticalities between parts
combine_sims([sim1, sim2])

#####################
#####   NOTES   #####
#####################

# performance length should generally be at least one order of magnitude greater than sequence length
# (sequence length = melody length plus any leading, trailing, or interspersed zeroes)
# if the two values are too close it will take too long to get random values that don't duplicate