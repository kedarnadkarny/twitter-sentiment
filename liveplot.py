import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
	graph_data = open('twitterDB.csv','r').read()
	lines = graph_data.split('\n')
	xs = []
	ys = []
	i=0
	total=0
	for line in lines:
		if len(line) > 1:
			x = line
			xs.append(i)
			ys.append(total)
			i = i + 1
			total = total + float(x)
	ax1.clear()
	ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=3000)
plt.show()
