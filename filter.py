import conllu

def filter_proiel_conllu_sources(input_path, output_path, exclude_sources):
    """
    Filters out sentences from specified sources in a .conllu file.
    
    Parameters:
    - input_path (str): Path to the input .conllu file.
    - output_path (str): Path to save the filtered .conllu file.
    - exclude_sources (list): List of source phrases to exclude (e.g., ["Jerome's Vulgate", "Commentarii belli Gallici", "Opus agriculturae"]).
    """
    try:
        with open(input_path, 'r', encoding='utf-8') as file:
            data = conllu.parse_incr(file)
            
            filtered_content = []
            sentence_skipped = False
            
            for sentence in data:
                # Extract source and check if it matches any exclude sources
                source = sentence.metadata.get("source", "")
                
                # Skip sentence if the source matches any excluded source
                if any(exclude_source in source for exclude_source in exclude_sources):
                    sentence_skipped = True
                    continue  # Skip this sentence
                
                # Add this valid sentence to the filtered content
                filtered_content.append(sentence.serialize())
            
            # Write the filtered content if any valid sentences exist
            if filtered_content:
                with open(output_path, 'w', encoding='utf-8') as output_file:
                    for sentence in filtered_content:
                        output_file.write(sentence + "\n")
                
                print(f"Filtered file saved as {output_path}")
            else:
                print("No valid sentences to save.")

            # Check if any sentences were skipped
            if sentence_skipped:
                print("Some sentences were skipped based on exclude_sources criteria.")
            else:
                print("No sentences matched the exclude criteria.")
                
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_file = 'C:/Users/benji/Desktop/UD/classical/la_proiel-ud.conllu'
output_file = 'C:/Users/benji/Desktop/UD/classical/la_proiel-ud-filtered.conllu'

# Exclude sentences from sources: Jerome's Vulgate, Commentarii belli Gallici, and Opus agriculturae
exclude_sources = ["Jerome's Vulgate", "Commentarii belli Gallici", "Opus agriculturae"]
filter_proiel_conllu_sources(input_file, output_file, exclude_sources)
