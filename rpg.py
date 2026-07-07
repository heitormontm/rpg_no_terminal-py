import random

class Personagem:
    def __init__(self, nome, hp=100, ataque=15, defesa=5, pocoes=3):
        self.nome = nome
        self.hp_max = hp
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa
        self.pocoes = pocoes

    def esta_vivo(self):
        return self.hp > 0
    
    def status(self):
        barra = int((self.hp / self.hp_max) * 20)
        print(f'{self.nome} HP:[{'█' * barra}{'.'*(20-barra)}] {self.hp}/{self.hp_max}')

    def atacar(self, alvo):
        critico = random.random() < 0.2
        dano = self.ataque + random.randint(-3, 5)
        if critico:
            dano = int(dano * 1.8)
        dano_final = alvo.receber_dano(dano)
        msg = f'{self.nome} ataca {alvo.nome} causando {dano_final} de dano'
        if critico:
            msg += "(CRÍTICO!)"
        print(msg)
    
    def receber_dano(self, dano):
        dano_final = max(1, dano - self.defesa)
        self.hp = max(0, self.hp - dano_final)
        return dano_final
    
    def usar_pocao(self):
        if self.pocoes <= 0:
            print('Sem poções restantes!')
            return
        cura = 30
        self.hp = min(self.hp_max ,self.hp + cura)
        self.pocoes -= 1
        print(f'{self.nome} bebe uma poção e recupera {cura} de HP\
              ({self.pocoes} restantes)')

class Inimigo(Personagem):
    def ataque_especial(self, alvo):
        raise NotImplementedError
    
class Goblin(Inimigo):
    def __init__(self, nome='Goblin Sorrateiro'):
        super().__init__(nome, hp=60, ataque=10, defesa=2, pocoes=0)

    def ataque_especial(self, alvo):
        print(f'{self.nome} ataca duas vezes rapidamente!')
        for i in range(2):
            dano = random.randint(5, 10) #randint = random integer
            dano_final = alvo.receber_dano(dano)
            print(f'{self.nome} -> causa {dano_final} de dano')
    
class Dragao(Inimigo):
    def __init__(self, nome='Dragão Vermelho'):
        super().__init__(nome, hp=140, ataque=18, defesa=6, pocoes=0)

    def ataque_especial(self, alvo):
        dano = random.randint(25, 40)
        dano_final = alvo.receber_dano(dano)
        print(f'{self.nome} solta um sopro de fogo em {alvo.nome}!\
              ({dano_final} de dano)')

def turno_inimigo(inimigo, heroi):
    if random.random() < 0.35:
        inimigo.ataque_especial(heroi)
    else:
        inimigo.atacar(heroi)

dragao = Dragao()
goblin = Goblin()
print(isinstance(dragao, Inimigo), isinstance(goblin, Personagem))

