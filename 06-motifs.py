string = 'GATATATGCATATACTT'
substring = 'ATAT'

for position in range(len(string)):
     if string[position:].startswith(substring):
          print(position+1)
