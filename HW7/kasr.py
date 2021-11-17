class kasr:
    def _init_(self, x=None, y=None):
        self.x = x
        self.y = y
        
    def sum(self, second):
        result = kasr()
        result.x = self.x*second.y + self.y*second.x
        result.y = self.y*second.y
        return result


    def sub(self, second):
        result = kasr()
        result.x = self.x*second.y - self.y*second.x
        result.y = self.y*second.y
        return result

    def multiple(self, second):
        result = kasr()
        result.x = self.x*second.x
        result.y = self.y*second.y
        return result


    def divide(self, second):
        result = kasr()
        result.x = self.x*second.y
        result.y = self.y*second.x
        return result



    def show(self):
        return str(self.x) + '/' + str(self.y)

xx= list(map(int, input('enter kasr1: e.g. x/y\n').split('/')))
yy= list(map(int, input('enter kasr2: e.g. x/y\n').split('/')))
a = kasr(xx[0], xx[1])
b = kasr(yy[0], yy[1])
print('sum: %s\tsub: %s\tmul: %s\tdiv: %s'%((a.sum(b)).show(), (a.sub(b)).show(), (a.multiple(b)).show(), (a.divide(b)).show()))