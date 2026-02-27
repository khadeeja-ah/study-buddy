t=int(input("Time to plan your learning for today!\nHow many chapters are you planning on studying today? :  "))
sl=[]
cl=[]
ll=[]
hl=[]
dl=[]
for i in range (t):
    s=input("Enter subject: ")
    c=input("Enter chapter: ")  
    l=int(input("Enter length of chapter: "))
    h=float(input("Enter no: of hours: "))
    d=int(input("Enter level of difficulty:\n1 for difficult\n2 for medium\n3 for easy\n"))
    while d!=1 and d!=2 and d!=3 :
        print("Invalid Option")
        print()
        d=int(input("Enter level of difficulty again:\n1 for difficult\n2 for medium\n3 for easy\n"))
    print()
    sl.append(s)
    cl.append(c)
    ll.append(l)
    hl.append(h)
    dl.append(d)
left=list(range(t))
o=[]
while left:
    high=left[0]
    for j in left:
        if dl[j]<dl[high] or (dl[j]==dl[high] and ll[j]>ll[high]):
            high=j
    o.append(high)
    left.remove(high)
print("Here's your study plan for today, from first chapter to last:")
for k in o:
    print("Subject: ",sl[k], "\nChapter: ",cl[k], "\nLength of chapter: ",ll[k]," pages\nNo: of hours:",hl[k])
    print()
print("Let's get grinding!")

#Motivational quotes list
quotes = ["Believe in yourself and all that you are!",
                 "Small progress each day adds up to big results.",
                 "Don’t stop until you’re proud.",
                 "Push yourself, because no one else is going to do it for you."]
while True:
    print("\n--- Delete Chapter Menu ---")
    print("1. Delete Chapter")
    print("2. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        ch_name = input("Enter chapter name to delete: ")
        found = False
        for i in range(len(cl)):
            if cl[i].lower()==ch_name.lower():
                found=True
                print("Deleted:", sl[i], "-", cl[i])
                sl.pop(i)
                cl.pop(i)
                ll.pop(i)
                hl.pop(i)
                dl.pop(i)
                break
        if found == False:
            print("Chapter not found.")

          # Show a motivational quote after deleting
        import random
        i=(random.randrange(len(quotes)))
        print(quotes[i])

    elif choice == "2":
        print("Stay motivated and keep grinding!")
        break

    else:
        print("Invalid choice. Try again.")

#Summary report

N={'sub':sl,'chp':cl,'length':ll,'hours':hl,'difficulty':dl}
print('\nSummary report')
for i in range(len(N['sub'])):
    print('\nSubject:',N['sub'][i],'-')
    print('Chapter\t\tLength\t\tHours')
    print(N['chp'][i],'\t\t',N['length'][i],'\t\t',N['hours'][i])
print("\nCongratulations! Today's goal is complete")

#Editing
e=input("\nDo you want to edit the study details entered earlier(Yes/No):")
if e.lower()=='yes':
    print('''Type 
1 to Add
2 to Delete
3 to Make changes to an existing chapter''')
    o=int(input("Enter your choice (from 1 to 3):"))
    if o==1:
        n=int(input("How many chapters do you wish to add:"))
        for i in range(n):
            s=input("Enter subject: ")
            c=input("Enter chapter: ")
            l=int(input("Enter length of chapter: "))
            h=float(input("Enter no: of hours: "))
            d=int(input("Enter level of difficulty:\n1 for difficult\n2 for medium\n3 for easy\n"))
            while d!=1 and d!=2 and d!=3 :
                print("Invalid Option")
                print()
                d=int(input("Enter level of difficulty again:\n1 for difficult\n2 for medium\n3 for easy\n"))
            print()
            sl.append(s)
            cl.append(c)
            ll.append(l)
            hl.append(h)
            dl.append(d)
            print('\nSubject:',s,'\nChapter:',c,'\nLength:',l,'\nHours:',h)
            print()
        print('\n')
        print("\t\t\t\t!Chapter Added Successfully!")
    elif o==2:
        det=input("Enter the chapter you want to delete:")
        for i in range(len(cl)):
            if det.lower()==cl[i].lower():
                       sl.pop(i)
                       cl.pop(i)
                       ll.pop(i)
                       hl.pop(i)
                       dl.pop(i)
                       break
        print('\n')
        print("\t\t\t\t!!Deleted Chapter Successfully!!")
    elif o==3:
        m=input("Enter the chapter to which changes is to be made:")
        for i in range(len(cl)):
            if m.lower()==cl[i].lower():
                print("Enter the updated values to the following details")
                l2=int(input("Enter new length of chapter: "))
                h2=float(input("Enter no: of hours: "))
                d2=int(input("Enter level of difficulty:\n1 for difficult\n2 for medium\n3 for easy\n"))
                ll[i]=l2
                hl[i]=h2
                dl[i]=d2
                print("The updated chapter details are:",'\nChapter-',cl[i],'\nLength-',ll[i],'\nHours-',hl[i],'\nDifficulty-',dl[i])
                print("\n")
                print("\t\t\t\tUpdated Chapter Successfully")
                break
        else:
            print("Chapter not found")
    else:
        print("Invalid choice")

elif e.lower()=="no":
    print("No changes to be made")
else:
    print("Invalid Choice")
print()
print('\n')


#Searching and Marking status

status = []
for i in range(len(cl)):
    status.append(0)

while True:
    print("\n--- Search / Update Menu ---")
    print("1. Search by Subject")
    print("2. Search by Chapter")
    print("3. Mark Chapter as Completed")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        sub = input("Enter subject name to search: ")
        count = 0

        for i in range(len(sl)):
            if sl[i].lower() == sub.lower():
                count = count + 1
                print("\nSubject:", sl[i])
                print("Chapter:", cl[i])
                print("Hours:", hl[i])
                if status[i] == 1:
                    print("Status: Completed")
                else:
                    print("Status: Not Completed")

        if count == 0:
            print("Subject not found.")

    elif choice == "2":
        ch = input("Enter chapter name to search: ")
        count = 0

        for i in range(len(cl)):
            if cl[i].lower() == ch.lower():
                count = count + 1
                print("\nSubject:", sl[i])
                print("Chapter:", cl[i])
                print("Hours:", hl[i])
                if status[i] == 1:
                    print("Status: Completed")
                else:
                    print("Status: Not Completed")

        if count == 0:
            print("Chapter not found.")

    elif choice == "3":
        ch = input("Enter chapter name to mark completed: ")
        count = 0

        for i in range(len(cl)):
            if cl[i].lower() == ch.lower():
                status[i] = 1
                count = count + 1
                print("Chapter marked as completed.")
                break

        if count == 0:
            print("Chapter not found.")

    elif choice == "4":
        print("Exiting search menu.\n\nGreat work today! Stay consistent, stay focused, and success will follow..")
        break

    else:
        print("Invalid choice. Try again.")

