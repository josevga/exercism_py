def to_rna(dna_strand):
    transcription = {
        "G": "C", 
        "C": "G", 
        "T": "A", 
        "A": "U"
    }
    return "".join(transcription[nucl] for nucl in dna_strand)
