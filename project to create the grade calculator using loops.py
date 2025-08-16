n=int(input('Enter the no.of subjects:'))

mark=[]

total=0


for i in range(1,n+1):
    a=int(input(f'\nEnter marks in subject {i}:'))

    mark.append(a)

    total+=mark[0]

avg=total/n
print('\nyour total marks is:',total)
print('\nYour average is:',avg)
if avg==100:
    print('\nYou got \'O\' grade')

elif avg>=94:
    print('\nYou got \'A+\' grade')

elif avg>=85:
    print('\nYou got \'A\' grade')

elif avg>=75:
    print('\nYou got \'B\' grade')


elif avg==35:
    print('\nJust pass')

else:
    print('\nYou are failed')

    
