import pandas as pd
import csv
#find all protins with 2 fold change from a signle experiment/control group
def Find2FCInOnlyOneGroup(ctrlIndex, IPIndex, InFile, OutFile):
    df = pd.read_csv(InFile, delimiter='\t', na_values=['nan'], engine='python')
    tuples = [x for x in df.values]
    #print tuples[0][ctrlIndex]
    #write proteins with 2FC or larger to the outfile
    out = open(OutFile, 'wb')
    writer = csv.writer(out)
    
    for item in tuples:
        IPSignal = float(item[IPIndex])
        ctrlSignal = float(item[ctrlIndex])
        try:
            foldChange = IPSignal / ctrlSignal
            if foldChange >= 2.0:
                writer.writerow([item[1], foldChange])
        except ZeroDivisionError:
            writer.writerow([item[1], "infinite"])

    out.close()

if __name__ == "__main__":
    Find2FCInOnlyOneGroup(5, 8, 'Venn.csv', '2FCProteins_3.csv')
