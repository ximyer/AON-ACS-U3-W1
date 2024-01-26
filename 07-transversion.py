transition = {'A':'G', 'G':'A', 'T':'C', 'C':'T'}
transversion = {'A':('T','C'), 'G':('T','C'), 'T':('A','G'), 'C':('A','G')}

def trans(rosalind_0209, rosalind_2200):
     x = 0
     y = 0
     for i,j in zip(rosalind_0209, rosalind_2200):
          if transition[i] == j:
               x += 1 
          elif j in transversion[i]:
               y += 1
     return (x/y)

rosalind_0209 = 'GCAACGCACAACGAAAACCCTTAGGGACTGGATTATTTCGTGATCGTTGTAGTTATTGGAAGTACGGGCATCAACCCAGTT'
rosalind_2200 = 'TTATCTGACAAAGAAAGCCGTCAACGGCTGGATAATTTCGCGATCGTGCTGGTTACTGGCGGTACGAGTGTTCCTTTGGGT'

print(trans(rosalind_0209, rosalind_2200))


'''
Sources:
https://www.mun.ca/biology/scarr/Transitions_vs_Transversions.html#:~:text=Transitions%20are%20interchanges%20of%20two,ring%20%26%20two%2Dring%20structures.
https://blog.csdn.net/weixin_45848873/article/details/135143315

'''
