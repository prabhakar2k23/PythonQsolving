s="mynameissamrat"

def vowel_count(s):
    vowels = "aeiouAEIOU"
    sum=0
    for i in range(len(s)):
        if s[i] in vowels:
            sum += 1
    return sum
