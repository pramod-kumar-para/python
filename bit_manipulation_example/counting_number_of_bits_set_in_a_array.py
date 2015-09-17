list_of_numbers=[1,2,3,4,5,6]

def count_bits(n):
    count=0
    for i in n:
        while i:
            # performing '&' with 1 to check for last bit
            count+=i&1
            # performing a right shift by 1 bit
            i>>=1
    return count

print(count_bits(list_of_numbers))
