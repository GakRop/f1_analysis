# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import fastf1

session = fastf1.get_session(2019, "Monza", "Q")
session.load(telemetry=False, laps=False, weather=False)
vettel = session.get_driver("VET")
print(f"Pronto {vettel['FirstName']}?")

import fastf1.plotting

fastf1.plotting.setup_mpl(2019, "Monza", "Q")

session.load()
fast_leclerc = session.laps.pick_driver("LEC").pick_fastest()
lec_car_data = fast_leclerc.get_car_data()
t = lec_car_data['Time']
vCar = lec_car_data['Speed']

fig, ax = plt.subplots()
ax.plot(t, vCar, label="Fast")
ax.set_xlabel('Time')
ax.set_ylabel('Speed [Km/h]')
ax.set_title('Leclerc is')
ax.legend()
plt.show()