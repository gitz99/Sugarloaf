###matplotlib
##Reference
# https://wikidocs.net/book/5011

#Library Import
from turtle import filling
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

##Read Excel Data
var = pd.read_excel('AAPL.xlsx')
# print(var)
Date = list(var['Date'])
x = list(var['Open'])
y = list(var['Close'])

#Process Data
xarray=np.array(x)
yarray=np.array(y)
delta_array=np.subtract(xarray, yarray)
delta=list(delta_array)

##Plot
# plt.figure(figsize=(5,5))
# plt.title('AAPL')
# plt.xlabel('Date')
# plt.ylabel("AAPL_Open")
# plt.plot(Date, delta, label='AAPL', color='red', marker='.', markersize=8, linewidth=2)
# plt.legend(loc='lower right')
# plt.grid(True, axis='y', color='red', alpha=0.1, linestyle='--')
# # plt.grid(True)
# # plt.grid(True, axis='x')
# # plt.grid(True, axis='y')
# plt.show()

fig=plt.figure()
fig.set_size_inches(15,10)

plt.subplot(2,1,1)
plt.plot(Date,x,'b-',Date,y,'g-')
plt.title('Open/Close')
plt.ylabel('AAPL Stock Price')

plt.subplot(2,1,2)
plt.plot(Date,delta,'r')
plt.title('Delta')
plt.ylabel('$')

# fig,(ax1, ax2) = plt.subplots(2)
# fig.suptitle('AAPL', fontsize=18, c='magenta')

# ax1.plot(Date, x, 'b-', Date, y, 'g-')
# ax1.set_title('Open/Close')

# ax2.plot(Date, delta, color='red')
# ax2.set_title('Delta')

#Full Screen
# mng = plt.get_current_fig_manager()
# mng.full_screen_toggle()
plt.show()