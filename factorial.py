def maximizingXor(L, R):
    # The XOR of the largest number L and R will give the maximum possible result
    max_xor = 0
    
    # Iterate over all pairs of integers from L to R
    for a in range(L, R+1):
        for b in range(a, R+1):
            # Compute XOR of a and b
            xor_value = a ^ b
            # Keep track of the maximum XOR value
            if xor_value > max_xor:
                max_xor = xor_value
                
    return max_xor

if _name_ == '_main_':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    L = int(input().strip())
    R = int(input().strip())

    result = maximizingXor(L, R)

    fptr.write(str(result) + '\n')
    fptr.close()