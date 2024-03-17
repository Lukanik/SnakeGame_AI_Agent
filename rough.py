import matplotlib
# matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import time

# Enable interactive mode
plt.ion()

# Create a plot
plt.plot([1, 2, 3], [4, 5, 6])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Interactive Plot')

# Modify the plot dynamically
plt.plot([4, 5, 6], [7, 8, 9])
plt.plot([3, 5, 3], [2, 4, 1])
plt.plot([1, 6, 9], [6, 4, 3])
input("Press Enter...")

# The plot is updated dynamically without needing to redraw it
