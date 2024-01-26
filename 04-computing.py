gene_0808 = 'CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT'
gene_5959 = 'CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC'
gene_6404 = 'CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG'


def compute_content(gene, gene_name):
     computing_c = gene.count('C')
     computing_g = gene.count('G')
     presence = ((computing_c + computing_g) / len(gene)) * 100
     return presence


results={
     'gene_0808' : compute_content(gene_0808, 'gene_0808'),
     'gene_5959' : compute_content(gene_5959, 'gene_5959'),
     'gene_6404' : compute_content(gene_6404, 'gene_6404'),
}


highest_percentage = max(results, key=results.get)
print(f'The Rosalind gene with the highest presence of G and C amino acids is: {highest_percentage} with {results[highest_percentage]} %')

