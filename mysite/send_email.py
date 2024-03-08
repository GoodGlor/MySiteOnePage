from pygsheets import authorize



spreadsheet = authorize(service_file='./key_sheet.json').open('PersonalData')


def send_data(values: list):
    wks = spreadsheet.worksheet('title', 'Shaver')

    num_rows = len(wks.get_col(1, include_tailing_empty=False))
    print('ok')
    wks.update_row(num_rows + 1, values)


