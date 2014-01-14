class Lexicon(object):

    def __init__(self):
        self.nouns = ['bear', 'princess']
        self.verbs =['go','stop','kill','eat']
        self.stop_words = ['the','in','of','from','at','it']
        self.directions = ['north','south','east','west','down','up',
                'down', 'up', 'left','right','back']

    def convert_number(self, s):
        try:
            return int(s)
        except ValueError:
            return None 

    def check_noun(self,s):
        try:
            return self.nouns.index(s)
        except ValueError:
            return -1
    
    def check_verb(self,s):
        try:
            return self.verbs.index(s)
        except ValueError:
            return -1

    def check_stop(self,s):
        try:
            return self.stop_words.index(s)
        except ValueError:
            return -1

    def check_direction(self,s):
        try:
            return self.directions.index(s)
        except ValueError:
            return -1


    def scan(self,text):
        words = text.split()
        returnSet = []
        for word in words:

            mint =  self.convert_number(word)
            if mint != None:
                returnSet.append(('number',mint))
            elif self.check_noun(word) >= 0:
                returnSet.append(('noun',word))
            elif self.check_verb(word) >= 0:
                returnSet.append(('verb',word))
            elif self.check_stop(word) >= 0:
                returnSet.append(('stop',word))
            elif self.check_direction(word) >= 0:
                returnSet.append(('direction', word))
            else:
                returnSet.append(('error',word))

        return returnSet
