import re

text = """Hola maestro, estas es la cadena 1,ababababba como estas mi capitan
Esta es la segunda linea de texto  225 abababba
Y Esta es la linea definitiva mi capitan 2
"""

#! First result
result = re.search("Hola", text)
#! All results
result = re.findall("Esta", text)
print(result)
#! Ignoring upper and lower case
result = re.findall("Esta", text, flags=re.IGNORECASE)
print(result)

#! \d --> search the basic numeric digits (0-9)
result = re.findall(r"\d", text)
print(result)
#! \D --> search all chars other than the basic numeric digits
result = re.findall(r"\D", text)
print(result)

#! \w --> search alphanumeric chars (a-Z or A-Z or 0-9 or _)
result = re.findall(r"\w", text)
print(result)
#! \W --> search all chars other than alphanumeric chars
result = re.findall(r"\W", text)
print(result)

#! \s --> search all whitespaces, tabs and newlines
result = re.findall(r"\s", text)
print(result)
#! \S --> search all chars other than whitespaces, tabs and newlines
result = re.findall(r"\S", text)
print(result)

#! . --> search all chars other than newlines
result = re.findall(r".", text)
print(result)

#! \ --> cancel special chars
result = re.findall(r"\.", text)
print(result)

#! query
result = re.findall(r"\d\.\s", text)
print(result)

#! query to search "Hola" in the beginning of the text
result = re.findall(r"^Hola", text)
print(result)

#! query to search "Esta" in the beginning of the line
#! re.M active multiline
result = re.findall(r"^Esta", text, flags=re.M)
print(result)

#! query to search "Esta" in the end of the line
#! re.M active multiline
result = re.findall(r"capitan$", text, flags=re.M)
print(result)

# ? Groups

#! {n} --> search n times the value on the left
result = re.findall(r"\d{3}\s", text, flags=re.M)
print(result)

#! {n,m} --> search min n times and max m times the value on the left
result = re.findall(r"\d{1,4}", text, flags=re.M)
print(result)

#! {n,m} --> search min n times and max m times the value on the left
result = re.findall(r"(ab){2,4}", text, flags=re.M)
print(result)

#! | OR operator
result = re.findall(r"\d{2,4}|Hola", text, flags=re.M)
print(result)

#! * 0 or more coincidences of the value on the left
text = "The quick brown fox jumps over the lazy dog"
print(len(text))
x = re.search("^The.*dog$", text)
print(x)

#! sub method to replace the regular expression
text = "The date is 23/01/2023 and the phone is +1 5555-6565-10"
replacement = "hidden date"
x = re.sub("\d{2}/\d{2}/\d{4}", replacement, text)
print(x)

#! sub method to replace the regular expression
text = "The date is 23/01/2023 and the phone is +1 5555-6565-10"
replacement = "*"
x = re.sub("[aoeui]", replacement, text)
print(x)

# ? Notes
#! ? 0 or 1 coincidence
#! * 0 or infinite coincidence
#! + min 1 coincidence

text = "Hey Pedro my phone is: +52 55 4321-1245"
pattern = r"\+\d{2}\s\d{2}\s\d{4}-\d{4}"
replacement = "hidden number"
print(re.sub(pattern, replacement, text))
