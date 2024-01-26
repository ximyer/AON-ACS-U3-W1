string_S = 'GAGCCTACTAACGGGAT'
string_T = 'CATCGTAATGACGGCCT'

def hamming_distance(string_S, string_T):
     distance = 0
     lenght = len(string_S)
     for i in range(lenght):
          if string_S[i] != string_T[i]:
                    distance += 1
     return distance

hamming_mutations = hamming_distance('GAGCCTACTAACGGGA', 'CATCGTAATGACGGCCTGACTATA')
print(hamming_mutations)


'''
Sources: 
https://claresloggett.github.io/python_workshops/improved_hammingdist.html#:~:text=Hamming%20distance%20is%20the%20simplest,strings%20are%20the%20same%20lengths.
https://www.geeksforgeeks.org/hamming-distance-two-strings/
'''