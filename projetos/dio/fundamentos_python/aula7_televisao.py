class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 10

    def power(self):
        if self.ligada:
            self.ligada = False
        else:
            self.ligada = True

    def aumenta_canal(self): 
        if self.ligada:
            self.canal += 1

    def diminue_canal(self):
        if self.ligada:
            self.canal -= 1

if __name__ == '__main__': # serve para proteger a aplicação.
    televisao = Televisao()
    print(f'Televisão está ligada? {televisao.ligada}')
    televisao.power()
    print(f'Televisão está ligada? {televisao.ligada}')
    televisao.power()
    print(f'Televisão está ligada? {televisao.ligada}')
    televisao.power()
    print(f'Televisão está ligada? {televisao.ligada}')
    print(f'Canal: {televisao.canal}')
    televisao.aumenta_canal()
    televisao.aumenta_canal()
    print(f'Canal: {televisao.canal}')
    televisao.diminue_canal()
    print(f'Canal: {televisao.canal}')