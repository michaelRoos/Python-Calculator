def new_split_iter(expr):

	expr = expr + ";"
	pos = 0  # begin at first character position in the list
	ans = ""
	conditional = ['>','<','=','!','>=','<=','==','!=',]
	while expr[pos] != ";":
		ans = ""
		while expr[pos] == " ":
			pos += 1
		if expr[pos].isdigit():
			while pos < len(expr) and expr[pos].isdigit():
				ans += expr[pos]
				pos += 1
		elif expr[pos:pos+2]=="or":
			ans = "|"
			pos += 2
		elif expr[pos:pos+3]=="and":
			ans = '&'
			pos +=3
		elif expr[pos].isalpha():
			while pos < len(expr)-1 and expr[pos].isalpha() or expr[pos].isdigit():
				if expr[pos] == " ":
					pos += 1
				else:
					ans += expr[pos]
					pos += 1
		elif conditional.__contains__(expr[pos]):
			ans +=expr[pos]
			pos += 1
			if expr[pos] == '=':
				ans+=expr[pos]
				pos += 1
		else:
			ans += expr[pos]
			pos += 1
		yield ans

	yield ";"



