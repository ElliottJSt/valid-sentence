def check_valid_sentence(inp):
    # First checks if input is a String
    if not (isinstance(inp, str)):
        raise ValueError("Invalid Data Type: Input must be a string")
    # Checks that it starts with a capital letter
    if not inp[0].isupper():
        return False
    # Checks that there are an even number of quotation marks
    if (inp.count("\"") % 2) != 0:
        return False
    # Checks that the String ends with one of the following sentence termination characters:
    if not inp[len(inp) - 1] in [".", "?", "!"]:
        return False
    # Checks that the String has no period characters other than the last character.
    if inp.count(".") > 1:
        return False
    # Retrieves all the numbers in the list and checks that their value is greater than 12.
    nums = [int(x) for x in inp.split() if x.isdigit()]
    for i in nums:
        if 0 < i <= 12:
            return False
    # All conditions passed, sentence is valid.
    return True

