import tkinter as tk


def process(*args):
	print("process")

	val = ent_value.get()

	print(val)


	check = check01(val)
	print(check)



	if (check == True):
		val = remove0(val)
		print(val)

		result = base2to10(val)

		lab_results.config(text = str(val) + " --> " + str(result))

	else:
		lab_results.config(text = "INVALID")


	ent_value.delete(0,tk.END)

	


def remove0(str):


#0 means start at 0, len(str) means end there (exclusive), increase by 1 each time
	for i in range(0, len(str),1):
		if (str == "0"):
			return str
		elif (str[i] == "1"):
			return str[i:]





def check01(str):
	print("Check 01")


	num_0 = str.count("0")
	num_1 = str.count("1")

	if num_0 + num_1 == len(str):
		return True
	return False


def base2to10(str):

	n = 0
	total = 0

	for i in range(len(str) - 1, -1, -1):

		total = total + int(str[i]) * 2**n

		n = n + 1

	return total



root = tk.Tk()


lab_instructions = tk.Label(root, text = "Enter binary")

ent_value = tk.Entry(root)

lab_results = tk.Label(root, text = "--")





lab_instructions.pack()

ent_value.pack()

lab_results.pack()



















root.bind("<Return>", process)
root.mainloop()