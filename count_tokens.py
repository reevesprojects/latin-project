import conllu

def count_tokens_in_conllu(input_path):
    """
    Counts the number of tokens in a .conllu file.
    
    Parameters:
    - input_path (str): Path to the input .conllu file.
    
    Returns:
    - int: The total number of tokens in the file.
    """
    try:
        token_count = 0  # Variable to store the total number of tokens

        # Open and parse the .conllu file
        with open(input_path, 'r', encoding='utf-8') as file:
            data = conllu.parse_incr(file)  # Incremental parsing to handle large files

            # Iterate over each sentence
            for sentence in data:
                # Count the tokens in the sentence
                token_count += len(sentence)

        # Return the total number of tokens
        return token_count

    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
input_file = 'C:/Users/benji/Desktop/UD/medieval/medieval.conllu'
total_tokens = count_tokens_in_conllu(input_file)

if total_tokens is not None:
    print(f"Total number of tokens in the file: {total_tokens}")
