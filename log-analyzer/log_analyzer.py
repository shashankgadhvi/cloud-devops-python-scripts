def read_logs():
    with open("/Users/shashankgadhvi/Downloads/python_core/code/logfile.txt" , "r") as file:
        lines = file.readlines()
    return lines

def parsing(line): #what is parsing?
    #parsing is when you go through the log text and extract meaningfull information from it
    parts = line.split() 
    ip = parts[0] # ip address at first index to extract from log file
    method = parts[4].replace('"', '') # the part where it's GET and POST at fourth index
    status = parts[-2] # status like 404 error 200 etc , at second last index
    return{
        "ip" : ip,
        "Method" : method,
        "Status" : status
}

print("======Welcome to log analyzer tool======")
parsed_dict = []
# calling read function to read log files
logs = read_logs()

for line in logs:
    parsed_data = parsing(line)# function calling to parse log files into meaning full text
    parsed_dict.append(parsed_data) # adding the parsed data in a list so we can store it
    print(parsed_data)

#1 this is where real application starts 
# we check for errors in HTTP status codes, where 200 is alright rest are different errors 
print()
print("Following are the errors in parsed list: ")
for item in parsed_dict:
    if item["Status"] != "200":
        print(item["Status"])

#2 ip count

#3 track get and post methods, just for practice here we track GET method.
print()
print("Tracking GET method:")
for item in parsed_dict:
    if item["Method"] == "GET":
        print(item)

#4 export output to csv file
with open("/Users/shashankgadhvi/Downloads/python_core/code/output.csv" , "w") as file:
    for item in parsed_dict:
        file.write(str(item) + "\n")
