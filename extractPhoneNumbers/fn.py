import re


phone_pattern = re.compile(r"\d{10}")


# Read the input file
with open('data.txt', 'r') as file:
    input_text = file.read()

# Find all phone numbers in the input text
phone_numbers = phone_pattern.findall(input_text)

f = open("numbers.txt","a")
# filter phones numbers that starts with 98 or 97
for phone_number in phone_numbers:
    if phone_number[:2] in ['98','97']:
      f.write(phone_number+"\n")
        
