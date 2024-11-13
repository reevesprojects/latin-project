import pickle

def compare_lemmas_in_pickles(pickle_path_1, pickle_path_2):
    """
    Compares two pickle files containing sets of lemmas and finds how many lemmas are in one but not the other.
    
    Parameters:
    - pickle_path_1 (str): Path to the first pickle file containing the first set of lemmas.
    - pickle_path_2 (str): Path to the second pickle file containing the second set of lemmas.
    """
    try:
        # Load the first set of lemmas from pickle file 1
        with open(pickle_path_1, 'rb') as pickle_file_1:
            lemmas_1 = pickle.load(pickle_file_1)

        # Load the second set of lemmas from pickle file 2
        with open(pickle_path_2, 'rb') as pickle_file_2:
            lemmas_2 = pickle.load(pickle_file_2)

        # Find the lemmas in the first set but not in the second set
        unique_to_lemmas_1 = lemmas_1 - lemmas_2

        # Find the lemmas in the second set but not in the first set
        unique_to_lemmas_2 = lemmas_2 - lemmas_1

        # Print results
        print(f"Number of lemmas in classical but not in medieval: {len(unique_to_lemmas_1)}")
        print(f"Number of lemmas in medieval but not in medieval: {len(unique_to_lemmas_2)}")
        print(f"Total number of unique lemmas in either file: {len(unique_to_lemmas_1) + len(unique_to_lemmas_2)}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
pickle_file_1 = 'C:/Users/benji/Desktop/UD/classical/lemmas_set.pkl'
pickle_file_2 = 'C:/Users/benji/Desktop/UD/medieval/lemmas_set.pkl'

compare_lemmas_in_pickles(pickle_file_1, pickle_file_2)
