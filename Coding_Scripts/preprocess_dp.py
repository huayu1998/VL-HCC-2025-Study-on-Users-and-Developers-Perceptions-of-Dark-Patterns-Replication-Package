# packages import
'''regular expression'''
import re
import nltk
import string
import pandas as pd
# import pip
# pip.main(['install', 'emoji'])
import emoji
from nltk.corpus import stopwords

# helper functions
def contraction_list():
    contractions_dict = {
        "aren't": "are not",
        "can't": "cannot",
        "couldn't": "could not",
        "didn't": "did not",
        "doesn't": "does not",
        "don't": "do not",
        "hadn't": "had not",
        "hasn't": "has not",
        "haven't": "have not",
        "he'd": "he would",
        "he'll": "he will",
        "he's": "he is",
        "I'd": "I would",
        "i'd": "i would",
        "I'll": "I will",
        "i'll": "i will",
        "I'm": "I am",
        "i'm": "i am",
        "I've": "I have",
        "i've": "i have",
        "isn't": "is not",
        "it'd": "it would",
        "it'll": "it will",
        "it's": "it is",
        "let's": "let us",
        "mightn't": "might not",
        "mustn't": "must not",
        "shan't": "shall not",
        "she'd": "she would",
        "she'll": "she will",
        "she's": "she is",
        "shouldn't": "should not",
        "that's": "that is",
        "there's": "there is",
        "they'd": "they would",
        "they'll": "they will",
        "they're": "they are",
        "they've": "they have",
        "we'd": "we would",
        "we'll": "we will",
        "we're": "we are",
        "we've": "we have",
        "weren't": "were not",
        "what'll": "what will",
        "what're": "what are",
        "what's": "what is",
        "what've": "what have",
        "where's": "where is",
        "who'd": "who would",
        "who'll": "who will",
        "who's": "who is",
        "won't": "will not",
        "wouldn't": "would not",
        "you'd": "you would",
        "you'll": "you will",
        "you're": "you are",
        "you've": "you have",
        "how'd": "how did",
        "how'll": "how will",
        "how's": "how is",
        "here's": "here is",
        "there'd": "there would",
        "that'd": "that would",
        "who're": "who are",
        "y'all": "you all",
        "y'alls": "you alls",
        "ain't": "is not",
        "ma'am": "madam",
        "o'clock": "of the clock",
        "when's": "when is",
        "why's": "why is",
        "would've": "would have",
        "could've": "could have",
        "should've": "should have",
        "might've": "might have",
        "must've": "must have",
        "needn't": "need not",
        "had've": "had have",
        "that'll": "that will",
        "who've": "who have",
        "there'll": "there will",
        "there've": "there have",
        "wasn't": "was not",
        "wouldn't've": "would not have",
        "shouldn't've": "should not have",
        "couldn't've": "could not have",
        "mightn't've": "might not have",
        "mustn't've": "must not have",
        "I'd've": "I would have",
        "i'd've": "i would have",
        "he'd've": "he would have",
        "she'd've": "she would have",
        "we'd've": "we would have",
        "you'd've": "you would have",
        "it'd've": "it would have",
        "y'all'd've": "you all would have",
        "you'll've": "you will have",
        "she'll've": "she will have",
        "he'll've": "he will have",
        "it'll've": "it will have",
        "they'll've": "they will have",
        "we'll've": "we will have",
        "when've": "when have",
        "how've": "how have",
        "why've": "why have",
        "somebody's": "somebody is",
        "something's": "something is",
        "where'd": "where did",
        "where've": "where have",
        "there's": "there is",
        "who'll've": "who will have",
    }
    return contractions_dict

# Regular expression for contractions
def expand_contractions(text, contractions_dict=contraction_list()):
    contractions_re = re.compile('(%s)' % '|'.join(contraction_list().keys()))
    def replace(match):
        return contractions_dict[match.group(0)]
    # Substitutes all contractions using the dictionary
    return contractions_re.sub(replace, text)

def programming_keywords():
    programming_keywords = {
        "abstract", "and", "assert", "bool", "boolean", "break", "byte", "case", "catch", "char", 
        "class", "clone", "const", "continue", "def", "default", "delegate", "delete", "do", 
        "double", "each", "echo", "elif", "else", "elseif", "endfor", "endforeach", "endif", 
        "endwhile", "enum", "event", "except", "explicit", "export", "extends", "fi", "final", 
        "finally", "float", "for", "foreach", "function", "get", "global", "goto", "if", 
        "implements", "import", "in", "include", "instanceof", "int", "interface", "lambda", 
        "long", "namespace", "native", "new", "null", "or", "out", "override", "package", 
        "print", "private", "protected", "public", "raise", "readonly", "require", "return", 
        "set", "short", "signed", "static", "struct", "super", "switch", "synchronized", 
        "than", "this", "throw", "throws", "try", "union", "var", "virtual", "void", "with", 
        "yield"
    }
    return programming_keywords

def stopwords_with_programming_keywords():
    stopWords = set(stopwords.words('english'))
    # Set of programming keywords to add
    programming_keywords = {
        "abstract", "and", "assert", "bool", "boolean", "break", "byte", "case", "catch", "char", 
        "class", "clone", "const", "continue", "def", "default", "delegate", "delete", "do", 
        "double", "each", "echo", "elif", "else", "elseif", "endfor", "endforeach", "endif", 
        "endwhile", "enum", "event", "except", "explicit", "export", "extends", "fi", "final", 
        "finally", "float", "for", "foreach", "function", "get", "global", "goto", "if", 
        "implements", "import", "in", "include", "instanceof", "int", "interface", "lambda", 
        "long", "namespace", "native", "new", "null", "or", "out", "override", "package", 
        "print", "private", "protected", "public", "raise", "readonly", "require", "return", 
        "set", "short", "signed", "static", "struct", "super", "switch", "synchronized", 
        "than", "this", "throw", "throws", "try", "union", "var", "virtual", "void", "with", 
        "yield"
    }
    stopWords.update(programming_keywords)
    return stopWords

def preprocess_dp_single_data_general(input_string):
    ''' Preprocess steps as following:
        Remove: URLs✅, @mention tags✅, hashtag✅, HTML tags✅
        Lowercase✅
        Contraction✅
        Tokenization✅
        Remove: punctuation✅, numeric and alphanumeric strings✅, stop words✅
        Remove: meaningless words, emoji✅
        Negation handling✅
    '''
    update_text = ''
    if type(input_string) is str:
        #remove: extra whitespace, URLs, @mentions tags, hashtags, html tags
        update_text = re.sub(r"\s+", ' ', input_string)
        update_text = re.sub(r'https?:\/\/\S+', '', update_text)
        update_text = re.sub(r'@[A-Za-z0-9]+', '', update_text)
        update_text = re.sub(r'#[A-Za-z0-9]+', '', update_text)
        update_text = re.sub(r'<.*?>', '', update_text)
        # lower case all texts
        update_text = update_text.lower()
        # contractions handling
        update_text = expand_contractions(update_text)
        # remove: punctuation, stopwords including common programming language
        update_text = update_text.translate(str.maketrans('', '', string.punctuation))
        # remove both numeric and alphanumeric strings
        update_text= re.sub(r'\S*\d+\S*', '', update_text)
        # tokenization
        tokens = nltk.word_tokenize(update_text,language='english')
        # remove stop words
        stopWords = stopwords_with_programming_keywords()
        non_stop_words = []
        for word in tokens:
            if word not in stopWords:
                non_stop_words.append(word)
        # Get rid of the meaningless word
        updateMeanningfulTokens = []
        for word in non_stop_words:
            if len(word) < 20 and word.encode().isalpha():
                updateMeanningfulTokens.append(word)
        # convert the tokens into a stirng
        update_text = ' '.join(updateMeanningfulTokens)
    return update_text

def preprocess_dp_single_data_DEVA(input_string):
    ''' Preprocess steps as following: ✅ means needed & ❌ means NOT needed
    
        Remove: extra whitespace✅, URLs✅, @mention tags✅, #hashtag✅, HTML tags✅, code snippets✅
        Lowercase❌
        Contraction✅
        Tokenization❌
        Split the string into words✅
        Remove: punctuation/emoticons❌, numeric and alphanumeric strings✅, stop words❌, programming keywords✅
        Remove: meaningless words✅, emoticons❌, emojis✅
        Negation handling❌
    '''
    update_text = ''
    if type(input_string) is str:
        #remove: extra whitespace, URLs, @mentions tags, hashtags, html tags, emojis
        update_text = re.sub(r"\s+", ' ', input_string)
        update_text = re.sub(r'https?:\/\/\S+', '', update_text)
        update_text = re.sub(r'@[A-Za-z0-9]+', '', update_text)
        update_text = re.sub(r'#[A-Za-z0-9]+', '', update_text)
        update_text = re.sub(r'<.*?>', '', update_text)
        update_text = emoji.replace_emoji(update_text, "")
        # contractions handling
        update_text = expand_contractions(update_text)
        # remove: numeric and alphanumeric strings
        update_text= re.sub(r'\S*\d+\S*', '', update_text)
        # split the string word by word by space
        words = update_text.split()
        # remove programming language keywords
        programmingKeywords = programming_keywords()
        non_programming_kw = []
        for word in words:
            if word.lower() not in programmingKeywords:
                non_programming_kw.append(word)
        # Get rid of the meaningless word
        updateMeanningfulTokens = []
        for word in non_programming_kw:
            if len(word) < 20:
                updateMeanningfulTokens.append(word)
        # convert the tokens into a stirng
        update_text = ' '.join(updateMeanningfulTokens)
    return update_text

def preprocess_dp_single_data_SentiStrength_SE(input_string):
    ''' Preprocess steps as following: ✅ means needed & ❌ means NOT needed

        Remove: extra whitespace✅, URLs✅, @mention tags✅, #hashtag✅, HTML tags✅, code snippets✅
        Lowercase✅
        Contraction❌
        Tokenization❌
        Split the string into words✅
        Remove: punctuation/emoticons✅, numeric and alphanumeric strings✅, stop words❌, programming keywords✅
        Remove: meaningless words✅, emoji✅
        Negation handling❌
    '''
    update_text = ''
    if type(input_string) is str:
        #remove: extra whitespace, URLs, @mentions tags, hashtags, html tags, emojis
        update_text = re.sub(r"\s+", ' ', input_string)
        update_text = re.sub(r'https?:\/\/\S+', '', update_text)
        update_text = re.sub(r'@[A-Za-z0-9]+', '', update_text)
        update_text = re.sub(r'#[A-Za-z0-9]+', '', update_text)
        update_text = re.sub(r'<.*?>', '', update_text)
        update_text = emoji.replace_emoji(update_text, "")
        # lower case all texts
        update_text = update_text.lower()
        # remove: punctuation, stopwords including common programming language
        update_text = update_text.translate(str.maketrans('', '', string.punctuation))
        # remove both numeric and alphanumeric strings
        update_text= re.sub(r'\S*\d+\S*', '', update_text)
        # tokenization
        # tokens = nltk.word_tokenize(update_text,language='english')
        words = update_text.split()
        # remove stop words
        programmingKeywords = programming_keywords()
        non_programming_kw = []
        for word in words:
            if word not in programmingKeywords:
                non_programming_kw.append(word)
        # Get rid of the meaningless word
        updateMeanningfulTokens = []
        for word in non_programming_kw:
            if len(word) < 20:
                updateMeanningfulTokens.append(word)
        # convert the tokens into a stirng
        update_text = ' '.join(updateMeanningfulTokens)
    return update_text

def preprocess_dp_file(inputFileName, outputFileName, columnName):
    # Read the original data file
    data_df = pd.read_csv(inputFileName)
    items = data_df[columnName]
    preprocess_general = []
    preprocess_DEVA = []
    preprocess_SSSE = []
    for item in items:
        # Replace the preprocess function name here depends on the tools used
        curr_prepro = preprocess_dp_single_data_general(item)
        preprocess_general.append(curr_prepro)
    for item in items:
        # Replace the preprocess function name here depends on the tools used
        curr_prepro = preprocess_dp_single_data_DEVA(item)
        preprocess_DEVA.append(curr_prepro)
    for item in items:
        # Replace the preprocess function name here depends on the tools used
        curr_prepro = preprocess_dp_single_data_SentiStrength_SE(item)
        preprocess_SSSE.append(curr_prepro)
    # add addition column for the preprocessed data
    data_df['general_prepro_'+columnName] = preprocess_general
    data_df['DEVA_prepro_'+columnName] = preprocess_DEVA
    data_df['SSSE_prepro_'+columnName] = preprocess_SSSE
    data_df.to_csv(outputFileName, index=False)

def list_to_text_file(inputFileName, columnName, outputFileName):
    data_df = pd.read_csv(inputFileName)
    strings_list = data_df[columnName]
    with open(outputFileName, 'w') as file:
        # Iterate through the list of strings
        for index, string in enumerate(strings_list):
            # Write each string with its index number and a tab
            file.write(f"{index}\t{string}\n")

def list_to_text_remove_nan_file(inputFileName, columnName, outputFileName):
    data_df = pd.read_csv(inputFileName)
    # Drop rows where the specified column is empty or contains NaN
    filtered_data = data_df[columnName].dropna().str.strip()
    filtered_data = filtered_data[filtered_data != '']

    with open(outputFileName, 'w') as file:
        # Iterate through the filtered list of strings
        for index, string in enumerate(filtered_data, start=1):
            # Write each string with its index number and a tab
            file.write(f"{index}\t{string}\n")

def main():

    '''Preprocess the GitHub dark pattern data'''
    inputFileName = 'NAME_OF_INPUT_FILE_THAT_NEXT_PREPROCESS.csv'
    outputFileName = 'NAME_OF_PREPROCESSED_OUTPUT_FILE.csv'
    columnName = 'title' # THE PROPERTY NAME OF THE ROW NAME, e.g. title, body, comments, etc.
    preprocess_dp_file(inputFileName, outputFileName, columnName)
    print("Preprocess successfully.")

    # # Convert the a list of strings into a text file with specific format for sentiment analysis tools: SentiStrength-SE and DEVA
    list_to_text_file('prepro_dp_title.csv', 'DEVA_prepro_title', 'dp_prepro_DEVA_title.txt')
    print("Text file created successfully.")

    # Return true or pass
    pass

if __name__ == "__main__":
    main()