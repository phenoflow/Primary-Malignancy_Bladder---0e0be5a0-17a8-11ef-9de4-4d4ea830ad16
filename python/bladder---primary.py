# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"38862.0","system":"readv2"},{"code":"42023.0","system":"readv2"},{"code":"42012.0","system":"readv2"},{"code":"19162.0","system":"readv2"},{"code":"36949.0","system":"readv2"},{"code":"47801.0","system":"readv2"},{"code":"28241.0","system":"readv2"},{"code":"44996.0","system":"readv2"},{"code":"779.0","system":"readv2"},{"code":"35963.0","system":"readv2"},{"code":"31102.0","system":"readv2"},{"code":"41571.0","system":"readv2"},{"code":"105388.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('primary-malignancy_bladder-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["bladder---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["bladder---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["bladder---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
