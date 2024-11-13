import conllu
import pickle

def save_lemmas_as_pickle(input_path, pickle_path):
    """
    Extracts all unique lemmas from a .conllu file and saves them as a set in a pickle file.
    
    Parameters:
    - input_path (str): Path to the input .conllu file.
    - pickle_path (str): Path to save the set of lemmas as a pickle file.
    """
    try:
        lemmas = set()  # Set to store unique lemmas

        # Read the .conllu file and extract lemmas
        with open(input_path, 'r', encoding='utf-8') as file:
            data = conllu.parse_incr(file)
            for sentence in data:
                for token in sentence:
                    lemma = token['lemma']
                    lemmas.add(lemma)  # Add lemma to the set

        # Save the set of lemmas as a pickle file
        with open(pickle_path, 'wb') as pickle_file:
            pickle.dump(lemmas, pickle_file)

        print(f"Set of lemmas saved to {pickle_path}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_file = 'C:/Users/benji/Desktop/UD/medieval/medieval.conllu'
pickle_file = 'C:/Users/benji/Desktop/UD/medieval/lemmas_set.pkl'

save_lemmas_as_pickle(input_file, pickle_file)
