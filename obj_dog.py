from dog_class import Dog
# para criar o objeto, utilizamos a variável
# pastor e realizamos o processo de
# instanciação da classe Dog.
# foi passado o nome e a idade
pastor = Dog("Mel",4)
# acessamos o método data_dog que mostra
# os dados do cachorro
pastor.data_dog()
pastor.sit()
pastor.roll_over()
print(pastor.__class__)
print(pastor.__dict__)

