
# Задание 1
# Реализовать класс Person, у которого должно быть два публичных поля: age и name. 

# Также у него должен быть следующий набор методов: 
# know(person), который позволяет добавить другого человека в список знакомых. 
# И метод is_known(person), который возвращает знает ли знакомы ли два человека.


class Person(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.contact_list = []
	
	def add(self, contact):
		self.contact_list.append(contact)
		print('{} has added {}, {} to his contacts.'.format(self.name, contact.name, contact.age))
		print('Use .contacts() to see full contact list.', '\n')

	def check(self, contact):
		if contact in self.contact_list:
			print('Yes, {} is known to {}.'.format(contact.name, self.name))
		elif self in contact.contact_list:
			print('Yes, {} is known to {}.'.format(contact.name, self.name))
		else:
			print('No, {} isn\'t known to {}.'.format(contact.name, self.name))

	def contacts(self):
		print('{}\'s contact list: '.format(self.name))
		for contact in self.contact_list:
			print('{}, {} '.format(contact.name, contact.age))
		print('\n')

person1 = Person('Dima', 38)
person2 = Person('Oleg', 35)
person3 = Person('Yulya', 27)
person4 = Person('Tanya', 30)

person1.add(person2)
person1.add(person3)
person1.contacts()

person1.check(person2)
person2.check(person1)
person1.check(person4)



# Задание 2
# Есть класс, который выводи информацию в консоль: `Printer`, у него есть метод: log(*values). 
# Написать класс FormattedPrinter, который выводит в консоль информацию, окружая ее строками из *


class Printer:
	print('Use .log(text) to print the text', '\n')
	def log(self, *text):
		for t in text:
			print(t)


class FormattedPrinter(Printer):
	print('Use .form_log(text) to print formatted text', '\n')
	def form_log(self, *text):
		for t in text:
			print('\n', len(t) * '*', '\n', t, '\n', len(t) * '*', '\n')


my_text = FormattedPrinter()

my_text.log('first log', 'second log')

my_text.form_log('first log', 'second log')




# Задание 3
# Написать класс Animal и Human, сделать так, 
# чтобы некоторые животные были опасны для человека (хищники, ядовитые). Другие - нет. 
# За что будет отвечать метод is_dangerous(animal)




class Animal:
	danger = False
	def __init__(self, name):
		self.name = name
		pass
		
class Wild_Predators(Animal):
	danger = True

class Venomous(Animal):
	danger = True


class Human:

	def is_dangerous(self, animals):
		for animal in animals:
			if animal.danger == True:
				print('Human, beware of {}, it\'s dangerous!'.format(animal.name))
			else:
				print('It\'s OK, {} is not dangerous!'.format(animal.name))



animal1 = Animal('cat')
animal2 = Wild_Predators('lion')
animal3 = Venomous('cobra')

human = Human()
human.is_dangerous(animals = [animal1, animal2, animal3])



# Version 2:

class Human:
	def __init__(self, dangerous_animals):
		self.dangerous_animals = dangerous_animals
	


class Animal:
	def __init__(self, animal, animal_class):
		self.animal = animal
		self.animal_class = animal_class

	def is_danderous(self, animal_class):
		if animal_class in human.dangerous_animals:
			print('Human, beware of {}, it\'s dangerous!'.format(self.animal))
		else:
			print('It\'s OK, {} is not dangerous!'.format(self.animal))


human = Human(dangerous_animals = ['wild_predator', 'venomous_snake'])


animal1 = Animal('lion', 'wild_predator')
animal2 = Animal('cat', 'pet')

animal1.is_danderous('wild_predator')
animal2.is_danderous('pet')


