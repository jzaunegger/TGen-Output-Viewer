import os, sys

'''
    Function to iterate through the files to print out a specific sentence.
'''
def printSentence(id, dataset):

    sentences_id = int(id)

    for file_data in dataset:
        current_sentences = dataset[file_data]

        current_sentence_data = current_sentences[sentences_id].replace("\n", "")

        file_name = file_data.replace('.txt', '')

        print('File {:15s} Sentence: {}'.format(file_name, current_sentence_data))
    print("==========================================================")


'''
    Helper function that checks if a string variable can be cast to 
    a integer.
'''
def isInt(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


'''
    Recursive Function that will continue to prompt a user to input a 
    number to view that sentence from each of the files.
'''
def prompt(dataset, num_sentences):
    print("If you would like to view a specific sentence from each file")
    print("please enter a number between 0 and {}. ".format(len(sentences)-1))
    input_value = input('Sentence Value: ')
    print("==========================================================")

    if input_value == 'exit':
        sys.exit()
    
    elif isInt(input_value) == True:
        value = int(input_value)

        if value < 0 or value >= num_sentences:
            print('* Error: Please enter a valid number.')
            prompt(dataset, num_sentences)

        else:
            printSentence(value, dataset)
            prompt(dataset, num_sentences)


'''
    Main Program
'''
# Check if dataset path exists
dataset_path = os.path.join(os.getcwd(), 'dataset')
if os.path.exists(dataset_path):
    dataset = os.listdir(dataset_path)

    file_data = {}

    # Parse the files
    for file_name in dataset:

        file_path = os.path.join(dataset_path, file_name)

        # Read a file
        current_file = open(file_path, mode='r')
        data = current_file.readlines()
        
        line_data = []
        for line in data:
            line_data.append(line)

        file_data[file_name] = line_data

        current_file.close()

    # Log Information
    sent_len = 0

    print("The dataset has {} files.".format( len(file_data.keys())) )
    print("==========================================================")
    for key in file_data:
        sentences = file_data[key]
        sent_len = len(sentences)

        print('File "{}" has {} sentences.'.format(key, sent_len))
    print("==========================================================")

    prompt(file_data, sent_len)