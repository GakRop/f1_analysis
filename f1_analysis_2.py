# -*- coding: utf-8 -*-
"""
Created on Sun May 28 19:51:21 2023

@author: gakro
"""

"""
this program is to predict the final position of each driver in the race.
thus, the output should be the position (ordinal data from 1 to 20).
the inputs (which parameters to use and which year, race, and session to use)
and the appropriate algorithms should be considered.

training set: Bahrain, Saudi Arabia, Australia, Azerbaijan (all in 2023)
test set: Miami (2023)
"""

import matplotlib.pyplot as plt
import fastf1

"""
the following block of code loads the session data of each qualifying race
"""

bahrain_quali = fastf1.get_session(2023, "Bahrain", "Q")
bahrain_quali.load(telemetry=False, laps=False, weather=False)

saudi_quali = fastf1.get_session(2023, "Saudi Arabi", "Q")
saudi_quali.load(telemetry=False, laps=False, weather=False)

australia_quali = fastf1.get_session(2023, "Australia", "Q")
australia_quali.load(telemetry=False, laps=False, weather=False)

azerbaijan_quali = fastf1.get_session(2023, "Azerbaijan", "Q")
azerbaijan_quali.load(telemetry=False, laps=False, weather=False)

miami_quali = fastf1.get_session(2023, "Miami", "Q")
miami_quali.load(telemetry=False, laps=False, weather=False)

bahrain_quali_result = bahrain_quali.results
saudi_quali_result = saudi_quali.results
australia_quali_result = australia_quali.results
azerbaijan_quali_result = azerbaijan_quali.results
miami_quali_result = miami_quali.results

"""
the following block of code loads the session data of each race
"""
bahrain_race = fastf1.get_session(2023, "Bahrain", "Race")
bahrain_race.load(telemetry=False, laps=False, weather=False)

saudi_race = fastf1.get_session(2023, "Saudi Arabi", "Race")
saudi_race.load(telemetry=False, laps=False, weather=False)

australia_race = fastf1.get_session(2023, "Australia", "Race")
australia_race.load(telemetry=False, laps=False, weather=False)

azerbaijan_race = fastf1.get_session(2023, "Azerbaijan", "Race")
azerbaijan_race.load(telemetry=False, laps=False, weather=False)

miami_race = fastf1.get_session(2023, "Miami", "Race")
miami_race.load(telemetry=False, laps=False, weather=False)

bahrain_race_result = bahrain_race.results
saudi_race_result = saudi_race.results
australia_race_result = australia_race.results
azerbaijan_race_result = azerbaijan_race.results
miami_race_result = miami_race.results

"""
plot the quali position in the x axis and the race finishing position in the y axis
to see how much they are correlated as the starter.
Try to use the logistic regressio. However, it must be for multiple class
(since what we are predicting is the position in the end of the race from 1 to 20),
and for ordinal output (since the position has the order).
"""
"""
print(bahrain_quali_result)
print(type(bahrain_quali_result))

bahrain_quali_result:
DriverNumber, BroadcastName, Abbreviation, 
"""
