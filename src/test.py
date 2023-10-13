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

    # Split the text into sentences
    sentences = text.split('.')

    # Iterate through sentences
    for i, sentence in enumerate(sentences):
        # Process the sentence with spaCy
        doc = nlp(sentence)

        # Check for interesting content (adjust conditions as needed)
        if len(doc) >= 5:  # At least 5 words in a sentence
            nugget_candidates.append(sentence.strip())

        # Check for book references
        book_references = re.findall(r'"(.*?)"\s*\(\d{4}\)', sentence)
        for ref in book_references:
            book_reference_candidates.append(ref.strip())

        # Check for the word "book" and extract book title
        if "book" in sentence.lower():
            book_title_match = re.search(r'"(.*?)"', sentence)
            if book_title_match:
                print("meh",book_title_match)
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

The author shared an interesting insight into his writing process. He said, "Writing is a way of thinking on paper." This nugget of wisdom resonated with many listeners.

Later in the conversation, the host mentioned a TED talk by Susan Cain (2012), titled "The Power of Introverts." This was another valuable reference.
"""

nugget_candidates, book_reference_candidates, other_reference_candidates = extract_candidates(long_text)

print("Nugget Candidates:")
for candidate in nugget_candidates:
    print(candidate)

print("\nBook Reference Candidates:")
for candidate in book_reference_candidates:
    print(candidate)

print("\nOther Reference Candidates:")
for candidate in other_reference_candidates:
    print(candidate)
