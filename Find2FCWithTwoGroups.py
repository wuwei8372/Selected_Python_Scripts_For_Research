import pandas as pd
import csv
##find all protins with 2 fold change from a signle experiment/control group
def Find2FCInTwoGroup(ctrlIndex1, ctrlIndex2, IPIndex1, IPIndex2, InFile, OutFile):
    df = pd.read_csv(InFile, delimiter='\t', na_values=['nan'])
    tuples = [tuple(x) for x in df.values]
    #write proteins with 2FC or larger to the outfile
    out = open(OutFile, 'wb')
    writer = csv.writer(out)
    
    for item in tuples:
        try:
            foldChange = ((item[IPIndex1] + item[IPIndex2])*1.0) / ((item[ctrlIndex1] + item[ctrlIndex2])*1.0)
            if foldChange >= 2.0:
                writer.writerow([item[1], foldChange])
        except ZeroDivisionError:
            writer.writerow([item[1], "infinite"])

    out.close()

if __name__ == "__main__":
    Find2FCInTwoGroup(3, 4, 6, 7, 'Venn.csv', '2FCProteins_1and3.csv')
