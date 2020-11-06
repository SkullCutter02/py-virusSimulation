import numpy
import random

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
        pass

    def reproduce(self, popDensity):
        prob = self.maxBirthProb * (1 - popDensity)
        prob2 = random.random()
        if prob2 <= prob:
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            return NoChildException

class SimplePatient(object):
    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """
    def __init__(self, viruses, maxPop):
        self.viruses = viruses
        self.maxPop = maxPop
        """
        Initialization function, saves the viruses and maxPop parameters asattributes.
        viruses: the list representing the virus population (a list of
        SimpleVirus instances)
        maxPop: the maximum virus population for this patient (an integer)
        """
        # TODO
    def getTotalPop(self):
        pass
        """
        Gets the current total virus population.
        returns: The total virus population (an integer)
        """
        # TODO
    def update(self):
        pass
        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        - Determine whether each virus particle survives and updates the list of virus particles accordingly.
        - The current population density is calculated. This population density value is used until the next call to update()
        - Determine whether each virus particle should reproduce and add offspring virus particles to the list of viruses in this patient.
        returns: the total virus population at the end of the update (an
        integer)
        """
        # TODO
