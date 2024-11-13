import random
import conllu

def pick_random_sentences(input_path, output_path, num_sentences=6182):
    """
    Randomly selects a specified number of sentences from a .conllu file and saves them to a new .conllu file.
    
    Parameters:
    - input_path (str): Path to the input .conllu file.
    - output_path (str): Path to save the randomly selected sentences.
    - num_sentences (int): Number of sentences to select randomly (default is 6182).
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            # Parse all sentences in the input file
            sentences = list(conllu.parse_incr(file))
        
        # Check if there are enough sentences in the file
        if len(sentences) < num_sentences:
            print(f"Warning: The file only contains {len(sentences)} sentences, which is less than {num_sentences}.")
            num_sentences = len(sentences)  # Adjust to the number of available sentences

        # Randomly select the specified number of sentences
        selected_sentences = random.sample(sentences, num_sentences)

        # Write the selected sentences to the output file
        with open(output_path, 'w', encoding='utf-8') as output_file:
            for sentence in selected_sentences:
                output_file.write(sentence.serialize() + "\n")
        
        print(f"Randomly selected {num_sentences} sentences saved to {output_path}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_file = 'C:/Users/benji/Desktop/UD/medieval/la_ittb-ud.conllu'
output_file = 'C:/Users/benji/Desktop/UD/medieval/la_ittb-ud-random-6182.conllu'

pick_random_sentences(input_file, output_file)
