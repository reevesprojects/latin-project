import conllu

def count_sentences_in_conllu_files(file_paths):
    """
    Counts the total number of sentences across multiple .conllu files.
    
    Parameters:
    - file_paths (list): List of paths to .conllu files.
    
    Returns:
    - int: Total count of sentences across all files.
    """
    total_sentences = 0

    for file_path in file_paths:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                # Parse each sentence in the file and count it
                sentences = list(conllu.parse_incr(file))
                sentence_count = len(sentences)
                total_sentences += sentence_count
                print(f"{file_path}: {sentence_count} sentences")
        except Exception as e:
            print(f"An error occurred while processing {file_path}: {e}")

    print(f"Total sentences across all files: {total_sentences}")
    return total_sentences

# Example usage:
conllu_files = [
    'C:/Users/benji/Desktop/UD/medieval/la_ittb-ud.conllu',
    'C:/Users/benji/Desktop/UD/medieval/la_udante-ud.conllu'
]
count_sentences_in_conllu_files(conllu_files)
