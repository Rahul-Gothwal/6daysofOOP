#how to instantiate a class

#class classname:
#	pass

class team:
	def __init__(self, first, last, role): #init method
		self.first = first #instance variables
		self.last = last
		self.role = role
		self.email = first + '.' + last +'@team.dev'

	def fullname(self):
		return '{} {}'.format(self.first, self.last)

member_1 = team('rahul', 'gothwal', 'head')
member_2 = team('yugam', 'sachdeva', 'head')
member_3 = team('prafull', 'anand', 'head')

print(member_1.email)
print(team.fullname(member_1))
print(member_2.email)
print(team.fullname(member_2))
print(member_3.email)
print(team.fullname(member_3))