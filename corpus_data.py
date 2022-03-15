# -*- coding: utf-8 -*-

from os import listdir
from os.path import isfile, join
import re
import csv



def transform_corpus_data(input_file, output_file):
    """
    This method transforms the corpus data into a csv file with two rows:
        
    text of instance | title of corresponding text file
    ----------------------------------------------------
                     |
                     |
                     
    The corpus data (input) was downloaded using the GridExporter
    and due to pre-processing using Excel looks like this:

    car hit a blue car from behind when a passerbyer 's ball flew into the road and another pedestrian 's dog 
    USbi01FT_fwE


     passerbyer 's ball flew into the road and another pedestrian 's dog started barker and also jumped into the road . 
    USbi01FT_fwE
     """   
        
    with open(input_file, "r", encoding="utf8") as inp, open(output_file, "w", encoding="utf8", newline='') as csv_out:
        lines = inp.readlines()
        meta, examples = [],[]
        for line in lines:
            if re.match('^\w+', line):
                line = line.replace("\n", "")
                meta.append(line)
            else:
                if not re.findall("\w+", line) == []:
                    line = line.replace("\n", "")
                    examples.append(line)
                else:
                    continue
        #write csv file
        writer = csv.writer(csv_out)
        for exe, docname in zip(examples,meta):
            writer.writerow([exe,docname])
            
def count(subcorp, list_s, list_of):
    """

    Parameters
    ----------
    subcorp : str
        Specifies the subcorpus 
        (values: EN, RUEG, GR, DE, wr, spo, form, inform,..).
    list_s : list 
        Contains the list of the corresponding text file names 
        of all s-genitives in the RUEG-EN corpus.
    list_of : list
        Contains the list of the corresponding text file names 
        of all of-genitives in the RUEG-EN corpus.

    Returns
    -------
    list
        The frequencies of s-genitives and of-genitives in
        the respective subcorpus.

    """
    if subcorp=="EN":
        s_count, of_count = 0,0
        for s in list_s:
            if s.startswith("USmo"):
                s_count += 1
        for of in list_of:
            if of.startswith("USmo"):
                of_count += 1
        return ["EN mono all", s_count, of_count, s_count+of_count]
    elif subcorp=="RUEG":
        s_count, of_count = 0,0
        for s in list_s:
            s_count += 1
        for of in list_of:
            of_count += 1
        return ["RUEG", s_count, of_count, s_count+of_count]
    elif subcorp=="GR":
        s_count, of_count = 0,0
        for s in list_s:
            if "G_" in s:
                s_count += 1
        for of in list_of:
            if "G_" in of:
                of_count += 1
        return ["GR mono all", s_count, of_count, s_count+of_count]
    elif subcorp=="DE":
        s_count, of_count = 0,0
        for s in list_s:
            if "D_" in s:
                s_count += 1
        for of in list_of:
            if "D_" in of:
                of_count += 1
        return ["DE mono all", s_count, of_count, s_count+of_count]   
    elif subcorp=="wr":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("_.w", s) == []:
                s_count += 1
        for of in list_of:
            if not re.findall("_.w", of) == []:
                of_count += 1
        return ["Written", s_count, of_count, s_count+of_count]
    elif subcorp=="spo":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("_.s", s) == []:
                s_count += 1
        for of in list_of:
            if not re.findall("_.s", of) == []:
                of_count += 1
        return ["Spoken", s_count, of_count, s_count+of_count]    
    elif subcorp=="form":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("_f", s) == []:
                s_count += 1
        for of in list_of:
            if not re.findall("_f", of) == []:
                of_count += 1
        return ["Formal", s_count, of_count, s_count+of_count]
    elif subcorp=="inform":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("_i", s) == []:
                s_count += 1
        for of in list_of:
            if not re.findall("_i", of) == []:
                of_count += 1
        return ["Informal", s_count, of_count, s_count+of_count]
    elif subcorp=="fem":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("F._", s) == []:
                s_count += 1
        for of in list_of:
            if not re.findall("F._", of) == []:
                of_count += 1
        return ["Gender: F", s_count, of_count, s_count+of_count]
    elif subcorp=="masc":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("M._", s) == []:
                s_count += 1
        for of in list_of:
            if not re.findall("M._", of) == []:
                of_count += 1
        return ["Gender: M", s_count, of_count, s_count+of_count]
    ############################
    elif subcorp=="ENwr":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("_.w", s) == []:
                if s.startswith("USmo"):
                    s_count += 1
        for of in list_of:
            if not re.findall("_.w", of) == []:
                if of.startswith("USmo"):
                    of_count += 1
        return ["English x Written", s_count, of_count, s_count+of_count]  
    elif subcorp=="ENspo":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("_.s", s) == []:
                if s.startswith("USmo"):
                    s_count += 1
        for of in list_of:
            if not re.findall("_.s", of) == []:
                if of.startswith("USmo"):
                    of_count += 1
        return ["English x Spoken", s_count, of_count, s_count+of_count]  
    elif subcorp=="GRwr":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("_.w", s) == []:
                if "G_" in s:
                    s_count += 1
        for of in list_of:
            if not re.findall("_.w", of) == []:
                if "G_" in of:
                    of_count += 1
        return ["Greek x Written", s_count, of_count, s_count+of_count]  
    elif subcorp=="GRspo":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("_.s", s) == []:
                if "G_" in s:
                    s_count += 1
        for of in list_of:
            if not re.findall("_.s", of) == []:
                if "G_" in of:
                    of_count += 1
        return ["Greek x Spoken", s_count, of_count, s_count+of_count]  
    elif subcorp=="DEwr":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("_.w", s) == []:
                if "D_" in s:
                    s_count += 1
        for of in list_of:
            if not re.findall("_.w", of) == []:
                if "D_" in of:
                    of_count += 1
        return ["German x Written", s_count, of_count, s_count+of_count]  
    elif subcorp=="DEspo":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("_.s", s) == []:
                if "D_" in s:
                    s_count += 1
        for of in list_of:
            if not re.findall("_.s", of) == []:
                if "D_" in of:
                    of_count += 1
        return ["German x Spoken", s_count, of_count, s_count+of_count]  
    #################################################################
    elif subcorp=="ENform":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("_f", s) == []:
                if s.startswith("USmo"):
                    s_count += 1
        for of in list_of:
            if not re.findall("_f", of) == []:
                if of.startswith("USmo"):
                    of_count += 1
        return ["English x Formal", s_count, of_count, s_count+of_count]  
    elif subcorp=="ENinform":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("_i", s) == []:
                if s.startswith("USmo"):
                    s_count += 1
        for of in list_of:
            if not re.findall("_i", of) == []:
                if of.startswith("USmo"):
                    of_count += 1
        return ["English x Informal", s_count, of_count, s_count+of_count]  
    elif subcorp=="GRform":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("_f", s) == []:
                if "G_" in s:
                    s_count += 1
        for of in list_of:
            if not re.findall("_f", of) == []:
                if "G_" in of:
                    of_count += 1
        return ["Greek x Formal", s_count, of_count, s_count+of_count]  
    elif subcorp=="GRinform":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("_i", s) == []:
                if "G_" in s:
                    s_count += 1
        for of in list_of:
            if not re.findall("_i", of) == []:
                if "G_" in of:
                    of_count += 1
        return ["Greek x Informal", s_count, of_count, s_count+of_count]  
    elif subcorp=="DEform":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("_f", s) == []:
                if "D_" in s:
                    s_count += 1
        for of in list_of:
            if not re.findall("_f", of) == []:
                if "D_" in of:
                    of_count += 1
        return ["German x Formal", s_count, of_count, s_count+of_count]  
    elif subcorp=="DEinform":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("_i", s) == []:
                if "D_" in s:
                    s_count += 1
        for of in list_of:
            if not re.findall("_i", of) == []:
                if "D_" in of:
                    of_count += 1
        return ["German x Informal", s_count, of_count, s_count+of_count] 
    #############################################################################
    elif subcorp=="ENfem":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("F._", s) == []:
                if s.startswith("USmo"):
                    s_count += 1
        for of in list_of:
            if not re.findall("F._", of) == []:
                if of.startswith("USmo"):
                    of_count += 1
        return ["English x Fem", s_count, of_count, s_count+of_count]  
    elif subcorp=="ENmasc":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("M._", s) == []:
                if s.startswith("USmo"):
                    s_count += 1
        for of in list_of:
            if not re.findall("M._", of) == []:
                if of.startswith("USmo"):
                    of_count += 1
        return ["English x Masc", s_count, of_count, s_count+of_count]  
    elif subcorp=="GRfem":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("F._", s) == []:
                if "G_" in s:
                    s_count += 1
        for of in list_of:
            if not re.findall("F._", of) == []:
                if "G_" in of:
                    of_count += 1
        return ["Greek x Fem", s_count, of_count, s_count+of_count]  
    elif subcorp=="GRmasc":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("M._", s) == []:
                if "G_" in s:
                    s_count += 1
        for of in list_of:
            if not re.findall("M._", of) == []:
                if "G_" in of:
                    of_count += 1
        return ["Greek x Masc", s_count, of_count, s_count+of_count]  
    elif subcorp=="DEfem":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("F._", s) == []:
                if "D_" in s:
                    s_count += 1
        for of in list_of:
            if not re.findall("F._", of) == []:
                if "D_" in of:
                    of_count += 1
        return ["German x Fem", s_count, of_count, s_count+of_count]  
    elif subcorp=="DEmasc":
        s_count, of_count = 0,0
        for s in list_s:
            if not re.findall("M._", s) == []:
                if "D_" in s:
                    s_count += 1
        for of in list_of:
            if not re.findall("M._", of) == []:
                if "D_" in of:
                    of_count += 1
        return ["German x Masc", s_count, of_count, s_count+of_count] 



def create_result_table(s_gen_file, of_gen_file, outfile):
    """

    Parameters
    ----------
    s_gen_file : str
        File name and path of the transformed file containing
        the matches of s-genitives.
    of_gen_file : str
        File name and path of the transformed file containing
        the matches of of-genitives.
    outfile : str
        File name and path of the output file.

    Returns
    -------
    None.

    """
    with open(s_gen_file, "r", encoding="utf8") as inps, open(of_gen_file, "r", encoding="utf8") as inpof:
        csvreader_s = csv.reader(inps, delimiter =';')
        csvreader_of = csv.reader(inpof, delimiter =';')
        rows_s, rows_of = [], []
        for row in csvreader_s:
            rows_s.append(row[1])
        for row in csvreader_of:
            rows_of.append(row[1])
        with open(outfile, "w", encoding="utf8", newline="") as out:
            csvwriter= csv.writer(out)
            header = ["SUBCORPUS", "TOTAL S-GEN", "TOTAL OF-GEN", "TOTAL GEN"]
            csvwriter.writerow(header)
            rueg = count("RUEG", rows_s, rows_of)
            en = count("EN", rows_s, rows_of)
            de = count("DE", rows_s, rows_of)
            gr = count("GR", rows_s, rows_of)
            spo = count("spo", rows_s, rows_of)
            wr = count("wr", rows_s, rows_of)
            form = count("form", rows_s, rows_of)   
            inform = count("inform", rows_s, rows_of)
            fem = count("fem", rows_s, rows_of)
            masc = count("masc", rows_s, rows_of)
            enwr = count("ENwr", rows_s, rows_of)
            enspo = count("ENspo", rows_s, rows_of)
            dewr = count("DEwr", rows_s, rows_of)
            despo = count("DEspo", rows_s, rows_of)
            grwr = count("GRwr", rows_s, rows_of)
            grspo = count("GRspo", rows_s, rows_of)
            enform = count("ENform", rows_s, rows_of)
            eninform = count("ENinform", rows_s, rows_of)
            deform = count("DEform", rows_s, rows_of)
            deinform = count("DEinform", rows_s, rows_of)
            grform = count("GRform", rows_s, rows_of)
            grinform = count("GRinform", rows_s, rows_of)
            enfem = count("ENfem", rows_s, rows_of)
            enmasc = count("ENmasc", rows_s, rows_of)
            defem = count("DEfem", rows_s, rows_of)
            demasc = count("DEmasc", rows_s, rows_of)
            grfem = count("GRfem", rows_s, rows_of)
            grmasc = count("GRmasc", rows_s, rows_of)
            csvwriter.writerow(rueg)
            csvwriter.writerow(en)
            csvwriter.writerow(de)
            csvwriter.writerow(gr)
            csvwriter.writerow(spo)
            csvwriter.writerow(wr)
            csvwriter.writerow(form)
            csvwriter.writerow(inform)
            csvwriter.writerow(fem)
            csvwriter.writerow(masc)
            csvwriter.writerow(enwr)
            csvwriter.writerow(enspo)
            csvwriter.writerow(dewr)
            csvwriter.writerow(despo)
            csvwriter.writerow(grwr)
            csvwriter.writerow(grspo)
            csvwriter.writerow(enform)
            csvwriter.writerow(eninform)
            csvwriter.writerow(deform)
            csvwriter.writerow(deinform)
            csvwriter.writerow(grform)
            csvwriter.writerow(grinform)
            csvwriter.writerow(enfem)
            csvwriter.writerow(enmasc)
            csvwriter.writerow(defem)
            csvwriter.writerow(demasc)
            csvwriter.writerow(grfem)
            csvwriter.writerow(grmasc)
 
if __name__ == 'main':
    create_result_table("data_input/csv_s.csv", "data_input/csv_of.csv", "data_ouptut/results.csv")

    
    
    
    
    
    
    
    
    