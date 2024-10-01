# f=open('text.txt','x')
# f.write('hey good morning\n')

# f=open('text.txt','a')
# f.write('welcome all\n')
# f.write('enjoy the journey')
f=open('text.txt','r')
a=len(f.readlines())
print(a)
f.seek(0)
longest=''
for i in range(a):
    l=f.readline().strip()
    s=l.split(' ')
    for j in s:
        if j!='':
            if len(longest)<len(j):
                longest=j
print('longest is ',longest)