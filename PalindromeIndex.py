def IsPalindromo(s):
     if s==s[::-1]:
        return -1

def letras_extras(s):
    if s==s[::-1]:
        return -1
    l=0
    i=0
    j=len(s)-1
    for i in range(0,len(s)):
        if s[i]!=s[j]:
            newWord=''
            for k in range(0,len(s)):
                if k!=i:
                    newWord+=s[k]
            if IsPalindromo(newWord)==-1:
                return i
        j -= 1
