
# encryption using a linear feedback shift register
import bindec


Base64List = [
    ('000000', 'A'), ('000001', 'B'), ('000010', 'C'), ('000011', 'D'),
    ('000100', 'E'), ('000101', 'F'), ('000110', 'G'), ('000111', 'H'),
    ('001000', 'I'), ('001001', 'J'), ('001010', 'K'), ('001011', 'L'),
    ('001100', 'M'), ('001101', 'N'), ('001110', 'O'), ('001111', 'P'),
    ('010000', 'Q'), ('010001', 'R'), ('010010', 'S'), ('010011', 'T'),
    ('010100', 'U'), ('010101', 'V'), ('010110', 'W'), ('010111', 'X'),
    ('011000', 'Y'), ('011001', 'Z'), ('011010', 'a'), ('011011', 'b'),
    ('011100', 'c'), ('011101', 'd'), ('011110', 'e'), ('011111', 'f'),
    ('100000', 'g'), ('100001', 'h'), ('100010', 'i'), ('100011', 'j'),
    ('100100', 'k'), ('100101', 'l'), ('100110', 'm'), ('100111', 'n'),
    ('101000', 'o'), ('101001', 'p'), ('101010', 'q'), ('101011', 'r'),
    ('101100', 's'), ('101101', 't'), ('101110', 'u'), ('101111', 'v'),
    ('110000', 'w'), ('110001', 'x'), ('110010', 'y'), ('110011', 'z'),
    ('110100', '0'), ('110101', '1'), ('110110', '2'), ('110111', '3'),
    ('111000', '4'), ('111001', '5'), ('111010', '6'), ('111011', '7'),
    ('111100', '8'), ('111101', '9'), ('111110', '+'), ('111111', '/')
]




def charToBin(c):
    binlist = [] 
    for binary, char in Base64List:  # Fetching data from the custom Base64 list 
        if c == char:
            return binary  # Return the binary string directly

    return None  # Return None if the character is not found
            

def binToChar(b):
    # Convert the list of bits to a binary string
    binchar = ''.join(map(str, b))
    
    # Initialize the character to return
    ch = ''
    
    # Fetching data from the custom Base64 list
    for binary, char in Base64List:  # Ensure Base64List contains tuples (binary, character)
        if binchar == binary:  # Compare with the binary string
            ch += char  # Append the matching character
            break  # Break the loop after finding a match

    return ch  # Return the character



# convert a string of characters into a list of 1's and 0's using Base64 encoding 
def strToBin(s): 
    binlist = [] 
    for i in s:
        binlist.extend(charToBin(i)) #Sending each character of the strig to charToBin function and getting the binary number 
#back 
        x = list(binlist) #Converting all the list chunks to a single list item. 
    return x


def binToStr(b_list): 
    binlist = [] 
    str= '' 
    for i in range(0, len(b_list), 6): 
        binlist.append( b_list[i:i + 6]) #Converting one single list item to 6 digit binary chunks. 
    for i in binlist: 
        str+= binToChar(i) #Sending each list item to binToChar and adding all the returned charecter to a string. 
    return str


# generates a sequence of pseudo-random numbers 
def generatePad(seed, k, length): 
    tappad =[] 
    tapposition = len(seed)-k 
    while(length!=0): 
        length-=1 
        if (seed[0]!=seed[tapposition]):
            seed.append(1) 
            tappad.append(1) 
            seed.pop(0) 
        else: 
            seed.append(0) 
            tappad.append(0) 
            seed.pop(0) 
    return tappad


def encrypt(message, seed, k):
    padlength = len(message) * 6  # Length for binary representation
    randomNumber = generatePad(seed=seed, k=k, length=padlength)  # Generate LFSR output
    binaryofmessage = strToBin(message)  # Convert message to binary
    encryptedbinary = []  # List to hold encrypted binary numbers

    # Ensure binaryofmessage is a list of integers
    binaryofmessage_int = [int(bit) for bit in binaryofmessage]  # Convert binary string to list of integers

    # Encrypting the message
    for i in range(len(binaryofmessage_int)):
        # XOR the binary representation of the message with the generated random number
        encryptedbinary.append(binaryofmessage_int[i] ^ randomNumber[i])

    # Convert the encrypted binary back to a string
    encryptedstring = binToStr(encryptedbinary)  # Ensure you have this function defined
    return encryptedstring


