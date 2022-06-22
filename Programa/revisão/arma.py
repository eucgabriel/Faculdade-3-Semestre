'''class Arma:
    def __init__(self, tambor, municao):
        self.gatilho = False
        self.tambor = tambor
        self.trava = False
        self.municao = municao

    def engatilhar(self):
        self.trava = True

    def recarregar(self):
        self.tambor = 6
        self.trava = False

    def atirar(self):
        if self.trava == True:
            if self.tambor > 0:
                self.tambor -=1
                self.trava = False
            else:
                 self.recarregar()
        else:
            self.recarregar'''

            