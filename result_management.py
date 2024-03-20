import pandas as pd
#to import excel sheet we use pandas and to use mathematical operation
import matplotlib.pyplot as plt
# graphical visualization
str1=input("Enter the UserName: ")
# to import excelsheet using pandas
df = pd.read_excel(r"C:\Users\dell\Documents\class record main.xlsx")
df.set_index('Roll Number', inplace=True)
# to find the percentage of students
S=int(input("\nEnter the Maximum Marks in each subject: "))
df["Total Marks"]=df.sum(axis = 1, numeric_only = True)
df["Percentage %"]=(df["Total Marks"]/(len(df.select_dtypes(['int64']).columns)*S))*100
# to check the authenticity of the user
while str1 == "Maninderpal Singh" or str1 == "Insha Altaf" or str1 == "Deepak thakur":
    N = int(input("What do you want to do? "))
    if N == 1:
        print(df)
    # to find the grade of each student
    elif N == 2:
        grade = []
        for i in df["Percentage %"] :
            if(i >= 90):
                grade.append("A Grade")
            elif(90 > i >= 80):
                grade.append("B Grade")
            elif(80 > i >= 70):
                grade.append("C Grade")
            elif(70 > i >= 60):
                grade.append("D Grade")
            elif(60 > i >= 40):
                grade.append("E Grade")
            else:
                grade.append("Fail")
        df["Grade"] = grade
        print(df)
    # to check the record of any particular student
    elif N == 3:
        S1=int(input("Enter the Student Roll Number: "))
        data2 = df.loc[S1]
        print("\nStudent Result: \n\n",data2)
    #to show minimum and maximum marks of each subject
    elif N == 4:
        print("Minimum Marks in MCP, Python, MCP(Practical), Python(Practical)", df['MCP'].min(), df['Python'].min(), df['MCP(Practical)'].min(), df['Python(Practical)'].min())
        df.min(numeric_only=True)
        print("Maximum Marks in MCP, Python, MCP(Practical), Python(Practical)", df['MCP'].max(), df['Python'].max(), df['MCP(Practical)'].max(), df['Python(Practical)'].max())
        df.max(numeric_only=True)
    #to see the topper name
    elif N == 5:
        print("\nClass Topper: \n",df["Total Marks"].idxmax(),df._get_value(df["Total Marks"].idxmax(), "Name"))
    #to see the composition of marks in class
    elif N == 6:
        c=[str(x) for x in input("Enter the Colors of your choice: ").split(",")]
        df.plot(kind="pie",y="Percentage %",title= "Class Performance", legend=False, explode=[0.1,0.1,0.1,0.1,0.1,0.1,0.2,0.1,0.1,0.1], autopct="%.2f", colors=c)
        plt.show()
    else:
        break
else:
    print("Invalid UserName")