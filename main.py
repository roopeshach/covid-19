#!us/usr/bin/python3
import requests
import bs4 as BeautifulSoup



def Country(name):
	URL = "https://www.worldometers.info/coronavirus/"

	page = requests.get(URL)
	tds = []
	soup = BeautifulSoup.BeautifulSoup(page.text, 'lxml')


	table = soup.find("table", id="main_table_countries_today")
	time= soup.find("div", {"style": "font-size:13px; color:#999; margin-top:5px; text-align:center"})
	headers = [head.text.replace(",Other","") for head in table.findAll('th')]
	table_rows = [row for row in table.findAll('tr')]
	results = [{headers[index]:cell.text for index,cell in enumerate(row.findAll("td"))} for row in table_rows ]

	for i in results:
		if "Country" in i:
			if i["Country"].lower().strip() == name.lower().strip():
				cases = i;

	

	print("""


			\033[1;0;40m Total Cases in """+name+""":\033[1;34;40m""" + cases['TotalCases'] + """
			\033[1;0;40m New cases in """+name+""":\033[1;35;40m """+ cases['NewCases'] +"""
			\033[1;0;40m Total recovered in """+name+""": \033[1;32;40m""" + cases['TotalRecovered']+"""
			\033[1;0;40m Total Deaths in """+name+""": \033[1;31;40m"""+ cases['TotalDeaths']+"""
			\033[1;0;40m New Deaths in """ + name + """:\033[1;91;40m """ + cases['NewDeaths']+"""
						\033[1;0;40m"""+time.text+"""

	""") 

print("""


   _____    ____   __      __  _____   _____               __    ___    
  / ____|  / __ \  \ \    / / |_   _| |  __ \             /_ |  / _ \   
 | |      | |  | |  \ \  / /    | |   | |  | |  ______     | | | (_) |  
 | |      | |  | |   \ \/ /     | |   | |  | | |______|    | |  \__, |  
 | |____  | |__| |    \  /     _| |_  | |__| |             | |    / /   
  \_____|  \____/      \/     |_____| |_____/              |_|   /_/    
                                                                        
                                                                        

  By: Roopesh Acharya					

	""")
Country("World")

Country(str(input("Enter Country:\t")))