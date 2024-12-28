# Importing the SequenceMatcher class from the difflib module
from difflib import SequenceMatcher

# Function to check plagiarism based on similarity percentage
def check_plagiarism(similarity):
    if similarity >= 90:  # Adjusted thresholds to reflect percentages
        print("High probability of plagiarism!", f"Similarity: {similarity:.2f}%")
    elif similarity >= 70:
        print("Some similarity detected, but not necessarily plagiarism.", f"Similarity: {similarity:.2f}%")
    else:
        print("Low similarity. Likely no plagiarism.", f"Similarity: {similarity:.2f}%")

# Reading the contents of both text files ("1.txt" and "2.txt")
try:
    with open("1.txt", "r", encoding="utf-8") as file1, open("2.txt", "r", encoding="utf-8") as file2:
        # Reading the contents of the files
        file1data = file1.read()
        file2data = file2.read()

        # Using SequenceMatcher to calculate similarity ratio
        similarity_ratio = SequenceMatcher(None, file1data, file2data).ratio()
        similarity_percentage = round(similarity_ratio * 100, 2)  # Convert ratio to percentage

        # Checking plagiarism based on similarity percentage
        check_plagiarism(similarity_percentage)

except FileNotFoundError as e:
    print(f"Error: {e}")
    print("Please ensure that both '1.txt' and '2.txt' are in the same directory as this script.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
