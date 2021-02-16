//Massivdeki ededlerin cemini tapan kod//
             //1 ci variant

const sum = function (a,b,c,d,e,f,g,h,i,j,k,l){
    var m=a+b+c+d+e+f+g+h+i+j+k+l
    return m;
}
console.log(sum(1,3,4,90,23,890,12,30,4,3,67,21));


         //2 ci variant

var numbers = [1,3,4,90,23,890,12,30,4,3,67,21];
var sum1 = numbers.reduceRight(myFunction);

function myFunction(total, value, index, array) {
    return total + value;
  }
  console.log(sum1);
  
  
//Massivdeki en kicik ededi tapin

var points = [1,3,4,90,23,890,12,30,4,3,67,21] ;

points.sort(function(a,b){
    return a-b
});

console.log(points[0]);

//Massivdeki en boyuk ededi tapin
var points = [1,3,4,90,23,890,12,30,4,3,67,21] ;

points.sort(function(a,b){
    return b-a
});

console.log(points[0]);


//Massivdeki ededleri azalan sira ile ekrana yazdirin

var points = [1,3,4,90,23,890,12,30,4,3,67,21] ;
points.sort(function(a,b){
  return b-a 
 });

console.log(points);










