import markdown
x=input("Enter filename : ")
fhand=open(x)
html=markdown.markdown(fhand.read())
print(html)
y=x.split(".")
y=y[0]+".html"
fhand2=open('temp.html')
html=html.format(fhand2.read())
fhand=open(y,'w')
fhand.write(html)