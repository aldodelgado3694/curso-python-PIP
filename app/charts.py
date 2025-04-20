import matplotlib.pyplot as plt

def generate_bar_chart(labels = ['a', 'b', 'c'], values = [10, 200, 80], name = "Pais"):
  fig, ax = plt.subplots()
  ax.bar(labels, values)
  #plt.show()
  plt.savefig('bar_{}.png'.format(name))
  plt.close()

def generate_pie_chart(labels = ['a', 'b', 'c'], values = [10, 200, 80], name = "Pais"):
  fig, ax = plt.subplots()
  ax.pie(values, labels=labels)
  ax.axis('equal')
  #plt.show()
  plt.savefig("pie_{}.png".format(name))
  plt.close()

if __name__ == '__main__':
  generate_pie_chart()