
# ~~~~~~~~BASIC QUESTIONS~~~~~~~~~

# Tuples
def reverse(tup):
	return tup[::-1]


# Rlists
def tup_to_rlist(lst):
	rlist = empty_rlist
	while lst != ():
		track = len(lst) - 1 
		last = lst[track]
		rlist = last, rlist
		lst = lst[:track]
	return rlist

def map_rlist(lst, f):
	"Theirs"
    new = empty_rlist
    while lst != empty_rlist:
        new = rlist(f(first(lst)), new)
        lst = rest(lst)
    while new != empty_rlist:
        lst = rlist(first(new), lst)
        new = rest(new)
    return lst


# Map, Filter and Friends
def map(f, seq):
	tup = ()
	for elem in seq:
		tup += (f(elem),)
	return tup

def filter(pred, seq):
	tup = ()
	for elem in seq:
		if pred(elem):
			tup += (elem,)
	return tup

def reduce(combiner, seq):
	i = 1
	value = seq[0]
	while i < len(seq):
		value = combiner(value, seq[i])
		i+=1
	return value


# Lists
def reverse(L):
	"""Why doesnt this work"""
	L = L[::-1]

def reverse(L):
	"Theirs"
    for i in range(len(L)//2):
        L[i], L[-i-1] = L[-i-1], L[i]

def map_mut(f, L):
	"""Switching up the order because the value L[i] appears more than once"""
	i = 0
	while i < len(L):
		x = L[i]
		L.remove(L[i])
		L.insert(i, f(x))
		i += 1

def map_mut(f, L):
	"""Theirs"""
    for i in range(len(L)):
        L[i] = f(L[i])


# ~~~~~~~~Exam Questions~~~~~~~~~

# Tuples
def is_palindrome(tup):
	for i in range(len(tup)//2):
		if tup[i] != tup[-i-1]:
			return False
		return True

def flatten(tup):
	new = ()
	for i in tup:
		if len(i) == 1:
			new += i
		else:
			flatten(i)
	return new()




































