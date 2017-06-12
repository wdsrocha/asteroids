# Aplica força no corpo da nave, alterando sua aceleração
def ativa_propulsao(nave):
    angulo = math.radians(nave['corpo']['direcao'])
    forca = fisica.cria_vetor_unitario(angulo)
    nave['corpo'] = fisica.aplica_forca(nave['corpo'], forca)
    return nave

# Tudo daqui pra baixo falta arrumar
def atualiza_nave(nave):
   nave['corpo'] = fisica.atualiza_corpo(nave['corpo']) 
    

def desenha_nave(nave):
    pass
