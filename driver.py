x=int(input('enter no of inputs \n'))
k=l=m=n=o=p=0
for i in range(1,x):
    a=input("please enter the input \n")
    if 'employee' in a:
        k=1
        print("employee are doing thier job to save nature because every one is connected to nature")
    if 'nature' in a:
        l=1
        print("all employee and employer are directly inherent to nature")
    if 'employer' in a:
        m=1
        print('All employee and employer are doing a meeting and everyone inherently connected to nature')
    if 'cabin' in a:
        n=1
        print('All employee and employer are in a cabin and everyone inherently connected to nature')
    if 'meeting' in a:
        o=1
        print('All employee and employer are sitting in a cabin,all furniture is inherently connected to nature ')
    if 'furniture' in a:
        p=1

    if k==1:
        if l==1:
            if m==1:
                if n==1:
                    if o==1:
                        if p==1:
                            print('All employee and employer are sitting on furniture in a cabin,all furniture is inherently connected to nature ')
                    else:
                        print('All employee and employer are sitting in a cabin,all furniture is inherently connected to nature ')
                else:
                    print('All employee and employer are in a cabin and everyone inherently connected to nature')
            else:
                print('All employee and employer are doing a meeting and everyone inherently connected to nature')
        else:
            print("all employee and employer are directly inherent to nature")
    else:
        print("employee are doing thier job to save nature because every one is connected to nature")
        
                            
                            
            
        

    
    
