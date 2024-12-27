def caesar_decode(ciphertext):
    # Alphabet to be used for decoding
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Convert the ciphertext to uppercase to standardize (caesar ciphers are case-insensitive)
    ciphertext = ciphertext.upper()
    
    # Try all 26 possible shifts (0-25)
    for shift in range(26):
        decoded_message = ''
        
        # Decode each character by shifting it backwards
        for char in ciphertext:
            if char in alphabet:
                # Find the new shifted index
                shifted_index = (alphabet.index(char) - shift) % 26
                # Append the shifted character to the decoded message
                decoded_message += alphabet[shifted_index]
            else:
                # Keep non-alphabet characters as they are
                decoded_message += char
        
        # Print the result for this shift
        print(f'Shift {shift}: {decoded_message}')

# Example usage
ciphertext = "WKLV LV D WHVW PHVVDJH"  # Encrypted text
caesar_decode(ciphertext)
