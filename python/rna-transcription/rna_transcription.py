def to_rna(dna):  # type: (str) -> str
    """Given a DNA strand, returns its RNA complement"""

    dna_to_rna_map = {
        "G": "C",
        "C": "G",
        "T": "A",
        "A": "U"
    }

    rna = ''
    for nucleotide in dna:
        if nucleotide not in dna_to_rna_map:
            return ''

        rna += dna_to_rna_map[nucleotide]

    return rna
