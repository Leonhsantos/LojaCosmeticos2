# A loja de cosméticos ficou muito feliz com seu trabalho e chamaram você novamente! Dessa vez, eles precisam que você atualize o array de produtos.
# Agora, eles estão vendendo rímel ao invés de batons, e cremes hidratantes no lugar de loções. 
#  Além disso, ficaram sem delineadores, então precisam que você remova ele da lista de produtos.
# Imprima a nova lista no terminal para verificar que as alterações foram realizadas corretamente.
# Como desafio, adicione dois novos produtos da sua escolha à lista. 


#Lista original
lista_produtos = ['máscaras faciais', 'batons', 'esmaltes', 'perfumes', 'loções', 'xampus', 'sabonetes', 'delineadores'] 



#Lista alterando os batons e loções
lista_produtos[1], lista_produtos[4] = 'rímel', 'hidratantes'
print(lista_produtos)


# #Lista removendo o delineador
lista_produtos.pop()
print(lista_produtos)

#Lista adicionando 2 produtos
lista_produtos.append('Desodorante')
lista_produtos.append('Sombra')
print(lista_produtos)