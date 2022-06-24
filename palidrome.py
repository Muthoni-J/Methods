def word(a):
  y=a.split()
  start=0
  end=len(y)-1
  while start<end:
    y[start],y[end]=y[end],y[start]
    start+=1
    end-=1
    b=' '
  print(b.join(y))
word("I study at AkiraChix")  
p="AkiraChix at study I"
