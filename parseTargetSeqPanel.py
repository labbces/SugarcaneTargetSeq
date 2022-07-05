import sys
import openpyxl
from pathlib import Path
xlsx_file = Path(sys.argv[1])
wb_obj = openpyxl.load_workbook(xlsx_file)
sheet = wb_obj.active

amplicon2isoform={}
isoform2amplicon={}

for row in sheet.iter_rows():
    if not str(row[0].value).startswith("#"):
        isoforms=str(row[1].value).split(',')
        for iso in isoforms:
            if iso != '':
                # print(f'{row[0].value}\t{iso}')
                if not str(row[0].value) in amplicon2isoform.keys():
                    amplicon2isoform[row[0].value]={}
                amplicon2isoform[row[0].value][iso]=1
                if not iso in isoform2amplicon.keys():
                    isoform2amplicon[iso]={}
                isoform2amplicon[iso][str(row[0].value)]=1

# with open('numberOfIsoformsPerAmplicon.txt', 'w') as outNumberIsoform4amplicon:
#     outNumberIsoform4amplicon.write(f'Amplicon\tNumberOfIsoformsTargettedByAmplicon\n')
#     for amplicon in amplicon2isoform.keys():
#         numberIsoform4amplicon=len(amplicon2isoform[amplicon].keys())
#         outNumberIsoform4amplicon.write(f'{amplicon}\t{numberIsoform4amplicon}\n')

# with open('numberOfAmpliconsPerIsoform.txt', 'w') as outNumberAmpliconsPerIsoform:
#     outNumberAmpliconsPerIsoform.write(f'Isoform\tNumberOfAmpliconsTargetingIsoform\n')
#     for isoform in isoform2amplicon.keys():
#         numberAmpliconsPerIsoform=len(isoform2amplicon[isoform].keys())
#         outNumberAmpliconsPerIsoform.write(f'{isoform}\t{numberAmpliconsPerIsoform}\n')

print(f'There are {len(isoform2amplicon.keys())} identificadores diferentes de isoformas')
print(f'There are {len(amplicon2isoform.keys())} identificadores diferentes de amplicons')