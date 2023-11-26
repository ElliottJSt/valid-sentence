# Test file for validsentence.py and the isValid function.

from validsentence import check_valid_sentence

testSentences = ["The quick brown fox said \"hello Mr lazy dog\".",
                 "The quick brown fox said hello Mr lazy dog.",
                 "One lazy dog is too few, 13 is too many.",
                 "One lazy dog is too few, thirteen is too many.",
                 "How many \"lazy dogs\" are there?"
                 "The quick brown fox said \"hello Mr. lazy dog\".",
                 "the quick brown fox said \"hello Mr lazy dog\".",
                 "The quick brown fox said \"hello Mr lazy dog.\"",
                 "One lazy dog is too few, 12 is too many.",
                 "Are there 11, 12, or 13 lazy dogs?",
                 "There is no punctuation in this sentence"]
try:
    y = 1
    for x in testSentences:
        print(f"Test {y}: {x}")
        y += 1
        if check_valid_sentence(x):
            print("Passed")
        else:
            print("Failed")
    check_valid_sentence(12)
except Exception as e:
    print("Error occurred: ", e)
