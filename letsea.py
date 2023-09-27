#!/bin/env python3
from Bio import pairwise2


alignments = pairwise2.align.globalxx("ACCGT", "ACG",score_only=True)
print(alignments)


# crashlist=[('houhouhou', 'SHABOUGADA', 15.0), ('houhouhou', 'weee', 16.0), ('yapapa', 'houhouhou', 19.0), ('SHABOUGADA', 'weee', 20.0), ('Shabadouuuu', 'houhouhou', 20.0), ('Shabadouuuu', 'SHABOUGADA', 21.0), ('yapapa', 'SHABOUGADA', 23.0), ('yapapa', 'weee', 24.0), ('Shabadouuuu', 'weee', 25.0), ('yapapa', 'Shabadouuuu', 30.0)]

# for index,seq in enumerate(crashlist):
#     crashdico[crashlist[index][0]]=[]
# for index,szq in enumerate(crashlist):
#     crashdico[crashlist[index][0]].append(crashlist[index][2])
# print(crashdico)