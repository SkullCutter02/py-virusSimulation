import matplotlib.pyplot as plt
from simulation import *
import numpy as np
from scipy.optimize import curve_fit

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

def gaussian(x, mean, amplitude, standard_deviation):
    return amplitude * np.exp( - ((x - mean) / standard_deviation) ** 2)

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
    # mu = meanOfDistribution(virusValues)
    # sigma = numpy.std(virusValues)
    # # x = mu + sigma * numpy.random.randn(virusValues[-1], steps + additionalSteps)
    # x = mu + sigma
    # numBins = columnValues[-1]
    # n, bins, patches = plt.hist(x, numBins, density=1, facecolor="blue", alpha=0.5)
    # y = norm.pdf(bins, mu, sigma)
    # plt.plot(bins, y, "r--")
    # plt.xlabel("Virus Population")
    # plt.ylabel("Patients")
    # plt.subplots_adjust(left=0.15)
    # plt.show()

    # https://realpython.com/python-histograms/
    # n, bins, patches = plt.hist(virusValues, bins="auto", color="#0504aa", alpha=0.7, rwidth=0.85)
    n, bins, _ = plt.hist(virusValues, bins='auto', label='histogram')
    # plt.grid(axis="y", alpha=0.75)
    # plt.xlabel("Virus Population")
    # plt.ylabel("Patients")
    # plt.title(f"Virus Population vs Patient Histogram at {steps} steps")

    bin_centers = bins[:-1] + np.diff(bins) / 2
    popt, _ = curve_fit(gaussian, bin_centers, n, p0=[1., 0., 1.])

    x_interval_for_fit = np.linspace(bins[0], bins[-1], 10000)
    plt.plot(x_interval_for_fit, gaussian(x_interval_for_fit, *popt), label='fit')
    plt.legend()

    # maxFreq = n.max()
    # plt.ylim(ymax=np.ceil(maxFreq / 10) * 10 if maxFreq % 10 else maxFreq + 10)
    # plt.show()

simulateDelayed()

