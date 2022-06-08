import sqlite3, os
nomeBD = input ("Nome do Banco de Dados: ")
try:
  conector = sqlite3.connect(nomeBD)
  id = '1'
  cursor = conector.cursor()
  while id != '0':
    id = input("Digite o índice [0 - Sair]: ")
    if id != '0':
      cursor.execute("SELECT * FROM agenda WHERE id=?",(id))
      result = cursor.fetchall()
      achei = False
      for contato in result:
        print ("id: %d\nNome: %s \nFone: %s" % (contato))
        achei = True
      if not achei:
        print("Erro: Contato não Encontrado")
  cursor.close()
  conector.close()
except sqlite3.Error as error:
  print("ERRO: BD não encontrado")
  print("Erro: ", error)
  os.remove(nomeBD) # remove arquivo criado