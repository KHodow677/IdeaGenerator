import random, os

class RandomWordGen():
    def __init__(self):
        self.Reset()
        

    def Reset(self):
        self.noun = self.GetNoun()
        self.verb = self.GetVerb()
        self.adj = self.GetAdj()
        self.idea = f"{self.verb} {self.adj} {self.noun}"
        self.idea = self.idea[0].upper() + self.idea[1:]

    def GetNoun(self):
        randomWord = self.RandomLine("WordBank/nouns.txt")
        return randomWord

    def GetVerb(self):
        randomWord = self.RandomLine("WordBank/verbs.txt")
        return randomWord

    def GetAdj(self):
        randomWord = self.RandomLine("WordBank/adjectives.txt")
        return randomWord

    def RandomLine(self, fileName):
        line = random.choice(open(fileName).readlines()).strip()
        return line

randomthing = RandomWordGen()
print(randomthing.idea)