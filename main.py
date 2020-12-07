import matplotlib.pyplot as plt
from simulation import *
from scipy.stats import norm
import numpy

def meanOfDistribution(val):
    acc = 0
    for x in range(len(val)):
        acc += val[x]
    return acc / len(val)

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

# simulate_simple()

def simulate_drug():
    population = 100
    maxPopulation = 1000
    pop = []
    for x in range(population):
        virus = ResistantVirus(0.1, 0.05, {"guttagonal": False}, 0.005)
        pop.append(virus)
    patient = ResistantPatient(pop, maxPopulation)
    xPlotPoints = []
    yPlotPoints = []
    for i in range(150):
        pop = patient.update()
        xPlotPoints.append(i)
        yPlotPoints.append(pop)
    patient.addPrescription("guttagonal")
    for i in range(150):
        pop = patient.update()
        xPlotPoints.append(i + 150)
        yPlotPoints.append(pop)
    plt.plot(xPlotPoints, yPlotPoints)
    plt.ylabel("Virus Population")
    plt.xlabel("Generations")
    plt.show()

# simulate_drug()

def simulateDelayed():
    steps = int(input("300/150/75/0"))
    additionalSteps = 150
    population = 100
    maxPopulation = 1000
    pop = []
    for x in range(population):
        virus = ResistantVirus(0.1, 0.05, {"guttagonal": False}, 0.005)
        pop.append(virus)
    patient = ResistantPatient(pop, maxPopulation)
    columnValues = []
    virusValues = []
    for i in range(steps):
        pop = patient.update()
        columnValues.append(i)
        virusValues.append(pop)
    for i in range(additionalSteps + steps + 1):
        pop = patient.update()
        columnValues.append(i)
        virusValues.append(pop)
    mu = meanOfDistribution(virusValues)
    print(mu)
    sigma = numpy.std(virusValues)
    x = mu + sigma * numpy.random.randn(10000)
    numBins = columnValues[-1]
    n, bins, patches = plt.hist(x, numBins, density=1, facecolor="blue", alpha=0.5)
    y = norm.pdf(bins, mu, sigma)
    plt.plot(bins, y, "r--")
    plt.xlabel("Virus Population")
    plt.ylabel("Patients")
    plt.subplots_adjust(left=0.15)
    plt.show()

simulateDelayed()

