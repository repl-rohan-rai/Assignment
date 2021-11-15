para_open=("(","{","[")
para_close=(")","}","]")

def IsInputValid(expression):
    try:
        if not isinstance(expression, str):
            raise TypeError
        elif len(expression) == 0:
            raise Exception
    except TypeError:
        return 'Invalid Input'
    except Exception:
        return 'No expression entered'
    else:
        return ValidParentheses(expression)

def ValidParentheses(exp):
    position=[]
    s=[]
    for x in range(len(exp)):
        if exp[x] in para_open:
	    s.append(para_open.index(exp[x]))
	    position.append(x)
	elif exp[x] in para_close:
	    if para_close.index(exp[x]) in s:
		if s[-1]==para_close.index(exp[x]):
		    s.pop()
		    position.pop()
		return (exp[x],x+1)
    if len(s)==0:
	print ("Valid Expression.")
	return 1
    else:
	return (exp[position[-1]],position[-1]+1)
