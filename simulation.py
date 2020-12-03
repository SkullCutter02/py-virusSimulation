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
        prob2 = random.random() / 10
        if prob2 <= prob:
            return SimpleVirus(self.maxBirthProb, self.clearProb)
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
            pass
        return int(len(self.viruses))

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
        prob = self.maxBirthProb * (1 - popDensity)
        prob2 = random.random() / 10
        # if len(activeDrugs) > 0 and prob2 <= prob:
        if prob2 <= prob:
            newResistances = {}
            for k, v in self.resistances.items():
                newResistances[k] = True if random.random() <= 1 - self.mutProb else False
                newResistances[k] = not newResistances[k] if random.random() <= self.mutProb else newResistances[k]
                return ResistantVirus(self.maxBirthProb, self.clearProb, newResistances, self.mutProb)
        else:
            raise NoChildException


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
            pass
        return int(len(self.viruses))

