from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

#coleta os dados do json
with open('google.json') as f:
    json_google = json.load(f)

with open('google.json') as f:
    json_ap = json.load(f)
	
#abre o Chrome para realizar os testes
browser = webdriver.Chrome()

#pesquisa no google enquanto houver registros
for i in range (0, len (json_google["google-me"])):
	#Navega para o site do google
	browser.get('http://www.google.com.br/')
	
	#preenche o texto no campo de pesquisa e clica em enter
	element = browser.find_element_by_name('q')
	element.send_keys(json_google["google-me"][i])
	element.send_keys(Keys.ENTER)
	
	#coleta os 3 primeiros resultados
	l = 0
	while l<3:
		print(browser.find_elements_by_class_name('r')[l].text)
		json_ap["google-me"].insert(i,{json_google["google-me"][i]:browser.find_elements_by_class_name('r')[l].text} )
		l += 1

#salva os dados no novo json
with open('output.json', 'w') as json_outfile:
    json.dump(json_ap, json_outfile)
	
#encerra o browser
browser.quit()