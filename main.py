import matplotlib.pyplot as plt
from simulation import *
import numpy as np

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
    repeats = int(input("How many times do you want to repeat the experiment? "))
    columnValues = []
    virusValues = []
    for number in range(repeats):
        pop = []
        for x in range(population):
            virus = ResistantVirus(0.1, 0.05, {"guttagonal": False}, 0.005)
            pop.append(virus)
        patient = ResistantPatient(pop, maxPopulation)
        tempVirusValues = []
        for i in range(steps):
            pop = patient.update()
            tempVirusValues.append(pop)
        patient.addPrescription("guttagonal")
        for i in range(additionalSteps + steps + 1):
            pop = patient.update()
            tempVirusValues.append(pop)
        virusValues.append(tempVirusValues[-1])
        print(tempVirusValues[-1])
        columnValues.append(1)
    n, bins, patches = plt.hist(virusValues, bins="auto", color="#0504aa", alpha=0.7, rwidth=0.85)
    plt.grid(axis="y", alpha=0.75)
    plt.xlabel("Virus Population")
    plt.ylabel("Patients")
    plt.title(f"Virus Population vs Patient Histogram at {steps} steps")
    maxFreq = n.max()
    plt.ylim(ymax=np.ceil(maxFreq / 10) * 10 if maxFreq % 10 else maxFreq + 10)
    plt.show()

# simulateDelayed()

def simulateTreatment():
    pass

simulateTreatment()

def simulateTwoDrugs():
    inputSteps = int(input("300/150/75/0"))
    steps = 150
    population = 100
    maxPopulation = 1000
    pop = []
    for x in range(population):
        virus = ResistantVirus(0.1, 0.05, {"guttagonal": False, "grimpex": False}, 0.005)
        pop.append(virus)
    patient = ResistantPatient(pop, maxPopulation)
    columnValues = []
    virusValues = []
    for i in range(steps):
        pop = patient.update()
        columnValues.append(i)
        virusValues.append(pop)
    patient.addPrescription("guttagonal")
    for i in range(inputSteps + steps + 1):
        pop = patient.update()
        columnValues.append(i)
        virusValues.append(pop)
    patient.addPrescription("grimpex")
    for i in range(steps + steps + inputSteps + 1):
        pop = patient.update()
        columnValues.append(i)
        virusValues.append(pop)
    n, bins, patches = plt.hist(virusValues, bins="auto", color="#0504aa", alpha=0.7, rwidth=0.85)
    plt.grid(axis="y", alpha=0.75)
    plt.xlabel("Virus Population")
    plt.ylabel("Patients")
    plt.title(f"Virus Population vs Patient Histogram at {inputSteps} steps")
    maxFreq = n.max()
    plt.ylim(ymax=np.ceil(maxFreq / 10) * 10 if maxFreq % 10 else maxFreq + 10)
    plt.show()

# simulateTwoDrugs()
