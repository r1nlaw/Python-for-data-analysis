def count_polypeptide_chains(rna_sequence):
    stop_codons = {'UAA', 'UAG', 'UGA'}
    chains = []
    current_chain = []
    
    i = 0
    while i < len(rna_sequence):
        codon = rna_sequence[i:i+3]
        if codon in stop_codons:
            if current_chain:
                chains.append(len(current_chain))
                current_chain = []
            else:
                chains.append(0)
        else:
            current_chain.extend(codon)
        i += 3
    
    return chains

rna_sequence = input().strip()
chains = count_polypeptide_chains(rna_sequence)
print(' '.join(map(str, chains)))