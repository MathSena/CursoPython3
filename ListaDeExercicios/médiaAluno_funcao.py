"""
Faça	uma	função	que calcule a	média	de	um	aluno	de	acordo	com	o	critério	definido
neste	curso.	Além	disso,	 faça	uma	segunda	 função	que	informe	o	status	do	aluno	de
acordo	com	a	tabela	a	seguir:
Nota	acima	de	6	à “Aprovado”
Nota	entre	4	e	6	à Conceito	“Verificação	Suplementar”
Nota	abaixo	de	4	à Conceito	“Reprovado”

"""
def notasAluno(nota):
    nota = int(input(nota))
    return nota

def statusAluno(notasAluno):
    if notasAluno >6:
        return 'Aprovado'
    elif notasAluno >=4 and notasAluno<=6:
        return 'Verificação	Suplementar'
    else:
        return 'Reprovado'

print(statusAluno(9))