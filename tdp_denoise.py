def strip_html(text):
	soup = BeautifulSoup(text, "html.parser")
	return soup.get_text()
	
def remove_between_square_brackets(text):
	return re.sub('\[[^]]*\]', '', text)

def denoise_text(text):
	text = strip_html(text)
	text = remove_between_square_brackets(text)
	return text

sample=denoise_text(sample)
print(sample)
