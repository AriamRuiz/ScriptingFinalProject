class Regular_Verb:
    def __init__(self, verb):
        self.verb = verb

    def conjugate(self, subject):
        endings = {
            'je': 'e',
            'tu': 'es',
            'il': 'e',
            'elle': 'e',
            'on': 'e',
            'nous': 'ons',
            'vous': 'ez',
            'ils': 'ent',
            'elles': 'ent'
        }
        if subject.lower() in endings:
            return self.verb[:-2] + endings[subject.lower()]
        else:
            return "Wrong person conjugation"


parler = Regular_Verb('parler')
print(parler.conjugate('je'))  # Outputs: parle
print(parler.conjugate('nous'))
print(parler.conjugate('nouss'))
