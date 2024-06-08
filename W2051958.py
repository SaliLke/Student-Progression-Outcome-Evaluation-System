 # I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
 #Reference
   #Zelle, J.M. (2004) Python Programming: An Introduction to Computer Science.
   #CS Dojo (2018) How to use functions in Python(Python Tutorial #3):https://www.youtube.com/watch?v=NSbOtYzIQI0.
   #W3schools (2019).Python Lists.[online]W3schools.com: https://www.w3schools.com/python/python_lists.asp.
# Student ID: w20519586
# Date: 10/12/2023


#PART1
from graphics import *

print('Enter who you are,','\n 1- Student\n','2- staff member\n')
text=int(input('Enter 1 or 2:'))

def get_credits(credits):           #Validation
    while True:
        try:
            score=int(input(credits))
            if score in range(0,121,20):
                return score
            else:
                print('Out of range\n')
        except ValueError:
            print('Integer Required\n')

            
#HISTOGRAM
def histogram(progress_count,trailer_count,excluded_count,retriever_count):
    win = GraphWin("Histogram", 700, 700)
    win.setBackground("Mint Cream")

    my_heading = Text(Point(180, 30), 'Histogram Results')  #Heading
    my_heading.draw(win)                                   
    my_heading.setTextColor("grey")
    my_heading.setSize(22)
    my_heading.setStyle("bold")
    my_heading.setFace("helvetica")

    P_counts=int(550-(progress_count*25))
    T_counts=int(550-(trailer_count*25))
    R_counts=int(550-(retriever_count*25))
    E_counts=int(550-(excluded_count*25))

    aLine = Line(Point(70,550), Point(650,550))             #Graph
    aLine.draw(win)
    aRectangle = Rectangle(Point(120,P_counts), Point(220,550))
    aRectangle.setFill('Yellow')
    aRectangle.draw(win)
    aRectangle = Rectangle(Point(250,T_counts), Point(350,550))
    aRectangle.setFill('LightBlue')
    aRectangle.draw(win)
    aRectangle = Rectangle(Point(380, R_counts), Point(480,550))
    aRectangle.setFill('Lightpink')
    aRectangle.draw(win)
    aRectangle = Rectangle(Point(510,E_counts), Point(610,550))
    aRectangle.setFill('LightGreen')
    aRectangle.draw(win)

    aText = Text(Point(170, 570), "Progress")               #Labels
    aText.draw(win)
    bText = Text(Point(300, 570), "Trailer")
    bText.draw(win)
    cText = Text(Point(435, 570), "Retriever")
    cText.draw(win)
    dText = Text(Point(560, 570), "Excluded")
    dText.draw(win)

    eText = Text(Point(170,P_counts- 20), int(progress_count)) #Counts
    eText.draw(win)
    fText = Text(Point(300,T_counts- 20), int(trailer_count))
    fText.draw(win)
    gText = Text(Point(430,R_counts - 20), int(retriever_count))
    gText.draw(win)
    hText = Text(Point(560,E_counts- 20), int(excluded_count))
    hText.draw(win)

    texts=[aText,bText,cText,dText,eText,fText,gText,hText]  #Assinging details for labels and counts
    for item in texts:
        item.setTextColor("grey")
        item.setStyle("bold")
        item.setSize(15)


    total_outcome=int(progress_count+trailer_count+retriever_count+excluded_count)

    kText= Text(Point(200, 610), str(total_outcome)+ " outcomes in total") #Total Outcomes
    kText.setSize(22)
    kText.setTextColor("grey")
    kText.setStyle("bold")
    kText.draw(win)

CreditList=[]                       

def credits():                      #Input credits
    """Entering credits and receiving the progress of the students"""
    progress_count=0
    trailer_count=0
    retriever_count=0
    excluded_count=0
    outcome=''
    display_histogram=False
    credits_input=False
    while not credits_input:        #Credit Results
        Pass = get_credits('Enter your Pass credits:')
        Defer = get_credits('Enter your Defer credits:')
        Fail = get_credits('Enter your Fail credits:')
        Total = Pass + Defer + Fail
        if Total == 120:
            if Pass == 120:
                outcome='Progress'
                progress_count+=1
            elif Pass == 100:
                outcome='Progress(module trailer)'
                trailer_count+=1
            elif (Pass + Defer) < Fail:
                outcome='Exclude'
                excluded_count+=1
            else:
                outcome='Do not Progress(Module Retriever)'
                retriever_count+=1

            print(outcome)
        else:
            print('Total is incorrect\n')

        CreditList.append([outcome,Pass,Defer,Fail])    #Appending list elements

        if text==1:
            break
        
        while True:
            print('Would you like to enter another set of data?')
            more_credits = input("Enter 'y' for yes or 'q' to quit and view results:").lower()
            if more_credits== 'q':
                credits_input=True
                display_histogram=True
                break
            elif more_credits== 'y':
                break
            else:
                continue
            
            
    if display_histogram==True:
        histogram(progress_count,trailer_count,excluded_count,retriever_count)
credits()



#PART 2
def get_list():
    print('\nPart 2:')   
    for element in CreditList:   
            print(element[0],'-', element[1], element[2],element[3])
get_list()



# PART3
def get_text_file():
    f = open('test.txt', 'w')
    data = ''
    for item in CreditList:
        data+=f"{item[0]} - {item[1]},{item[2]},{item[3]}\n"

    f.write(data)
    f = open('test.txt', 'r')
    print('\nPart3')
    print(f.read())
    f.close()
get_text_file()

