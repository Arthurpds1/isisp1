while True:
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    salario = float(input('Digite seu salario: '))
    sexo = input('Digite seu sexo: F ou M: ')
    ecivil = input('Digite seu estado civil: S(solteiro), C(casado), V(viuvo), D(Divorciado): ')
    
    if len(nome) < 3 or idade < 0 or idade > 150 or salario < 0 or sexo != ('F', 'M') or ecivil != ('S', 'C', 'V', 'D'):
        print('Valores invalidos.')
    else:
        print(nome,' ', idade,' ', salario,' ', sexo,' ', ecivil)
        break        