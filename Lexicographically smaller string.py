'''Given two strings s and t, both consisting of lowercase English letters and digits, your task is to calculate how many ways exactly one digit could be removed from one of the strings so that s is lexicographically smaller than t after the removal. Note that we are removing only a single instance of a single digit, rather than all instances (eg: removing 1 from the string a11b1c could result in a1b1c or a11bc, but not abc).

Also note that digits are considered lexicographically smaller than letters.

Example

For s = "ab12c" and t = "1zz456", the output should be solution(s, t) = 1.

Here are all the possible removals:

We can remove the first digit from s, obtaining "ab2c". "ab2c" > "1zz456", so we don't count this removal
We can remove the second digit from s, obtaining "ab1c". "ab1c" > "1zz456", so we don't count this removal
We can remove the first digit from t, obtaining "zz456". "ab12c" < "zz456", so we count this removal
We can remove the second digit from t, obtaining "1zz56". "ab12c" > "1zz56", so we don't count this removal
We can remove the third digit from t, obtaining "1zz46". "ab12c" > "1zz46", so we don't count this removal
We can remove the fourth digit from t, obtaining "1zz45". "ab12c" > "1zz45", so we don't count this removal
The only valid case where s < t after removing a digit is "ab12c" < "zz456". Therefore, the answer is 1.

For s = "ab12c" and t = "ab24z", the output should be solution(s, t) = 3.

There are 4 possible ways of removing the digit:

"ab1c" < "ab24z"
"ab2c" > "ab24z"
"ab12c" < "ab4z"
"ab12c" < "ab2z"
Three of these cases match the requirement that s < t, so the answer is 3.

Input/Output

[execution time limit] 4 seconds (py3)

[memory limit] 1 GB

[input] string s

A string consisting of lowercase English letters and digits 0..9.

Guaranteed constraints:
1 ≤ s.length ≤ 103.

[input] string t

A string consisting of lowercase English letters and digits 0..9.

Guaranteed constraints:
1 ≤ t.length ≤ 103.

[output] integer

The number of ways to remove exactly one digit from one of the strings so that s is lexicographically smaller than t after the removal.'''

def solution(s, t):
    c=0
    for x in range(len(s)):
        
        if s[x] in '123456789':
            temp_s=s[:x]
            if x<len(s)-1:
                temp_s=temp_s+s[x+1:]
            if len(s)==1:
                temp_s=s
            
            for i in range(len(temp_s)):
            
                if temp_s[i]>t[i]:
                    break  
                if temp_s[i]<t[i]:
                    c+=1
                    break
            
    
    for x in range(len(t)):
        
        if t[x] in '123456789':
            temp_t=t[:x]
            if x<len(t)-1:
                temp_t=temp_t+t[x+1:]
            if len(t)==1:
                temp_t=t

            for i in range(len(temp_t)):

                if s[i]>temp_t[i]:
                    break  
                if s[i]<temp_t[i]:
                    c+=1
                    break
                           
    return c  
        
