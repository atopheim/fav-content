import glob
import os


# Alternatively you can use web search and link to the transcript!
def split_inputs(filename: str):
    """
    Split input text into 4000 character or 500 word chunks
    """
    
    with open(filename, "r") as transcript:
        content = transcript.readlines()
        wordcount = 0
        character_count = 0
        chunks: list[str] = []
        last_split = 0
        for i, line in enumerate(content):
            if (character_count + len(line)) // 8000 > 0:
                chunks.append("".join(content[last_split:i-1]))
                last_split = i-1
                character_count = 0
                wordcount = 0
            # if (wordcount + len(line.split(" "))) // 500 > 0:
            #     chunks.append("".join(content[last_split:i-1]))
            #     last_split = i-1
            #     character_count = 0
            #     wordcount = 0
            character_count += len(line)
            wordcount += len(line.split(" "))

    for i, chunk in enumerate(chunks):
        with open(filename.split(".")[0] + "_" + str(i) + ".txt", "w") as outfile:
            if chunk:
                outfile.write(chunk)



# Define the path where you want to search for transcript.txt files

search_path = os.getcwd()
# Use glob to find all files called transcript.txt in the search path
file_paths = glob.glob(search_path + "/**/transcript.txt", recursive=True)

# Print the file paths
for path in file_paths:
    print(path)
    input("continue?")
    split_inputs(filename=path)

