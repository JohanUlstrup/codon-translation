"""Module for translating DNA to proteins via codons."""

CODON_MAP = {'TTT': 'F', 'TTC': 'F', 'TTA': 'L', 'TTG': 'L',
             'TCT': 'S', 'TCC': 'S', 'TCA': 'S', 'TCG': 'S',
             'TAT': 'Y', 'TAC': 'Y', 'TAA': '*', 'TAG': '*',
             'TGT': 'C', 'TGC': 'C', 'TGA': '*', 'TGG': 'W',
             'CTT': 'L', 'CTC': 'L', 'CTA': 'L', 'CTG': 'L',
             'CCT': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
             'CAT': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
             'CGT': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
             'ATT': 'I', 'ATC': 'I', 'ATA': 'I', 'ATG': 'M',
             'ACT': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
             'AAT': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
             'AGT': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
             'GTT': 'V', 'GTC': 'V', 'GTA': 'V', 'GTG': 'V',
             'GCT': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
             'GAT': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
             'GGT': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'}


def split_codons(dna: str) -> list[str] | None:
    """Split a DNA string into a list of triplets.

    If the length of the string is a multiple of tree, then this
    function splits the string into non-overlapping triplets.

    >>> split_codons('aaacccgggttt')
    ['aaa', 'ccc', 'ggg', 'ttt']

    If the string length is not a multiple of three, the function
    should return `None`. (There are better ways at reporting
    errors, but we will see those later).

    >>> split_codons("acgt") is None
    True
    """
    codons=[]
    if len(dna)%3 ==0:
       for i in range(0,len(dna)-(2),3):
            codons.append(dna[i:i+3])
       return codons
    return None
    


def translate_codons(codons: list[str]) -> list[str]:
    """Translate a list of codons (triplets) into their corresponding
    amino acid sequence.

    >>> translate_codons(['TGT', 'TGC', 'TGA'])
    ['C', 'C', '*']

    The function must be able to handle both upper and lower case
    strings.

    >>> translate_codons(['tgt', 'tgc', 'tga'])
    ['C', 'C', '*']

    If the `codons` list contain anything that isn't a valid codon,
    i.e. not in the CODON_MAP when translated into upper case, the
    function should return `None`.

    >>> translate_codons(["acg", "ac", "gca"]) is None
    True

    """     
    # FIXME: Implement the function
    y=[]
    output=[]
    for i in codons:
        x= i.upper()
        y.append(x)
    
    for i in y:
        if i in CODON_MAP:
            output.append(CODON_MAP[i])
            
        else: 

            return None #"somthing rong with the sequens"
    return output




def translate_dna(dna: str) -> str:
    """Translate a DNA string into its corresponding amino acid string.

    >>> translate_dna('TGTTGCTGA')
    'CC*'
    >>> translate_dna('tgttgctga')
    'CC*'

    If the sequence does not have a length that is a multiple of three, of if
    any of the triplets in it are not valid codons (when in uppercase), the function
    should return `None`.

    >>> translate_dna('tgtgctg') is None
    True

    """
    # FIXME: Implement the function'
    split_codon = split_codons(dna)
    if split_codon == None:
        return None
    translated_codon = translate_codons(split_codon)
    if translated_codon == None:
        return None
     
    output_string = "".join(translated_codon)


    return output_string

