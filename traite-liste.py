import unicodedata

def enlever_accents(input_str):
	nfkd_form = unicodedata.normalize('NFKD', input_str)
	return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

def enlever_paslettres(s):
	return "".join([c for c in s if c.isalpha()])

def bon_mot(x):
	return x == enlever_paslettres(enlever_accents(x)) and len(x) > 4

liste = open('liste.txt').read().split('\n')
liste_clean = [x for x in liste if bon_mot(x)]
print(len(liste), len(liste_clean))
open('liste-trim.txt', 'w').write('\n'.join(liste_clean))