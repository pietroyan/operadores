# -*- coding: utf-8 -*-
"""AlunoMedia.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1d8UUlJpU6KduJpYf_W2JOO37Bj98DB0z
"""

aluno = input('Digite o nome do aluno: ')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
media = (n1+n2+n3)/3
if media >= 7:
    situacao = 'aprovado'
elif media >= 4:
    situacao = 'em recuperação'
else:
    situacao = 'reprovado'        
print(f'O aluno {aluno} está em situação {situacao} com média {media} ')