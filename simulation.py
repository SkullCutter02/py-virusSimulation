import random

class NoChildException(Exception):
    pass

# SimpleVirus
class SimpleVirus(object):
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
        if random.random() <= prob:
            return SimpleVirus(self.maxBirthProb, self.clearProb)
        else:
            raise NoChildException

# ResistantVirus
class ResistantVirus(SimpleVirus):
    def __init__(self, maxBirthProb, clearProb, resistances, mutProb):
        super().__init__(maxBirthProb, clearProb)
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb
        self.resistances = resistances
        self.mutProb = mutProb

    def getResistance(self, drug):
        for k, v in self.resistances.items():
            if k.lower() == drug.lower():
                return v

    def reproduce(self, popDensity, activeDrugs):
        # activeDrugs: a list of the drug names acting on this virus particle (a list of strings).
        prob = self.maxBirthProb * (1 - popDensity)
        if len(activeDrugs) > 0 and random.random() <= prob:
            newMaxBirthProb = 0
            newClearProb = 0
            newMutProb = 0
            newResistances = {}
            for k, v in self.resistances.items():
                newResistances[k] = True if random.random() <= 1 - self.mutProb else False
                newResistances[k] = not newResistances[k] if random.random() <= self.mutProb else newResistances[k]
                return ResistantVirus(newMaxBirthProb, newClearProb, newResistances, newMutProb)
        else:
            raise NoChildException

# SimplePatient
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
            print("Error")
        return int(len(self.viruses))

class ResistantPatient(SimplePatient):
    def __init__(self, viruses, maxPop):
        super().__init__(viruses, maxPop)
        self.viruses = viruses
        self.maxPop = maxPop
        self.drugs = []

    def addPrescription(self, newDrug):
        if newDrug not in self.drugs:
            self.drugs.append(newDrug)

    def getPrescriptions(self):
        return self.drugs

    def getResistPop(self, drugResist):
        pop = 0
        for virus in self.viruses:
            num = 0
            for k, v in virus.resistances.items():
                if v:
                    if k in drugResist:
                        num += 1
                if num == len(drugResist):
                    pop += 1
        return pop

    def update(self):
        self.viruses = list(filter(lambda x: not x.doesClear(), self.viruses))
        try:
            for virus in self.viruses:
                if len(self.viruses) < self.maxPop:
                    popDensity = len(self.viruses) / self.maxPop
                    self.viruses.append(virus.reproduce(popDensity, self.drugs))
        except NoChildException:
            print("Error")
        return int(len(self.viruses))

