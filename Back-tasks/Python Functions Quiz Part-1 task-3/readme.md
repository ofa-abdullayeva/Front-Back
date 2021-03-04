1.Heç bir dəyəri açıq şəkildə qaytarmayan bir funksiyanın qaytarma dəyəri nədir?

 cvb:none

2. Aşağıdakı maddələrdən hansı funksiya başlığında mövcuddur?

  cvb:  function name and parameter list

3.Aşağıdakılardan hansı funksiyanın giriş parametrlərini və ya arqumentlərini əhatə edir?

   cvb:parentheses

4.Aşağıdakı açar sözlərdən hansı funksiya blokunun başlanğıcını göstərir?
   cvb: def

5.Sistemin funksiya çağırışının parametrlərini və lokal dəyişənlərini saxladığı yaddaş sahəsinə verilən ad necədir?   
  cvb:storage area
  duzgun cvb:a stack

6.Aşağıdakı funksiya tərifindən hansı biri dəyər vermir?  

 cvb: a function that prints integers from 1 to 100.

7. Aşağıdakı ifadələrdən hansı verilmiş kod parçasındakı funksiya bədənini düzgün təmsil edir?
    def f(number):
    # Missing function body
        print(f(5))
  cvb:   return number 


8.Aşağıdakı kod parçasının çıxışı nədir?   
    def func(message, num = 1):
        print(message * num)
 
    func('Welcome')
    func('Viewers', 3)

  cvb:  B. Welcome
           ViewersViewersViewers

9.Aşağıdakı kod parçasının çıxışı nədir? 

    def myfunc(text, num):
    while num > 0:
        print(text)
     num = num - 1

    myfunc('Hello', 4)

 cvb: D. infinite loop

10. Parametri olaraq qəbul edilmiş bir arqumentlə edilən bir funksiya çağırışı ilə aşağıdakılardan hansı ilə əlaqələndirərdiniz?
  cvb:B. pass by value

11.  Aşağıdakı kod parçasının çıxışı nədir?

   def func(x = 1, y = 2):
        x = x + y
        y += 1
        print(x, y)
    func(y = 2, x = 1)
cvb: 3 3

12.Aşağıdakı kod parçasının çıxışı nədir?

    num = 1
    def func():
        num = 3
        print(num)

    func()
    print(num)

 cvb: 3 1

13. Aşağıdakı kod parçasının çıxışı nədir?

    num = 1
    def func():
        num = num + 3
        print(num)

    func()
    print(num)


 cvb:  C. The program has a runtime error because the local variable ‘num’ referenced before assignment.(Proqramda iş vaxtı xətası var, çünki ‘num’ yerli dəyişəninə atamadan əvvəl istinad edilmişdir.) 

14.  Aşağıdakı kod parçasının çıxışı nədir?

    num = 1
    def func():
        global num
        num = num + 3
        print(num)

    func()
    print(num)

 cvb: 4 4   


15.  Aşağıdakı kod parçasının çıxışı nədir?
        def test(x = 1, y = 2):
            x = x + y
            y += 1
        print(x, y)

        test()
    cvb: 3 3


16.  Aşağıdakı kod parçasının çıxışı nədir?  

       def test(x = 1, y = 2):
            x = x + y
            y += 1
            print(x, y)

        test(2, 1)

    cvb:3 2     

17.  Aşağıdakı kod parçasının çıxışı nədir?  


   def test(x = 1, y = 2):
        x = x + y
        y += 1
        print(x, y)

    test(y = 2, x = 1)

  cvb:3 3  

18.Aşağıdakı kod parçasının çıxışı nədir?  

   cvb:C. def f(a = 1, b = 1, c = 2):
   
19. Aşağıdakı kod parçasının çıxışı nədir?
   exp = lambda x: x ** 3
   print(exp(2))

 cvb: C. 8  

20.Aşağıdakı kod parçasının çıxışı nədir?

        myList = [lambda x: x ** 2,
                lambda x: x ** 3,
                lambda x: x ** 4]
    
        for f in myList:
            print(f(3))

    cvb:  C. 9
            27
            81 

