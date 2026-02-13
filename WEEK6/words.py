# problem statement
# you are given list of strings with mixed casing and spaces.
# Normalize them(lowercase &trimed)and return only string 
# length >- 5

# input 
# words = ["  Python ", " AI ", "Machine ", " Data "]


# output 
# ["python","machine"]


def normalize_words(words):
    result = []
    
    for word in words:
        # Remove extra spaces
        cleaned_word = word.strip()
        
        # Convert to lowercase
        cleaned_word = cleaned_word.lower()
        
        # Keep words with length >= 5
        if len(cleaned_word) >= 5:
            result.append(cleaned_word)
    
    return result


# Given input
words = ["  Python ", " AI ", "Machine ", " Data "]

# Function call
output = normalize_words(words)

print(output)
