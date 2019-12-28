import re
import os


def read(path = "D:\\GT Data Science and Analytics\\Home_work\\PyParagraph\\raw_data", file = "paragraph_2.txt"):

	"""
	Read function takes two parameters - path and file, reads the file and returns the text of the file.
	"""

	paragraph = os.path.join(path, file)

	with open (paragraph, newline = '', encoding = 'utf-8') as txt_file: 
		content = txt_file.read()
	return content

def write(w_c, s_c, a_w_l, a_s_l):
	"""
	Function writes the results of the analysis in specified format to the txt file
	"""
	with open ("paragraph_result.txt", 'w') as txt_file:
		txt_file.write(f"Paragraph Analysis\n--------------------------\nApproximate Word Count: {w_c}\nApproximate Sentence Count: {s_c}\nAverage Letter Count: {a_w_l}\nAverage Sentence Length: {a_s_l}")




def count(text_file):
	"""
	Function splits the original text based on the given pattern to sentences. Further, each sentence is split to words and the number of the characters are found.
	"""
	
	word_count_lst = []
	char_count_lst = []
	sentence_split = re.split("\n+|(?<=[.!?]) +", text_file) #I added \n+ pattern to the split function since the recommended pattern did not work for the paragraph_2.txt. \n+ finds new line and splits the sentence 
	for sentence_index, sentences in enumerate(sentence_split, start = 1):
		sentence_count = sentence_index
		words = re.split("[\s]", sentences) # \s pattern splits the words at whitespace. This will leave the ., and other signs attached to the preceding word therefore the below split pattern is required 
		for word_index, word in enumerate(words, start = 1):
			word_count = word_index
			chars = re.findall(r'[a-zA-Z0-9]', word) #This pattern will only split the characters if they are alphabet letters or numbers. The remaining characters are left out of the words and were not counted in average character number per word
			for char_index, char in enumerate(chars, start = 1):
				char_count = char_index
			char_count_lst.append(char_count)
		word_count_lst.append(word_count)	
	return sentence_count, sum(word_count_lst), round(sum(word_count_lst)/len(word_count_lst), 1), round(sum(char_count_lst)/len(char_count_lst), 1)

def main():
	"""
	This is the main function that runs the other functions and lastly sends the returned values to write()
	"""
	text = read()
	sentence_count, word_count, average_sentence_length , average_word_length = count(text)
	write(word_count, sentence_count, average_word_length, average_sentence_length)


main()