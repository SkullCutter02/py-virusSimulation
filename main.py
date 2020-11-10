import numpy
import random
import matplotlib.pyplot as plt

class NoChildException(Exception):
    pass

# SimpleVirus is the virus population
class SimpleVirus(object):
    """
    Representation of a simple virus (does not model drug effects/resistance).
    """

    def __init__(self, maxBirthProb, clearProb):
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def doesClear(self):
        prob = random.random()
        if prob <= self.clearProb:
            return True
        else:
            return False

    def reproduce(self, popDensity):
        prob = self.maxBirthProb * (1 - popDensity)
        prob2 = random.random()
        if prob2 <= prob:
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException

class SimplePatient(object):
    def __init__(self, viruses, maxPop):
        self.viruses = list(viruses)
        self.maxPop = maxPop

    def getTotalPop(self):
        return len(self.viruses)

    def update(self):
        self.viruses = list(filter(lambda x: not x.doesClear(), self.viruses))
        try:
            for virus in self.viruses:
                if len(self.viruses) < self.maxPop:
                    density = self.getTotalPop() / self.maxPop
                    self.viruses.append(virus.reproduce(density))
        except NoChildException:
            pass
        return int(len(self.viruses))

def problem2():
    population = 1000
    generations = 300
    pop = []
    for x in range(100):
        virus = SimpleVirus(0.1, 0.05)
        pop.append(virus)
    simplePatient = SimplePatient(pop, population)
    xPlotPoints = []
    yPlotPoints = []
    for x in range(generations):
        pop = simplePatient.update()
        xPlotPoints.append(x)
        yPlotPoints.append(pop)
    print(xPlotPoints, yPlotPoints)
    plt.plot(xPlotPoints, yPlotPoints)
    plt.ylabel("Virus Population")
    plt.xlabel("Generations")
    plt.show()
    """
        Run the simulation and plot the graph for problem 2 (no drugs are used,
        viruses do not have any drug resistance).

        Instantiates a patient, runs a simulation for 300 timesteps, and plots the
        total virus population as a function of time.
    """

problem2()


