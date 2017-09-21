from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Blast.Applications import NcbiblastpCommandline
from Bio.Blast import NCBIXML
import csv

def xml_extraction(input,output):
        res = open(output,"wb")
        writer = csv.writer(res)
        writer.writerow(["reference", "length", "SPU_ID", "e_value", "alignment"])
        result_handle = open(input)
        blast_records = NCBIXML.parse(result_handle)
        for blast_record in blast_records:
                if blast_record.alignments:
       	                a = str(blast_record.query) + ";" + "\t" + str(blast_record.query_letters) +  "\t" + str(blast_record.alignments[0].hit_def) + "\t"  + str(blast_record.alignments[0].hsps[0].expect) + "\t" + str(blast_record.alignments[0].hsps[0].bits) + "\t" + str(blast_record.alignments[0].hsps[0].match) + "\n"  
           	        print a
               	        res = open(output,"ab")
                        writer = csv.writer(res)
               	        writer.writerow([blast_record.query+";",blast_record.query_letters,blast_record.alignments[0].hit_def,blast_record.alignments[0].hsps[0].expect,blast_record.alignments[0].hsps[0].match])
                                        

        res.close() 


xml_extraction("egg_all_xml.xml","egg_result.csv")
