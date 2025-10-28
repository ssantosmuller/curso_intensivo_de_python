lugares = ['italia', 'nova iorque', 'buenos aires', 'roma', 'azerbaijão']
print("Ordem  original: ",lugares)
print("Ordem alfabética: ",sorted(lugares))
print("Manteve sua ordem original:", lugares)
print("A lista em ordem alfabética inversa: ",sorted(lugares, reverse = True))
print("Manteve sua ordem original:", lugares)
lugares.reverse()
print("Usando reverse: ", lugares)