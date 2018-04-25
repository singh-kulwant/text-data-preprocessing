def replace_contractions(text)
	"""Replace contractions in string of text"""
	return contractions.fix(text)

sample = replace_contractions(sample)
print(sample)
