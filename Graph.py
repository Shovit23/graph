from matplotlib import pyplot as plt

tools = ['Metasploit','Nessus','Nmap','SqlMap','JohnTheRipper']

popularity = [92,100,82,80,90]

plt.bar(tools,popularity,color ='green')

plt.title('The Top Hacking Tools')

plt.xlabel('Tools')

plt.ylabel('Popularity')

plt.show()