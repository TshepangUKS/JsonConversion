import csv
ray = []
line_count =0

path = 'C:\\Users\\Mlambo\\Desktop\\Scripts\\NULData\\2023Users.csv'
csv_reader = csv.reader(path, delimiter=';')

with open('C:\\Users\\Mlambo\\Desktop\\Scripts\\NULData\\final.txt', 'w') as json_file:
    with open(path, 'r') as excel_file:
        for row in excel_file: 
            if line_count ==0:
                print(row)
                json_file.writelines(row)
                line_count+=1
                continue
            # print(splitrow)
            splitrow = row.split(';')
        # if 'undergrad' in row: 
            print(line_count)
                    # ray.append(row)
                    # splitrow[] = ray[line_count].split()
            json_file.writelines("[\n{\n 'Username:'Null \n")
            json_file.writelines(f'"externalSystmId": "{splitrow[0]}" \n')
            json_file.writelines(f'"barcode": "{splitrow[1]}" \n')
            json_file.writelines(f'"active": "true" \n')
            json_file.writelines(f'"PatronGroup": "{splitrow[2]}" \n')
            json_file.writelines(f'"Departments": "{splitrow[3]}" \n')
            json_file.writelines(f'"personal": "open" \n')
            json_file.writelines(f'"lastname": "{splitrow[4]}" \n')
            json_file.writelines(f'"firstname": "{splitrow[5]}" \n')
            json_file.writelines(f'"email": "{splitrow[6]}" \n')
            json_file.writelines(f'"phone": "{splitrow[7]}" \n')
            json_file.writelines(f'"mobilephone": "{splitrow[8]}" \n')
            json_file.writelines(f'"dateOfbirth": "{splitrow[9]}" \n')
            json_file.writelines(f'"addresses": "[" \n')
            json_file.writelines(f'"addressline1": "{splitrow[11]}" \n')
            json_file.writelines(f'"addressline2": "{splitrow[12]}" \n')
            json_file.writelines(f'"city": "{splitrow[13]}" \n')
            json_file.writelines(f'"postalcode": "{splitrow[14]}" \n')
            json_file.writelines(f'"addresstypeID": "{splitrow[15]}" \n')
            json_file.writelines(f'"primaryaddress": "{splitrow[16]}" \n')
            json_file.writelines(f'"enrollmentdate": "{splitrow[17]}" \n')
            json_file.writelines(f'"expirationdate": "{splitrow[18]}" \n')
            json_file.writelines("}\n]\n\n")
            line_count +=1
            # continue