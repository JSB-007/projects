import csv
import shutil

def check_and_append_header(csv_file, scheme_file):
    # Check if the CSV file has a header
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        has_header = csv.Sniffer().has_header(file.read(1024))
    
    if not has_header:
        # Create a copy of the CSV file
        copy_file = csv_file + '.copy'
        shutil.copyfile(csv_file, copy_file)
        
        # Read the headers from the .scheme file
        with open(scheme_file, 'r') as scheme:
            headers = scheme.readline().strip().split(',')
        
        # Append the headers to the copied CSV file
        with open(copy_file, 'r+') as file:
            content = file.read()
            file.seek(0, 0)
            file.write(','.join(headers) + '\n' + content)
    
    # Return the path of the copied CSV file if headers were appended, otherwise None
    if not has_header:
        return copy_file
    else:
        return None
