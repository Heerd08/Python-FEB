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
