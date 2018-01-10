
import sqlite3
import os
import time
connection= sqlite3.connect("banco.db")
c=connection.cursor()

c.execute("CREATE TABLE IF NOT EXISTS conta (nome text,saldo integer,senha integer)")


class conta:
	def __init__(self,nome,senha):
		self.nome =nome
		self.senha =senha
		self.saldo = 0
		c.execute("INSERT INTO conta (nome,saldo,senha) VALUES ('{}','{}','{}')".format(str(self.nome),int(self.saldo),int(self.senha)))
		connection.commit()

def login(nome,senha):
	c.execute("SELECT senha FROM conta WHERE nome='{}'".format(nome))
	sen = c.fetchone()
	if senha == int(sen[0]):
		print("logado!")
		time.sleep(1)
		os.system("clear")
		return 1
	else:
		print("tente novamente!")


def status(nome):
	c.execute("SELECT saldo FROM conta WHERE nome='{}'".format(nome))
	row = c.fetchone()
	print("saldo: "+str(row[0]))


def deposito(quantidade,nome):
	c.execute("SELECT saldo FROM conta WHERE nome='{}'".format(nome))
	row = c.fetchone()
	saldo = int(row[0])+quantidade
	c.execute("UPDATE conta SET saldo ='{}' WHERE nome ='{}'".format(int(saldo),str(nome)))
	connection.commit()
def saque(quantidade,nome):
	c.execute("SELECT saldo FROM conta WHERE nome='{}'".format(nome))
	row = c.fetchone()
	saldo = int(row[0])-quantidade
	c.execute("UPDATE conta SET saldo ='{}' WHERE nome ='{}'".format(int(saldo),str(nome)))
	connection.commit()

if input("voce e registrado ?") =="sim":
	os.system("clear")
	a = login(str(input("nome: \n")),int(input("senha: \n")))
else:
	a =1 
t =1
while a==1:
	x = input("(1)criar conta: \n(2)status: \n(3)depositar: \n(4)saque: \n(enter)sair: \n")
	if x == "1":
		os.system("clear")
		conta1 =  conta(str(input("nome: \n")),int(input("senha: \n")))
		print("conta criada!")
		time.sleep(t)
		os.system("clear")
	elif x=="2":
		os.system("clear")
		status(input("nome: "))
		time.sleep(t)
		os.system("clear")
		
	elif x == "3":
		os.system("clear")
		deposito(int(input("quantidade: " )),str(input("nome: ")))
		print("deposito realizado!")
		time.sleep(t)
		os.system("clear")
	elif x=="4":
		os.system("clear")
		saque(int(input("quantidade: " )),str(input("nome: ")))
		print("saque realizado!")
		time.sleep(t)
		os.system("clear")
	else:
		print("obrigado por usar meu sistema!")
		a = 2
