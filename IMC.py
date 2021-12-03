nome= ['-Kayky dos Sonhos', 
'-Matheus Furtado', 
'-Marcos Brito', 
'-Antonio Lascivia ']

altura= [1.80, 1.65, 1.70, 1.90]
peso= [64.0, 70.0, 80.0, 100.0]
imc=[0,0,0,0]

imc[0] += peso[0]/(altura[0] * altura[0])
imc[1] += peso[1]/(altura[1] * altura[1])
imc[2 ]+= peso[2]/(altura[2] * altura[2])
imc[3] += peso[3]/(altura[2] * altura[3])



print(nome[0], 
'\nAltura:',altura[0],'\nPeso: ',peso[0],'KG''\nMassa Corpórea:', imc[0])
print(nome[1], '\nAltura:', altura[1], '\nPeso:', peso[1],'KG''\nMassa Corpórea:',imc[1])
print(nome[2], '\nAltura:', altura[2], '\nPeso:', peso[2],'KG''\nMassa Corpórea:',imc[2])
print(nome[3], '\nAltura:', altura[3], '\nPeso:', peso[3],'KG''\nMassa Corpórea:',imc[3])