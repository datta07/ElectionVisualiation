import sqlite3
import matplotlib
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
import numpy as np
import requests
from difflib import SequenceMatcher
import matplotlib

def give_party(no):
	#data={82: 'Telangana Rashtra Samithi', 7: 'Telangana Rashtra Samithi', 97: 'Telangana Rashtra Samithi', 80: 'Telangana Rashtra Samithi', 59: 'Telangana Rashtra Samithi', 36: 'Telangana Rashtra Samithi', 11: 'Telangana Rashtra Samithi', 5: 'Indian National Congress', 118: 'Telugu Desam', 69: 'All India Majlis-E-Ittehadul Muslimeen', 19: 'Telangana Rashtra Samithi', 14: 'Telangana Rashtra Samithi', 3: 'Telangana Rashtra Samithi', 119: 'Indian National Congress', 94: 'Telangana Rashtra Samithi', 108: 'Indian National Congress', 8: 'Telangana Rashtra Samithi', 12: 'Telangana Rashtra Samithi', 67: 'All India Majlis-E-Ittehadul Muslimeen', 66: 'All India Majlis-E-Ittehadul Muslimeen', 2: 'Telangana Rashtra Samithi', 53: 'Telangana Rashtra Samithi', 27: 'Telangana Rashtra Samithi', 86: 'Telangana Rashtra Samithi', 76: 'Telangana Rashtra Samithi', 22: 'Telangana Rashtra Samithi', 101: 'Telangana Rashtra Samithi', 41: 'Telangana Rashtra Samithi', 79: 'Telangana Rashtra Samithi', 42: 'Telangana Rashtra Samithi', 99: 'Telangana Rashtra Samithi', 65: 'Bharatiya Janta Party', 32: 'Telangana Rashtra Samithi', 31: 'Telangana Rashtra Samithi', 89: 'Indian National Congress', 48: 'Telangana Rashtra Samithi', 75: 'Telangana Rashtra Samithi', 21: 'Telangana Rashtra Samithi', 98: 'Telangana Rashtra Samithi', 61: 'Telangana Rashtra Samithi', 13: 'Telangana Rashtra Samithi', 83: 'Telangana Rashtra Samithi', 16: 'Telangana Rashtra Samithi', 26: 'Telangana Rashtra Samithi', 64: 'All India Majlis-E-Ittehadul Muslimeen', 60: 'Telangana Rashtra Samithi', 112: 'Telangana Rashtra Samithi', 6: 'Telangana Rashtra Samithi', 90: 'Telangana Rashtra Samithi', 72: 'Telangana Rashtra Samithi', 85: 'Indian National Congress', 20: 'Telangana Rashtra Samithi', 117: 'Indian National Congress', 46: 'Telangana Rashtra Samithi', 49: 'Indian National Congress', 114: 'Indian National Congress', 102: 'Telangana Rashtra Samithi', 74: 'Telangana Rashtra Samithi', 50: 'Indian National Congress', 77: 'Telangana Rashtra Samithi', 58: 'All India Majlis-E-Ittehadul Muslimeen', 44: 'Telangana Rashtra Samithi', 30: 'Telangana Rashtra Samithi', 4: 'Telangana Rashtra Samithi', 24: 'Indian National Congress', 34: 'Telangana Rashtra Samithi', 43: 'Telangana Rashtra Samithi', 88: 'Telangana Rashtra Samithi', 10: 'Telangana Rashtra Samithi', 109: 'Indian National Congress', 93: 'Indian National Congress', 57: 'Telangana Rashtra Samithi', 87: 'Telangana Rashtra Samithi', 81: 'Telangana Rashtra Samithi', 95: 'Indian National Congress', 92: 'Telangana Rashtra Samithi', 63: 'All India Majlis-E-Ittehadul Muslimeen', 35: 'Telangana Rashtra Samithi', 73: 'Telangana Rashtra Samithi', 103: 'Telangana Rashtra Samithi', 37: 'Telangana Rashtra Samithi', 9: 'Telangana Rashtra Samithi', 18: 'Telangana Rashtra Samithi', 17: 'Telangana Rashtra Samithi', 113: 'Indian National Congress', 100: 'Telangana Rashtra Samithi', 104: 'Telangana Rashtra Samithi', 54: 'Telangana Rashtra Samithi', 40: 'Telangana Rashtra Samithi', 25: 'Telangana Rashtra Samithi', 110: 'Indian National Congress', 45: 'Telangana Rashtra Samithi', 51: 'Telangana Rashtra Samithi', 23: 'All India Forward Bloc', 62: 'Telangana Rashtra Samithi', 39: 'Indian National Congress', 116: 'Telugu Desam', 70: 'Telangana Rashtra Samithi', 71: 'Telangana Rashtra Samithi', 52: 'Telangana Rashtra Samithi', 84: 'Telangana Rashtra Samithi', 33: 'Telangana Rashtra Samithi', 29: 'Telangana Rashtra Samithi', 1: 'Telangana Rashtra Samithi', 91: 'Telangana Rashtra Samithi', 56: 'Indian National Congress', 96: 'Telangana Rashtra Samithi', 47: 'Telangana Rashtra Samithi', 28: 'Telangana Rashtra Samithi', 55: 'Telangana Rashtra Samithi', 78: 'Telangana Rashtra Samithi', 107: 'Telangana Rashtra Samithi', 106: 'Telangana Rashtra Samithi', 105: 'Telangana Rashtra Samithi', 115: 'Independent', 68: 'All India Majlis-E-Ittehadul Muslimeen', 111: 'Indian National Congress', 15: 'Indian National Congress', 38: 'Telangana Rashtra Samithi'}
	#partys={'All India Forward Bloc':(1,0,0,1),'All India Majlis-E-Ittehadul Muslimeen':(0,1,0,1),'Bharatiya Janta Party':(255/255, 191/255, 0,1),'Independent':(186/255, 185/255, 182/255,1),'Indian National Congress':(0,0,1,1),'Telangana Rashtra Samithi':(1, 0, 230/255),'Telugu Desam':(1, 247/255, 0)}
	data={8: 'BJP', 7: 'BJP', 9: 'BJP', 12: 'BJP', 5: 'BJP', 10: 'BJP', 13: 'BJP', 6: 'BJP', 4: 'BJP', 3: 'INC', 11: 'BJP', 14: 'BJP', 20: 'BJP', 15: 'BJP', 18: 'INC', 16: 'BJP', 2: 'BJP', 17: 'BJP', 19: 'INC', 1: 'BJP', 24: 'BJP', 22: 'BJP', 46: 'BJP', 25: 'BJP', 27: 'BJP', 26: 'INC', 49: 'BJP', 45: 'BJP', 48: 'BJP', 44: 'BJP', 50: 'BJP', 230: 'BJP', 70: 'BJP', 61: 'BJP', 28: 'BJP', 68: 'BJP', 47: 'BJP', 60: 'BJP', 51: 'BJP', 33: 'BJP', 69: 'BJP', 73: 'BJP', 32: 'BJP', 52: 'BJP', 43: 'BJP', 227: 'BJP', 228: 'BJP', 72: 'BJP', 71: 'BJP', 29: 'BJP', 62: 'BJP', 34: 'BJP', 67: 'BJP', 59: 'BJP', 53: 'BJP', 229: 'BJP', 63: 'BJP', 31: 'BJP', 79: 'BJP', 75: 'BJP', 74: 'BJP', 30: 'BJP', 64: 'BJP', 78: 'BJP', 76: 'INC', 225: 'BJP', 77: 'BJP', 35: 'BJP', 57: 'BJP', 58: 'BJP', 42: 'BJP', 66: 'BJP', 165: 'BJP', 36: 'BJP', 226: 'BJP', 147: 'BJP', 65: 'BJP', 162: 'BJP', 146: 'BJP', 54: 'BJP', 163: 'BJP', 82: 'BJP', 224: 'BJP', 83: 'BJP', 81: 'BJP', 80: 'BJP', 161: 'BJP', 92: 'BJP', 90: 'BJP', 148: 'BJP', 223: 'BJP', 40: 'BJP', 166: 'BJP', 222: 'BJP', 93: 'BJP', 55: 'BJP', 37: 'BJP', 164: 'BJP', 149: 'BJP', 145: 'BJP', 39: 'BJP', 41: 'BJP', 91: 'BJP', 160: 'BJP', 213: 'BJP', 56: 'BJP', 144: 'BJP', 143: 'BJP', 212: 'BJP', 89: 'BJP', 84: 'BJP', 159: 'BJP', 167: 'BJP', 221: 'INC', 219: 'BJP', 214: 'BJP', 168: 'BJP', 38: 'BJP', 94: 'BJP', 142: 'BJP', 169: 'BJP', 215: 'BJP', 85: 'BJP', 220: 'BJP', 155: 'BJP', 95: 'BJP', 171: 'BJP', 218: 'BJP', 86: 'BJP', 101: 'BJP', 194: 'BJP', 158: 'BJP', 102: 'BJP', 150: 'INC', 151: 'BJP', 170: 'BJP', 141: 'BJP', 216: 'BJP', 152: 'BJP', 153: 'INC', 88: 'INC', 154: 'BJP', 195: 'BJP', 217: 'BJP', 157: 'BJP', 96: 'BJP', 120: 'BJP', 202: 'BJP', 140: 'BJP', 119: 'BJP', 87: 'BJP', 99: 'BJP', 98: 'BJP', 203: 'BJP', 97: 'BJP', 100: 'BJP', 172: 'BJP', 211: 'BJP', 118: 'BJP', 196: 'BJP', 103: 'INC', 104: 'INC', 193: 'INC', 121: 'BJP', 156: 'BJP', 139: 'BJP', 173: 'BJP', 117: 'INC', 138: 'BJP', 204: 'BJP', 201: 'BJP', 174: 'BJP', 106: 'INC', 210: 'BJP', 192: 'INC', 123: 'INC', 137: 'BJP', 209: 'BJP', 197: 'INC', 136: 'BJP', 122: 'INC', 107: 'BJP', 200: 'BJP', 134: 'BJP', 182: 'BJP', 105: 'INC', 135: 'BJP', 191: 'BJP', 183: 'BJP', 116: 'BJP', 115: 'BJP', 199: 'BJP', 198: 'INC', 175: 'BJP', 132: 'BJP', 108: 'INC', 127: 'BJP', 110: 'BJP', 184: 'BJP', 188: 'BJP', 176: 'BJP', 124: 'BJP', 190: 'BJP', 130: 'BJP', 177: 'BJP', 114: 'BJP', 126: 'INC', 178: 'BJP', 181: 'BJP', 185: 'BJP', 133: 'BJP', 131: 'BJP', 111: 'BJP', 128: 'BJP', 189: 'BJP', 186: 'BJP', 125: 'BJP', 187: 'BJP', 129: 'BJP', 113: 'BJP', 112: 'BJP', 109: 'BJP', 179: 'BJP', 180: 'BJP', 21: 'BJP', 23: 'BJP'}
	partys={'All India Forward Bloc':(1,0,0,1),'AIMIM':(0,1,0,1),'BJP':(255, 140, 0),'Independent':(186/255, 185/255, 182/255,1),'INC':(0,0,1,1),'TRS':(1, 0, 230/255),'Telugu Desam':(1, 247/255, 0)}
	return partys[data[no]]

fig, ax = plt.subplots()
map=Basemap(projection="mill",lat_0=0, lon_0=0,llcrnrlon=74.05, llcrnrlat=21.05, urcrnrlon=82.8, urcrnrlat=27)
map.readshapefile('../data/India_AC','ap')

map_data={}

for info,shape in zip(map.ap_info, map.ap):
	ax.add_collection(PatchCollection([Polygon(np.array(shape))], facecolor= (1,1,1,1), edgecolor=(1,1,1,1), linewidths=.3, zorder=2))

for info,shape in zip(map.ap_info, map.ap):
	if (info['ST_NAME']=='MADHYA PRADESH'):
		ax.add_collection(PatchCollection([Polygon(np.array(shape))], facecolor= give_party(info['AC_NO']), edgecolor=(0,0,0,1), linewidths=.3, zorder=2))
#print(map_data)
		
plt.show()