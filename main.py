import matplotlib.pyplot as plt
from simulation import *

def simulate_simple():
    population = 100
    maxPopulation = 1000
    generations = 300
    pop = []
    for x in range(population):
        virus = SimpleVirus(0.1, 0.05)
        pop.append(virus)
    simplePatient = SimplePatient(pop, maxPopulation)
    xPlotPoints = []
    yPlotPoints = []
    for x in range(generations):
        pop = simplePatient.update()
        xPlotPoints.append(x)
        yPlotPoints.append(pop)
    plt.plot(xPlotPoints, yPlotPoints)
    plt.ylabel("Virus Population")
    plt.xlabel("Generations")
    plt.show()

simulate_simple()


