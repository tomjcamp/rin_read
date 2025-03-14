import pandas as pd
import pickle
import datetime

path = r"C:\Users\tom_j\Downloads\center_of_mass\nga22140.eph"

def read_tle(pth):
	observations = []
	with open(pth, "r") as f:
		while line := f.readline():
			obs = {}
			my_line = line.split()
			if my_line[0] == '*':
				time = datetime.datetime(*map(int,my_line[1:-1]))
			elif my_line[0] == 'P':
				positions = line.split()[2:]
			elif my_line[0] == 'V':
				velocities = line.split()[2:]
				prn = my_line[1]

				obs['prn'] = prn
				obs['time'] = time
				obs['x'] = positions[0]
				obs['y'] = positions[1]
				obs['z'] = positions[2]
				obs['clock'] = positions[3]
				obs['d_x'] = velocities[0]
				obs['d_y'] = velocities[1]
				obs['d_z'] = velocities[2]
				obs['d_clock'] = velocities[3]

				observations.append(obs)
	return observations	
	
observations = pd.DataFrame(read_tle(path))

print(observations)
