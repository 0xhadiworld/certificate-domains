# x.com/0xhadiworld
import argparse
import requests
import tldextract
import io
from colorama import init, Fore

# Help Messages
HELP_DESCRIPTION = 'Extracting domains based on SSL/TLS certificates from the crt.sh website'
ORGANIZATION_DESCRIPTION = 'Organization name for certificate search'
OUTPUT_DESCRIPTION = 'Path to the output file'

# Reset color every time
init(autoreset=True)

# The function for displaying messages in color
def print_colored(message, color):
	print(color + message)

# The function is used to separate the main domain from subdomains using tldextract
def extract_main_domain(domain):
	extracted = tldextract.extract(domain)
	return f"{extracted.domain}.{extracted.suffix}" # Adding the main domain to tld

# The function to get certificates from crt.sh
def get_certificates(organization, output_file_path='NULL'):
	# Crt.sh request url
	url = f'https://crt.sh/?output=json&Identity={organization}'

	# Make teh GET request
	response = requests.get(url)

	# Check if the request was successful
	if response.status_code == 200:
		# Prase the JSON data
		data = response.json()

		# Extract all values of 'common_name'
		common_names = [entry['common_name'] for entry in data]

		# Extract main domains from 'common_names'
		main_domains = [extract_main_domain(domain) for domain in common_names]

		# Removing duplicate domains from 'main_domains'
		uniqe_main_domains = list(set(main_domains)) 

		# Check If the -f argument was specified, save the result to a file
		if output_file_path != 'NULL':
			with io.open(output_file_path, 'w', encoding='UTF-8') as output_file:
				for main_domain in uniqe_main_domains:
					output_file.write(main_domain + '\n')
			print_colored(f'Results saved to {output_file_path}', Fore.GREEN)
		else:
			# Print main domains
			for main_domain in uniqe_main_domains:
				print_colored(main_domain, Fore.CYAN)
	else:
		print_colored(f'Error: {response.status_code}', Fore.RED)



# The main function
def main():
	# Creating a parser for processing input arguments
	parser = argparse.ArgumentParser(description=HELP_DESCRIPTION)
	parser.add_argument('-o', '--organization', help=ORGANIZATION_DESCRIPTION, required=True)
	parser.add_argument('-f', '--output-file', help=OUTPUT_DESCRIPTION)

	# Receiving input arguments.
	args = parser.parse_args()
	organization = args.organization
	output_file_path = args.output_file

	# Displaying a message when the program is executed
	print_colored("Wait...", Fore.YELLOW)

	# Get certificate domains from get_certificates()
	if output_file_path:
		get_certificates(organization, output_file_path)
	else:
		get_certificates(organization)

# main
if __name__ == "__main__":
    main()








