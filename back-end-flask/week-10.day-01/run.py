from flask import Flask,render_template

app=Flask(__name__)
Data=[
    {
        'title':'Azərbaycanlı döyüşçü iddialı danışdı: “Rəqibimin birinci raundda nəfəsini kəsəcəyəm” - FOTO',
         'content':"""Azərbaycanlı MMA döyüşçüsü Əli Quliyev “Brave CF 47” döyüş gecəsində hindistanlı Rana Rudra ilə qarşılaşacaq.

Oxu.Az xəbər verir ki, keçirdiyi beş görüşdə məğlub olmayan Əli asiyalı rəqibi barədə danışıb. O, 11 döyüşdə məğlubedilməz olan rəqibini tanımadığını və bu turnirdə əsas hədəfinin İngiltərəni təmsil edən digər məğlubedilməz 20 yaşlı superulduz Məhəmməd Mokayevlə qarşılaşmaq olduğunu bildirib:""",
        'img':'../static/img/img-2.jpg'
        
    },
     {
        'title':'Dövlət Sığorta Şirkəti həlak olmuş və yaralanmış hərbçilərə ödənilən vəsaitlərin həcmini AÇIQLADI',
        'content':"""Dövlət Sığorta Kommersiya Şirkəti (“Azərsığorta”) 44 günlük Vətən Müharibəsində həlak olmuş və yaralanmış hərbçilərə ödənilən vəsaitlərin həcmini açıqlayıb. 

Dövlət Sığorta Şirkətinin marketinq və ictimaiyyətlə əlaqələr şöbəsindən verilən məlumata görə, ötən ilin sentyabr ayının 27-dən noyabr ayının 10-dək Qarabağda aparılan əks-hücum əməliyyatları (Vətən Müharibəsi) zamanı həlak olmuş və yaralanmış hərbçilərə görə 40 milyon manatdan artıq ödəniş edilib. :"""
    },
     {
        'title':'First card title',
        'content':'First card content'
    },
]
@app.route('/')
def index():
    return render_template('index.html',melumatlar=Data)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__=='__main__':
    app.run(debug=True)   