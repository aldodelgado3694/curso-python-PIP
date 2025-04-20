import csv

def read_csv(path):
  with open(path, 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    header = next(reader)
    data = []
    #print(header)
    for row in reader:
      #print('***' * 5)
      iterable = zip(header, row)
      country_dict = {key: value for key, value in iterable}
      #print(country_dict)
      data.append(country_dict)
      #print(row)
      
  return data


if __name__ == '__main__':
  data = read_csv('./app/data.csv')
  print(data[1])
