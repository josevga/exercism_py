

def proteins(strand):
    """Translate RNA sequences into proteins"""

    translate = {
        "AUG": "Methionine", 
        "UUU": "Phenylalanine", 
        "UUC": "Phenylalanine", 
        "UUA": "Leucine", 
        "UUG": "Leucine", 
        "UCU": "Serine", 
        "UCC": "Serine", 
        "UCA": "Serine", 
        "UCG": "Serine", 
        "UAU": "Tyrosine", 
        "UAC": "Tyrosine", 
        "UGU": "Cysteine", 
        "UGC": "Cysteine", 
        "UGG": "Tryptophan", 
        "UAA": "", 
        "UAG": "", 
        "UGA": ""
    }
    proteins = []
    for condon in (strand[i:i + 3] for i in range(0, len(strand), 3)):
        protein = translate[condon]
        if protein:
            if not protein in proteins:
                proteins.append(protein)
        else:
            break

    return proteins
