import sqlite3
import os
import time
connection= sqlite3.connect("banco.db")
c=connection.cursor()

c.execute("CREATE TABLE IF NOT EXISTS conta (nome text,saldo integer)")


class conta:
	def __init__(self,nome):
		self.nome =nome
		self.saldo = 0
		c.execute("INSERT INTO conta (nome,saldo) VALUES ('{}','{}')".format(str(self.nome),int(self.saldo)))
		connection.commit()

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
	connection.commit()d


t =1
a = 1
while a==1:
	x = input("(1)criar conta: \n(2)status: \n(3)depositar: \n(4)saque: \n")
	if x == "1":
		os.system("cls")
		conta1 =  conta(input("digite o nome do novo usuario: "))
		print("conta criada!")
		time.sleep(t)
		os.system("cls")
	elif x=="2":
		os.system("cls")
		status(input("nome: "))
		time.sleep(t)
		os.system("cls")
		
	elif x == "3":
		os.system("cls")
		deposito(int(input("quantidade: " )),str(input("nome: ")))
		print("deposito realizado!")
		time.sleep(t)
		os.system("cls")
	elif x=="4":
		os.system("cls")
		saque(int(input("quantidade: " )),str(input("nome: ")))
		print("saque realizado!")
		time.sleep(t)
		os.system("cls")
	else:
		print("obrigado por usar meu sistema!")
		a = 2



input()