from CFGTree import CFGTree
from Node import simpleNode

class PredictTableMaker:
	def __init__(self, CFGTree, NonTerminalList, TerminalList):
		self.__treelist = CFGTree
		self.__nonterminallist = NonTerminalList
		self.__terminallist = TerminalList
		self.__predicttable = {}
		self.__AnsProductor()
		self.__TableEstablish()
		self.PrintTable()

	def __TableInitialize(self):
		for nonterminal in self.__nonterminallist:
			innertable = {}
			for terminal in self.__terminallist:
				innertable[terminal] = -1
			self.__predicttable[nonterminal] = innertable

	def __TableEstablish(self):
		self.__TableInitialize()
		for tree in self.__treelist:
			root = tree.getRoot().getRootVal()
			for rule in tree.getRoot().getRules():
				rule_number = rule.getRuleNumber()
				for ans in rule.getAns():
					self.__predicttable[root][ans] = rule_number

	def __AnsProductor(self):
		for tree in self.__treelist:
			for rule in tree.getRoot().getRules():
				answers = rule.getFirsts().copy()
				for element in rule.getFollows():
					if not element in answers:
						answers.append(element)
				rule.setAns(answers)

	def PrintTable(self):
		print("Predict Table:")
		for nonterminal in self.__nonterminallist:
			print("{%s: "% nonterminal, end = " ")
			for terminal in self.__terminallist:
				print("[%s: %d]"%(terminal, self.__predicttable[nonterminal][terminal]), end = " ")
			print("}")