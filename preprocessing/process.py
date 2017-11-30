
def main():
	f = open("dump.txt",'r')
	text = f.read()
	text = text.split("\n")
	result = ""
	for each in text:
		if each == "" or each == "\n":
			continue
		result += each + " "

	f = open("process_dump.txt",'w')
	f.write(result)

main()