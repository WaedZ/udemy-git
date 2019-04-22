def main():
    grade_one= {'Sami': [19, 18, 19.5, 30, 10], 'Ahmad': [15, 14, 16, 21, 7],
     'Faris': [18, 19, 17, 26, 9], 'Salem': [20, 20, 19, 30, 10], 'Mahmoud': [12, 13, 11, 18, 7]}

    grade_two= {'Lana': [17, 19, 20, 28, 9], 'Dina': [18.5, 19.5, 20, 29, 10], 'Maha': [20, 20, 18, 26, 9], 'Abeer': [16, 18, 19.5, 25, 8]}

    grade_three= {'Rima': [18, 19, 18, 26, 9], 'Tala': [20, 20, 19, 29, 10], 'Lamar': [19, 20, 18, 26, 9],
    'Rola': [15, 14, 16, 19, 7], 'Naya': [9, 6, 11, 14, 7], 'Dalal': [1, 5, 2, 6, 7], 'Ola': [19.5, 20, 20, 29.5, 10]}

    #Function one
    def students_names (class_name):
           if (class_name == "grade_one"):
               print(grade_one.keys())

           elif (class_name == "grade_two"):
               print(grade_two.keys())
           elif(class_name=="grade_three"):
               print(grade_three.keys())
    #Function Two
    def student_scores (class_name,student_name):
         if (class_name == "grade_one"):
            s = list(grade_one.get(student_name))
            print(sum(s))

         elif (class_name == "grade_two"):
            s = list(grade_two.get(student_name))
            print(sum(s))

         elif(class_name =="grade_three"):
             s = list(grade_three.get(student_name))
             print(sum(s))

    #Function Three
    def students_count (class_name):
         if (class_name == "grade_one"):
            s = list(grade_one.keys())
            print(len(s))

         elif (class_name == "grade_two"):
            s = list(grade_two.keys())
            print(len(s))

         elif(class_name =="grade_three"):
             s = list(grade_three.keys())
             print(len(s))

    #End of defining the functions and the dictionaries
    # Start the program
    fun = input('Choose One: students_names,student_scores,students_count: ')

    if (fun == "students_names"):
        c_name = input('Enter A Class Name (grade_one or grade_two or grade_three): ')
        students_names(c_name)

    elif (fun == "student_scores"):
        c_name = input('Enter A Class Name (grade_one or grade_two or grade_three): ')
        s_name= input('Enter A Student Name to get the score: ')
        student_scores(c_name,s_name)

    elif (fun == "students_count"):
        c_name = input('Enter A Class Name (grade_one or grade_two or grade_three): ')
        students_count(c_name)
    #At the End
    restart = input('Choose Done if you finished OR Choose More for more functions: ')
    if (restart == "More"):
        main()

    else:
        exit() 
#start code
main()
