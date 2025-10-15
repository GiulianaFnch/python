'''
Palindrome Check: Write a function is_palindrome(s) that returns 
True if the string is the same forward and backward (ignore spaces/case).
'''


def is_palindrome(s):
    string = s.strip().lower() # remove espaços e coloca em minusculas
    first, last = 0, len(string) - 1 # ponteiros primeiro e ultimo (comprimento -1)
    while first < last:  
        if string[first] == string[last]: # compara os caracteres
            first += 1 # avança os ponteiros
            last -= 1  # recua os ponteiros
        else:
            return False # se encontrar um par diferente
    return True 

print(is_palindrome("Ana"))
    