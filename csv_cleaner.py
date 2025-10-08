import csv
import os

# Ask user for the input file name
while True:
    input_filename = input("Please enter the input CSV filename (including .csv extension): ")
    if os.path.exists(input_filename):
        break
    print(f"Error: File '{input_filename}' not found. Please try again.")

with open(input_filename, newline='', encoding='utf-8') as infile, \
     open('output.csv', 'w', newline='', encoding='utf-8') as outfile:

    reader = csv.reader(infile)
    writer = csv.writer(outfile)
    writer.writerow(['Name', 'Email'])

    for row in reader:
        if not row:
            continue
        parts = row[0].strip().split()
        if len(parts) >= 3:
            # Find the index where email starts (looking for @ symbol)
            email_index = None
            for i, part in enumerate(parts):
                if '@' in part:
                    email_index = i
                    break
            
            if email_index is not None:
                # Combine all parts before email as the full name
                full_name = ' '.join(parts[:email_index])
                email = parts[email_index]
            else:
                # Fallback if email not found
                full_name = ' '.join(parts[:-1]) if len(parts) > 1 else parts[0]
                email = ''
        else:
            full_name = parts[0] if parts else ''
            email = ''
        writer.writerow([full_name, email])