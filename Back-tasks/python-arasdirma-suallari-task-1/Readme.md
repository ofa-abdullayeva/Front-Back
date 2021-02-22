Python araşdırma sualları

-1-Python interpreted bir dildir. İnterpreted dilin iş prinsipini izah edin

   -yüksek seviyeli programlama dili ile yazılmış bir programı adım-adım masin diline çeviren ve masin dilindeki talimatları Iwe salan programdır.
   

-2-Interpreted və compiler dillər arasında olan fərqləri izah edin

   -1-compiler Butun proqrami oxuyur sonra onu butovlukde icra edir,interpreter ise addim adim oxuyur ve icra edir
   -2-Compiler adeten menbe kodu teyin etmek ucun cox vaxt aparir,amma umumi icra muddeti interpretere nisbeten daha suretlidir
   -3-compiler dillerde adim adim oxuyur her hansi setirde sehv varsa onu gosterir,interpreterlerde sehv olarsa kodlari oxumayacaq


-3-Python data tipləri hansılardır? Hər biri haqqında qısa izahat verin

   -1-Number 
     --"Int" -tam eded
     --"float" -heqiqi eded
     --"complex" -murekkeb ededler
   -2-String
     --yazi tipi
   -3-list
      -Siyahılar birdən çox maddəni bir dəyişəndə ​​saxlamaq üçün istifadə olunur.
      -Siyahılar dördbucaqlı mötərizədən istifadə edərək yaradılır:
   -4-Turple
      -Tuples birdən çox maddəni bir dəyişəndə ​​saxlamaq üçün istifadə olunur.
      -Tupllar dairəvi mötərizələrlə yazılmışdır.
   -5-Set
      -setlər birdən çox elementi tək dəyişəndə ​​saxlamaq üçün istifadə olunur.
      -setlər qıvrım mötərizələrlə yazılır.
   -6-Dictionary
     -Dictionary məlumat dəyərlərini key: value cütlərində saxlamaq üçün istifadə olunur.
     -Lüğətlər qıvrım mötərizələrlə yazılmışdır və açarları və dəyərləri var:

-4-Object Oriented Programming nədir? Niyə belə bir paradigmanın var olduğunu izah edin
    -Gündəlik həyatda bir kompüterlə problemi həll etmək və gündəlik işləri asanlaşdırmaq üçün yazılmış bir proqramdır. Başqa sözlə, kompüterin bir funksiyanı yerinə yetirməsi üçün hazırlanmış əmrlər zənciridir.
    -Obyekt Odaklı Proqramlaşdırmada 4 əsas xüsusiyyət mövcuddur. Bu 4 xüsusiyyətdən birini təmin etməyən bir proqramlaşdırma dili obyekt yönümlü bir proqramlaşdırma dili hesab edilmir.
       -1. Abstraksiya
          -Abstraksiya: Sinifdəki davranışı və xüsusiyyətlərini təsvir etmək üçün abstraksiya deyirik.
          -Məsələn, avtomobil sinfində onun rəngi, modeli, təkər sayı, mühərrikin gücü, xüsusiyyətləri. Sürətlənmə, əyləc, dayanma davranışlardır və metodlarla təyin olunur.
       -2. Kapsula
           -kapsülasiya: Davranış və xüsusiyyətlər sinifdə mücərrədləşdirilir və əhatə olunur. kapsulyasiya ilə, hansı xüsusiyyətlərin və davranışların xaricə təqdim ediləcəyini və ya verilməyəcəyini təyin edirik.
           -Məsələn, İnsan sinfindəki yemək vərdişləri bizi maraqlandırmırsa, onu özəlləşdiririk və gizlədirik. Ancaq ad və soyad kimi məlumatlar bizə aid olduğundan açıq qalırlar. Bu hadisəyə məlumat saxlama, yəni kapsülləmə deyilir. İnformasiya saxlama giriş əlamətləri ilə həyata keçirilir (ümumi, xüsusi, qorunan).
             -ümumi: hər kəsin istifadə edə biləcəyi xüsusiyyətlər və davranışlar
             -Şəxsi(xüsusi): yalnız öz siniflərində istifadə edilə bilən xüsusiyyətlər və davranışlar
             -qorunan: sinif daxilində və miras alt siniflərdə istifadə olunur.
       -3. Miras
         -Dərslər bir-birindən qaynaqlana bilər. Alt sinif ana sinifin xüsusiyyətlərini ala bilər.
         -Məsələn, təkər nömrəsi, sürət ... kimi xüsusiyyətlərin yenidən yazılması əvəzinə avtomobil və velosiped siniflərində ortaq xüsusiyyətlər olaraq, bu xüsusiyyətləri özündə cəmləşdirən bir sinif yarada və miras ala bilərik. Bir sinifdən birdən çox  miras qalırsa, buna çoxlu miras deyilir.
       -4. Polimorfizm
          -Polimorfizm: Alt siniflərin yuxarı təbəqənin davranışını göstərmək məcburiyyətində deyil. Alt siniflərin fərqli davranışlarına Polimorfizm deyilir.
          -Məsələn, gəmi və avtomobil siniflərini nəzərdən keçirdiyimiz zaman hərəkət növləri olur. Gəmi su üzərində hərəkət edərkən, avtomobil quruda hərəkət edir. Bir sözlə, fərqli obyektlər (maşın və gəmi kimi) eyni hadisəyə (hərəkət növü) fərqli cavab verir.

-5-Proqram yazarkən metodlardan istifadə edirik. Hansı hallarda metod istifadə edilməlidir?

-6-local və global variable nədir izah edin
   -variable
     -Dəyişən, proqramın idarə edə biləcəyi bir saxlama sahəsinə verilən bir addır. Dəyişən tipi dəyişənin yaddaşının ölçüsünü və tərtibini təyin edir.

   -Lokal Dəyişən, proqramlaşdırma bloku və ya alt proqramlar daxilində elan olunan bir dəyişən növü kimi müəyyən edilir. Yalnız elan olunduğu alt proqramın və ya kod blokunun içərisində istifadə edilə bilər. Lokal dəyişən funksiyanın bloku icra olunana qədər mövcuddur. Bundan sonra məhv olacaq

   -  Qlobal Dəyişən,Proqramdakı bir Qlobal Dəyişən, alt proqramın və ya funksiyanın xaricində müəyyən edilmiş bir dəyişəndir. Qlobal bir əhatə dairəsinə malikdir, proqramın ömrü boyu dəyərini saxlayır. Beləliklə, kölgə salmadığı təqdirdə, proqram daxilində müəyyən edilmiş hər hansı bir funksiya ilə proqram boyunca əldə edilə bilər.

-7-Python type conversion haqqında izahat verin
  -Bir məlumat növünün Dəyərinin başqa bir məlumat növünə çevrilməsi prosesinə tip konversiyası deyilir. Pythonda iki növ tip dönüşüm var.
    -Qapalı Tip Çevirmə
      -Qapalı tip dönüşümdə, Python avtomatik olaraq bir məlumat növünü başqa bir məlumat növünə çevirir. Bu proses hər hansı bir istifadəçi iştirakına ehtiyac duymur.
    -Açıq Tip Dönüşüm
      -Açıq Tip Konversiyasında istifadəçilər bir obyektin məlumat növünü tələb olunan məlumat tipinə çevirirlər. Əvvəlcədən təyin edilmiş int(), float (), str () və s. Kimi funksiyaları açıq tipli konvertasiya etmək üçün istifadə edirik.
-8-init nədir?
   -__İnit__ metodu başlatma demekdir. __init__, OOP ilə proqramlaşdırmada bir sinifin  konstruktor metodudur. Bir sinifdən bir obyekt əldə etmək istəyiriksə, __init__ sinifin ilk metodu olmalıdır. Sinifdən alınan obyektlərin xüsusiyyətləri bu metodla obyektlərə verilir.

-9-self nədir?
   -__İnit__ metodunun quruluşuna baxdığımızda mötərizədəki mənlik anlayışı diqqətimizi çəkir. Self açar söz, __init__ metodu ilə gələn və sinifdən əldə etdiyimiz obyektlərə daxil olmağımızı təmin edən bir anlayışdır.

-10-*args,*kwargs nədir? nə zaman istifadə olunur?

-11-Python module nədir?
    -Modullar bəzi funksiyaları asanlıqla yerinə yetirməyimizə imkan verən müəyyən funksiyaları və atributları ehtiva edən vasitələrdir.
       -Ne ucun istifade olunur?
           -Daha az kod yazmaq üçün
           -Yazdığımız kodlardan dəfələrlə istifadə edə bilmək üçün,
           -Daha mütəşəkkil, daha mütəşəkkil bir şəkildə işləyə bilərik.

-12-Python package nədir?

-13-pass nədir? Nə zaman istifadə olunur?
  -Pass funcsiya bosdursa  funcsiyanin icine yazilir,Yazilmadigi halda error verir

-14-List metodlarından 5 ədəd metodun izahatını yazın
  -1-append()
     -Siyahının sonuna bir element əlavə edir
  -2-count()
     -Göstərilən dəyərə malik element sayını qaytarır
  -3-extend()
     -Cari siyahının sonuna bir siyahının elementlərini (və ya hər hansı bir təkrarlana bilən) əlavə edin
  -4-insert()
     -Müəyyən edilmiş vəziyyətdə bir element əlavə edir
  -5-reverse()
     -Siyahının sırasını dəyişdirir


-15-List və dict hansı hallarda istifadə olunur?

-16-Dict metodlarından 5 ədəd metodun izahatını yazın
  -1-clear() 
     -Bütün elementləri lüğətdən çıxarır
  -2-update()
     -lugeti yenileyir
  -3-values()
     -Lüğətdəki bütün dəyərlərin siyahısını qaytarır
  -4-items()
     -Hər bir əsas dəyər cütü üçün cədvəl olan siyahını qaytarır
  -5-pop()
     -Müəyyən edilmiş düymə ilə elementi silir

