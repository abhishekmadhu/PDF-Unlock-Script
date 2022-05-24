from PyPDF2 import PdfFileReader, PdfFileWriter
from datetime import date, timedelta

def decrypt_pdf(input_path, output_path, password):
  with open(input_path, 'rb') as input_file, \
    open(output_path, 'wb') as output_file:
    reader = PdfFileReader(input_file)
    reader.decrypt(password)

    writer = PdfFileWriter()

    for i in range(reader.getNumPages()):
      writer.addPage(reader.getPage(i))

    writer.write(output_file)

if __name__ == '__main__':
  
  phone_last_digits = '@0871'
  
  # example usage:
  
  start_date = date(1967, 1, 1)
  end_date = date(1967, 12, 31)

  date = start_date
  while date <= end_date:
    pass_first = date.strftime("%d%m")
    password = pass_first + phone_last_digits
    try:
      print(f'trying {password}')
      decrypt_pdf('Downloads/Account Statement Banamali Madhu.pdf', 'decrypted.pdf', password)
      print('hooray it is done')
    except Exception as e:
      print(e)
    
    date += timedelta(days=1)
      