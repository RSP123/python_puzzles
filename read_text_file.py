# This program reads text file
# Print no. of sentence and words count

#Function to read text file

def read_text_file(file_name):
    with open('file_name','r') as new_file:
        file_data = new_file.readline()
        words_count = file_data.split()
        words += len(words_count)
    return words

# Main Function

if __name__ == "__main__":
    file_name = input("Enter file name to read it >>>")

    print("----------Selected file : ",file_name + "----------")
    print("Number of words : ", read_text_file(file_name))
