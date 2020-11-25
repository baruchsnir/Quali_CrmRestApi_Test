import xlrd
import datetime
from itertools import count
import time
import os
from collections import OrderedDict

class MyRecruiter:
    def __init__(self, _file_name):
        self._file_name = _file_name

    def Get_Data_From_Workbook(self):
        data = {}
        user_data = []
        exists = os.path.exists(self._file_name)
        if not exists:
            return data,False
        # Open the workbook
        xl_workbook = xlrd.open_workbook(self._file_name)
        # List sheet names, and pull a sheet by name
        #
        sheet_names = xl_workbook.sheet_names()
        # print('Sheet Names', sheet_names)
        # xl_sheet = xl_workbook.sheet_by_name(sheet_names[0])
        xl_sheet = xl_workbook.sheet_by_index(0)

        # Locate all data and split it by user name
        # each user have a list of rows
        for row_idx in range(1, xl_sheet.nrows):  # Iterate through rows
            mobile =  xl_sheet.cell(row_idx, 0).value
            mail =  xl_sheet.cell(row_idx, 1).value
            status =  self.get_status_from_data(xl_sheet.cell(row_idx, 2).value)
            date =  xl_sheet.cell(row_idx, 3).value
            position =  xl_sheet.cell(row_idx, 4).value
            full_name =  str(xl_sheet.cell(row_idx, 5).value)
            job_code = xl_sheet.cell(row_idx, 6).value
            names = full_name.split(" ")
            first_name = full_name
            last_name = ''
            if len(names) > 1 :
                first_name = names[0]
                last_name = names[1]
            #we hold 2 records of Last Update one in float format for sorting
            #the second is a string of date time
            date_s =str( datetime.datetime(*xlrd.xldate_as_tuple(date, xl_workbook.datemode)).strftime("%d/%m/%Y %H:%M") )

            row_data = {'Mobile': mobile, 'Mail': mail, 'Status': status,'date time': date,'Last Update': date_s, 'Position': position,
                        'First Name': first_name,'Last Name' : last_name, 'Job Code': job_code}

            if full_name in data:
                user_data = data[full_name]
            else:
                user_data = []
            user_data.append(row_data)
            data[full_name] = user_data
        return data,True
    ###
    # Translate the status from hebrew to english status
    # Most of the data is in progress so we check only 3 state
    # ###
    def get_status_from_data(self,text):
        status = 'In Progress'
        if 'נשלל' in text:
            status = 'Rejected'
        if 'סירב' in text or 'לא מחפש' in text:
            status = 'Withdrawn'
        if 'התקבל' in text:
            status = 'Hired'
        return status
    ###
    # Write the dictionary to csv file
    # We write for each user the lsat row status
    # ###
    def copy_data_to_csv_file(self,data):
        filename = 'myrecuriter.csv'
        header = 'Mobile,Email,Status,Last Update,Position,First Name,Last Name,Job Code\n'
        with open(filename, "w", encoding="utf-8-sig") as f:
            f.write(header)
            for user in data:
                f.write(self.get_last_line_of_user_data(data[user]))
            f.close()
    ###
    # Sort the list of given order and get the last status of the user
    # the sorting is by the key Last Update
    # return the data as a csv line
    # ###
    def get_last_line_of_user_data(self,user_list):
        row_data = user_list[0]
        if len(user_list) > 1:
            cnt = count()
            user_list.sort(key=lambda d: (d['date time'], next(cnt)), reverse=True)
            row_data = user_list[0]

        line = '{0},{1},{2},{3},{4},{5},{6},{7}\n'.format(row_data['Mobile'],
                                                    row_data['Mail'],
                                                    row_data['Status'],
                                                    row_data['Last Update'],
                                                    row_data['Position'],
                                                    row_data['First Name'],
                                                    row_data['Last Name'],
                                                    row_data['Job Code']
                                                    )
        return line
file = 'OPS ENG task - sourceCandidates.xls'
myrec = MyRecruiter(file)
data,status = myrec.Get_Data_From_Workbook()
if status == True:
    myrec.copy_data_to_csv_file(data)