# This program reads text file
# Print no. of sentence and words count

#Function to read text file

def read_text_file(file_name):
    count = []
    with open(file_name,'r') as new_file:
        file_data = new_file.read()

        words_count = file_data.split()
        s_count = file_data.count(\n)

        count.append(len(file_data))
        count.append(len(words_count))
        count.append(s_count)
        new_file.close()
    return count

# Main Function

if __name__ == "__main__":
    file_name = 'open.txt' # input("Enter file name to read it >>>")
    count = read_text_file(file_name)
    print("Selected file : ",file_name)
    print("No of sentence : ", count[2])
    print("No of words :", count[1])
    print("no of char:", count[0]-1)
