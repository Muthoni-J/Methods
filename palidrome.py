def palidromeStr(text):
    start, end = 0, len(text)-1
    while start< end:
        text[start], text[end] = text[end] ,text[start]
        start += 1
        end -= 1
  
text= "My school is AkiraChix"     
palidromeStr(str)
print(str)