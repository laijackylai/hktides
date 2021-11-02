import Nio
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import datetime

OUT_PATH = './data/'
START_DATE = datetime.datetime(1990, 1, 1)

fname = './tidal sample data/WW3/HK/2021080300/ww3.20210803.nc'
f = Nio.open_file(fname, 'r')

var = list(f.variables.keys())
bounding_box = [f.westernmost_longitude, f.southernmost_latitude,
                f.easternmost_longitude, f.northernmost_latitude]

lon = f.variables['longitude'][:]
lat = f.variables['latitude'][:]
time = f.variables['time'][:]  # days since 1990-01-01 00:00:00

lat, lon = np.meshgrid(lat, lon)
# format should be [:, lat ,lon]
combined = (np.dstack((lat, lon)).swapaxes(0, 2))

mean_wave_height = f.variables['hs'][:, :, :].filled(
    np.NAN)  # wave height at time, lat, lon

for i in range(len(time)):
    timestamp = START_DATE + datetime.timedelta(days=time[i])
    timestring = timestamp.strftime("%Y%m%d%H%M%S")
    pngname = OUT_PATH + 'ww3_hs_' + timestring + '.png'

    data = np.nan_to_num(mean_wave_height[i, :, :])
    data = np.flipud(data)

    mask = np.nan_to_num(np.flipud(mean_wave_height[i, :, :]), nan=9999)
    mask = np.isin(mask, 9999).astype(np.uint8)

    plt.imsave(pngname, data, cmap=cm.gray)

# im = Image.fromarray(test_data).convert(
#     'L')
# im.save('test.png')
