

class Compress:
    
    def __init__(self):
        self.val = {}
        self.comp = []
        self.desc = ""


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
        i = 0
        for x in comp:
            self.desc[0] = Compress.x.get_key()
            i += 1

        return (" ".join(map(str, self.desc)))

    def get_key(self, x):
        for key, value in self.vals.items():
            if x == value:
                return key