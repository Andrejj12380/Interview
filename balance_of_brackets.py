# coding=utf-8
from main import Stack

opened_list = ['(', '[', '{']
closed_list = [')', ']', '}']


def check_brackets(data: str) -> str:
	stack = Stack()
	for bracket in data:
		if bracket in opened_list:
			stack.push(bracket)
		elif bracket in closed_list:
			position = closed_list.index(bracket)
			if (stack.isEmpty() == False) and (opened_list[position] == stack.stack[stack.size() - 1]):
				stack.pop()
			else:
				return 'Несбалансированно'
	if stack.isEmpty():
		return 'Сбалансированно'


print("(((([{}])))) ------ ", check_brackets('(((([{}]))))'))
print("[([])((([[[]]])))]{()}  ------  ", check_brackets('[([])((([[[]]])))]{()}'))
print("{{[(])]}}  ------  ", check_brackets('{{[(])]}}'))
print("{{[()]}}  ------  ", check_brackets('{{[()]}}'))
print("}{}  ------  ", check_brackets('}{}'))
print("[[{())}]  ------  ", check_brackets('[[{())}]'))