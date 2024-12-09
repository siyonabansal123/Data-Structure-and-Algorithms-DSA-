def largest_lexicographic_string(N):
    binary_representation = bin(N)[2:][::-1]
    print(binary_representation)
    characters = []
    
    for i, bit in enumerate(binary_representation):
        print(bit)
        if bit == '1':
            characters.append(chr(ord('a') + i))
    
    characters.sort(reverse=True)
    
    return ''.join(characters)

# Example usage
N = 8
print(largest_lexicographic_string(N))  # Output: "dca"


