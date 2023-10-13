import re
import spacy

def extract_candidates(text):
    # Load spaCy model for English
    nlp = spacy.load("en_core_web_sm")

    # Define pattern for other references
    other_reference_pattern = r'[A-Z][a-z]*\s+\d{4}'

    # Define lists to store candidates
    nugget_candidates = []
    book_reference_candidates = []
    other_reference_candidates = []

    # Trigger phrases for interesting content
    trigger_phrases = ["wow", "I've never thought about it", "brilliant way of saying", "brilliant way of putting it"]

    # Split the text into sentences
    sentences = text.split('.')

    # Iterate through sentences
    for i, sentence in enumerate(sentences):
        # Process the sentence with spaCy

        doc = nlp(sentence)
        
        try:
            last_two_sentences = sentences[i-1] + sentences[i-2]
            next_two_sentences = sentences[i+1] + sentences[i+2] 
        except Exception:
            last_two_sentences = ""
            next_two_sentences = ""
            print(i)
        
        # Check for trigger phrases
        for phrase in trigger_phrases:
            if phrase in sentence.lower():
                nugget_candidates.append("Nugget start")
                nugget_candidates.append(last_two_sentences.strip())
                nugget_candidates.append(sentence.strip())
                nugget_candidates.append(next_two_sentences.strip())
                nugget_candidates.append("Nugget end")
                break  # Break out of the loop if a trigger phrase is found

        # Check for book references
        book_references = re.findall(r'"(.*?)"\s*\(\d{4}\)', sentence)
        for ref in book_references:
            book_reference_candidates.append(ref.strip())

        # Check for the word "book" and extract book title
        if "book" in sentence.lower():
            book_title_match = re.search(r'"(.*?)"', sentence)
            if book_title_match:
                book_reference_candidates.append(book_title_match.group().strip())

        # Check for other references
        other_references = re.findall(other_reference_pattern, sentence)
        for ref in other_references:
            other_reference_candidates.append(ref.strip())
        
    # Return the lists of candidates
    return nugget_candidates, book_reference_candidates, other_reference_candidates

# Example usage:
long_text = """
In a recent podcast interview, the author mentioned his favorite book, "The Catcher in the Rye" (1951), which had a profound impact on his writing. 
He also referred to an article published in The New Yorker in 2019, titled "The Art of Storytelling." 
During the interview, they discussed various thought-provoking topics, such as the impact of literature on society.

The author shared an interesting insight into his writing process. He said, "Writing is a way of thinking on paper." This nugget of wisdom resonated with many listeners and received a "wow" from one of the participants.

Later in the conversation, the host mentioned a TED talk by Susan Cain (2012), titled "The Power of Introverts." This was another valuable reference. One of the listeners commented, "I've never thought about it that way."
"""
# Define the file path
file_path = "transcript.txt"

# Initialize the longer_text variable
longer_text = ""

# Read the content of the file and store it in longer_text
try:
    with open(file_path, "r", encoding="utf-8") as file:
        longer_text = file.read()
except FileNotFoundError:
    print(f"File '{file_path}' not found.")
except Exception as e:
    print(f"An error occurred while reading the file: {e}")

# Now you can use the 'longer_text' variable for further processing

# nugget_candidates, book_reference_candidates, other_reference_candidates = extract_candidates(long_text)

# print("Nugget Candidates:")
# for candidate in nugget_candidates:
#     print(candidate)

# print("\nBook Reference Candidates:")
# for candidate in book_reference_candidates:
#     print(candidate)

# print("\nOther Reference Candidates:")
# for candidate in other_reference_candidates:
#     print(candidate)



print("2")
nugget_candidates, book_reference_candidates, other_reference_candidates = extract_candidates(longer_text)

print("Nugget Candidates:")
for candidate in nugget_candidates:
    print(candidate)

print("\nBook Reference Candidates:")
for candidate in book_reference_candidates:
    print(candidate)

print("\nOther Reference Candidates:")
for candidate in other_reference_candidates:
    print(candidate)
