import csv

# Prompt the user for the input CSV file
input_csv_file = input("Enter the input CSV filename (or press Enter for default 'input.csv'): ")
if not input_csv_file:
    input_csv_file = 'input.csv'  # Default filename if nothing is entered

# Prompt the user for the output Nginx configuration file
output_nginx_config = input("Enter the output Nginx configuration filename (or press Enter for default 'output.conf'): ")
if not output_nginx_config:
    output_nginx_config = 'output.conf'  # Default filename if nothing is entered

# Prompt the user for a prepend string
prepend_string = input("Enter a prepend string (or press Enter for no prepend): ")

# Trim a trailing slash from the prepend_string if it's present
prepend_string = prepend_string.rstrip('/')

# Open the input CSV file and create the output Nginx configuration file
with open(input_csv_file, 'r') as csv_file, open(output_nginx_config, 'w') as nginx_config:
    # Create a CSV reader
    csv_reader = csv.reader(csv_file)

    # Iterate through the CSV rows
    for row in csv_reader:
        if len(row) < 2:
            continue  # Skip rows with missing data

        # Extract the fields from the CSV
        result = row[0]
        source = row[1]

        # Generate the Nginx redirect rule with or without prepend
        if prepend_string:
            redirect_rule = f'rewrite ^{source}$ {prepend_string}/{result} permanent;\n'
        else:
            redirect_rule = f'rewrite ^{source}$ {result} permanent;\n'
        nginx_config.write(redirect_rule)

print(f'Nginx redirect rules generated and saved to {output_nginx_config}')
