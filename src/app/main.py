#!/usr/bin/env python3
from pandas import DataFrame
from pathlib import Path
from models.FakerClasses import FakePerson, FakeContactDetail

# adjust the number of required entries to meet your data sampling needs
number_of_records = 100

# determine if tab-delimited csv or excel output format
excel_file_format = 0

# hardcoded data output directory
output_path = Path('./data/')

if __name__ == "__main__":
    # create empty lists for storing generated data
    person_list = []
    contact_detail_list = []

    for i in range(number_of_records):
        # instantiate new FakeRecords
        p = FakePerson(i)
        cd = FakeContactDetail(i)
        # append FakeRecords data to our respective lists
        person_list.append(p.__dict__)
        contact_detail_list.append(cd.__dict__)

    # convert the records to pandas DataFrame objects
    dfA = DataFrame(person_list)
    dfB = DataFrame(contact_detail_list)

    # write the generated records to a file
    if (excel_file_format):
        # attempting to write to the same workbook will overwrite data
        dfA.to_excel(output_path.joinpath('Person.xlsx'), index=False)
        dfB.to_excel(output_path.joinpath('ContactDetail.xlsx'), index=False)
    else:
        # csv may contain only one sheet
        dfA.to_csv(output_path.joinpath('Person.csv'), sep='\t', index=False)
        dfB.to_csv(output_path.joinpath('ContactDetail.csv'), sep='\t', index=False)