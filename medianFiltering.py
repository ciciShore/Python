#Ciera Headley
#CS:1210:0A01
#medianFiltering.py
#Homework 15
def medfiltering():
    #open all the files
    f1=open('IMG_1.ppm','rU')
    f2=open('IMG_2.ppm','rU')
    f3=open('IMG_3.ppm','rU')
    f4=open('IMG_4.ppm','rU')
    f5=open('IMG_5.ppm','rU')
    f6=open('IMG_6.ppm','rU')
    f7=open('IMG_7.ppm','rU')
    f8=open('IMG_8.ppm','rU')
    f9=open('IMG_9.ppm','rU')
    
    #read files one through nine and split the numbers start the files from th pixel data
    one = f1.read()  
    one = one.split()
    one = one[3:]

    
    two = f2.read() 
    two = two.split()
    two = two[3:]

    three = f3.read() 
    three = three.split()
    three = three[3:]
    
    four = f4.read() 
    four = four.split()
    four = four[3:]
 
    five = f5.read()
    five = five.split()
    five = five[3:]
    
    six = f6.read()   
    six = six.split()
    six = six[3:]

    seven = f7.read()        
    seven = seven.split()
    seven = seven[3:]

    eight = f8.read()
    eight = eight.split()
    eight = eight[3:]

    nine = f9.read()
    nine = nine.split()
    nine = nine[3:]
    
    #create and empty list
    
    finalL=[]
    
    #Create a counter
    count = 0
    
    #for the pixel index in file one we will go though and take the numbers need for the final List
    for i in one:
        count = count + 1
        L1 = one[count:count+1]+two[count:count+1]+three[count:count+1]+four[count:count+1]+five[count:count+1]+six[count:count+1]+seven[count:count+1]+eight[count:count+1]+nine[count:count+1]
        L2 = sorted(L1)
        L3 = L2[4:5]
        finalL = finalL + L2
    
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()
    f8.close()
    f9.close()
    
    #turn the strings into intergers
       
    finalL = map(int,finalL)
    #turn into a list
    finalL= list(finalL)
    #counter staring at zero
    index =0
    #while the counter is less than the final list insert the things need to create the median filtered list
    while index < len(finalL):
        finalL.insert(index+3,'\n')
        finalL.insert(index+2,' ')
        finalL.insert(index+1,' ')
        index=index+6
    
    
    finalL.insert(0,"255" + '\n')
    finalL.insert(0,"250 167" + "\n")
    finalL.insert(0,"P3"+'\n')
    finalL=map(str,finalL)
    finalL=list(finalL)
    final=''.join(finalL)
    file=open('IMG_final.ppm','w')
    file.write(final)
    file.close()
    
    