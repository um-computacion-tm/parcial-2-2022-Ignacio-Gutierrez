

class Compress:
    
    def __init__(self):
        self.val = {}
        self.comp = []
        self.desc = []


    def compress(self, text):
        tex = text.split(' ')
        i = 1
        for x in tex:
            if not x in self.val:
                self.val.update({x: i})
                i += 1
            else:
                pass
        
        for x in tex:
             self.comp.append(self.val.get(x))

        return self.comp, self.val

    def uncompress(self, comp, val):
        claves = list(val.keys())
        valores = list(val.values())

        for c in comp:
            self.desc.append(list(val.keys())[list(val.values()).index(c)])


        return (" ".join(map(str, self.desc)))