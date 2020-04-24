n1=int(input('Digite um valor'))
n2=int(input('Digite outro valor'))
s= n1+n2
su=n1-n2
m=n1*n2
d=n1/n2
di=n1//n2
sob=n1%n2
e=n1**n2
print('A soma entre {0} e {1} é {2} \n A subtração entre {0} e {1} é {3} \n A multiplicação entre {0} e {1} é {4} \n A divisão entre {0} e {1} é {5:.3f} \n A divisão inteira entre {0} e {1} é {6:.3f} \n A sobra da divisão entre {0} e {1} é {7} \n O resultado de {0} elevado a {1} é {8}'.format(n1, n2, s, su, m, d, di, sob, e))