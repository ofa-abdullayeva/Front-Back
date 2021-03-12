1.Jinja template nədir? Necə istifadə olunur?
cvb: Jinja , Python proqramlaşdırma dili üçün bir veb şablon mühərrikidir.Tekrar olunan kodlari her hansi bir html sehifesine yaziriq ve o sehifeni extend edirik ehtiyac olan diger sehifelere.


2.Database migration nədir necə istifadə olunur?
cvb:Databasedeki datalari alir,kopyasini yaradir.Yaddasda saxlayir.Her deyisiklik olunanda ,yeni deyisikliyin uzerine saxlanilan datani elave edir.
   yuklemek ucun
   ctrl+C
   Pip install Flask-Migrate
   sonra   (Import olunur (x.py) faylinin icine)
   from flask_migrate import Migrate

   MIGRATION SYSTEM
   -1-app.py de yazilir-migrate = Migrate(app,db)
   -2-terminalda-Flask db init (migration papkasi yaranir)
   -3-Flask db  migrate -m "First migration"
   deyisiklikden sonra
   -4-Flask db  migrate -m "new migration"
   -5-flask db upgrade  (olunan deyisikliyi database e tetbiq edir)

3.Flask Forms nədir? Necə istifadə olunur?


4.Flask layihəsinin folder ve fayl strukturunu necə optimallaşdıra bilərik?
cvb:


5.Flask Blueprint nədir? Necə istifadə olunur?
cvb:Layihe plani,layihəmizi hissə-hissə yarada, beləliklə layihə idarə olunmasını asanlaşdıra bilərik.Pytondaki qarisiqligi aradan qaldirmaq ucun istifade olunur.







GET VE POST METHODLARI HAQQINDA
-GET
GET metodu serverdən məlumat almaq üçün istifadə olunur. Sizə çox tanış görünür, çünki bu prosedurları əvvəlki dərslərimizdə həmişə etmişik. Məsələn, veb səhifəmizi açarkən və ya saytdakı hər hansı bir səhifəyə daxil olduqda bir ünvan tələb edirik və bu tələb brauzerdə GET metodu ilə edilir.

-POST
POST metodu, məlumatları serverə göndərmək üçün istifadə olunan HTTP metodudur. POST metodu ilə serverə məhdudiyyətsiz məlumat göndərə bilərsiniz. POST metodu ilə göndərilən məlumatlar HTTP sorğusunun istək hissəsində saxlanıldığı üçün məlumatlar daha etibarlı şəkildə ötürülür. Lakin POST metodu GET metodundan daha yavaşdır.

--serverdən məlumat almaq üçün GET metodundan, serverə məlumat göndərmək üçün POST metodundan istifadə edəcəyik.--

