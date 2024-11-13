def merge_conllu_files(file1_path, file2_path, output_path):
    """
    Merges two .conllu files into a single .conllu file.
    
    Parameters:
    - file1_path (str): Path to the first .conllu file.
    - file2_path (str): Path to the second .conllu file.
    - output_path (str): Path to save the merged .conllu file.
    """
    try:
        # Read contents of the first file
        with open(file1_path, 'r', encoding='utf-8') as file1:
            content1 = file1.read()
        
        # Read contents of the second file
        with open(file2_path, 'r', encoding='utf-8') as file2:
            content2 = file2.read()
        
        # Combine the contents
        combined_content = content1.strip() + "\n\n" + content2.strip()
        
        # Write the combined content to the output file
        with open(output_path, 'w', encoding='utf-8') as output_file:
            output_file.write(combined_content)
        
        print(f"Files merged successfully into {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
file1 = r'C:\Users\benji\Desktop\UD\medieval\la_ittb-ud-random-6182.conllu'
file2 = r'C:\Users\benji\Desktop\UD\medieval\la_udante-ud.conllu'
output = r'C:\Users\benji\Desktop\UD\medieval\medieval.conllu'
merge_conllu_files(file1, file2, output)
