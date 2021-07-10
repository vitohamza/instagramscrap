# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('google API JSON here', scope) #addjsonkey

# authorize the clientsheet 
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open('Instagram Data Scrap')

# get the first sheet of the Spreadsheet
sheet_instance = sheet.get_worksheet(0)

#first row is data header to keep    
sheet_instance.resize(rows=1)
sheet_instance.resize(rows=30)
sheet_instance.insert_rows(table.values.tolist(), row = 2)