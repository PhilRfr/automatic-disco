import secrets

def un_au_pif(liste):
	index = secrets.randbelow(len(liste))
	v = liste[index]
	del liste[index]
	return v

liste = open('liste-trim.txt').read().split('\n')
n = int(input('Combien ?'))
print(' '.join([un_au_pif(liste) for i in range(n)]))