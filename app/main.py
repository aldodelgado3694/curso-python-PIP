import read_csv
import charts
import utils

def get_population(country_data, heads):
  population = []
  for population_year in heads:
    population.append(int(country_data[0][population_year]))
  return population
seguir = True

while seguir:
  data = read_csv.read_csv("./app/data.csv")
  listaPaises = (list(map(lambda country: country['Country'], data)))
  pais = input("Introduce el pais: " + str(listaPaises) + "\n")
  while pais not in listaPaises:
    print("El pais no existe \n")
    pais = input("Introduce el pais: \n")
  county_data = utils.population_by_country(data, pais)

  heads = ['2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population','1970 Population']
  print(county_data)
  print('***' * 5)
  print(heads)
  values = get_population(county_data, heads)
  print(values)
  heads  = list(map(lambda head: head.split(' ')[0], heads))
  tipo = input("Intrduce el tipo de grafico (default=bar): (bar o pie) \n")
  if 'BAR' == tipo.upper():
    charts.generate_bar_chart(heads, values, pais)
  else:
    charts.generate_pie_chart(heads, values, pais)
  
  seguir = input("Salir: \n").upper() != "SALIR"


#RETO 2

'''
data = read_csv.read_csv("./app/data.csv")
heads = list(map(lambda country: country['CCA3'], data))
values = list(map(lambda country: country['World Population Percentage'], data))
print(heads)
print(values)
charts.generate_pie_chart(heads, values)
'''

#RETO 1
'''
def get_population(country_data, heads):
  population = []
  for population_year in heads:
    population.append(int(country_data[0][population_year]))
  return population

data = read_csv.read_csv("./app/data.csv")
county_data = utils.population_by_country(data, 'Argentina')
heads = ['2022 Population','2020 Population','2015 Population','2010 Population','2000 Population','1990 Population','1980 Population','1970 Population']
print(county_data)
print('***' * 5)
print(heads)
values = get_population(county_data, heads)
print(values)
heads  = list(map(lambda head: head.split(' ')[0], heads))
charts.generate_bar_chart(heads, values)
'''