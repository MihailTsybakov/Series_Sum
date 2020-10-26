import matplotlib.pyplot as plt
import math
X, N, f = [i/10000 for i in range(1, 10000)], 200, []
for x in X:
    f.append(sum([math.cos(n*x)/math.sqrt(n) for n in range(1, N)]))
fig, axes = plt.subplots()
axes.plot(X, f)