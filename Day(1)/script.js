/*
Fundamentals of .js ->
1) Variables

*/


/*
Variables: Storing some value in a container. 
(3) Types: let, const, var
<> let,var -> will be storing everything that can change. 
<> const -> constant : you just have to store only the contant values. 
<> Difference b/w var and let: Version, hoisting, scope resolution.
*/
// let Name = "Vishal";
// let age = 20
// console.log(Name) 
// console.log(age) 

// var a = 5
// let b = 10 
// let summumation;

// summumation=a+b
// console.log(summumation)

// const fruit = "apple"
// console.log(fruit)
// const fruit1 = "banana"
// console.log(fruit1)

/*
Operators: (Mathemtatical symbols)
1) + -> ++ (increment)
2) - => -- (decrement) 
3) * => multiplication
4) ** => power => a**b => 5**2 => 25
5) / => division 
6) % => reminder
7) = => equal => double equal -> checking => triple equal => I need to check value + datatype
8) ! => not => != => not equals => a!=b
9) || => or => either 1 condition will execute or another. 
10) && => and => both the conditions should be true
11) ?? => it is simillar to (or) operator but, it will scan the left condition everytime, unless left condition is null or undefined or 0 => called as 'nullish operator'
*/

// NOTE: javascript works left to right.
// Priority: strings > integers / numbers => BODMAS 


// type coercion
/* example : 

let a,b,c;
a=b=c = 3+2;
b+=a*=c-=2;
console.log(a,b,c)
// o/p: b =20


let x = 5  // (0101)
let y=2    // (0010)
x|=y       // bitwise OR -> (0111) -> x=7
y&=x       // bitwise AND -> (0010) -> y=2
console.log(x,y)
// o/p: false

let truthy = "I am truthy"
let falsy = 0
truthy ||= 'Default Value'
falsy &&='Another value'
console.log(truthy,falsy)
//o/p: true

*/


/*
Conditions -> There are (3) styles of writing the conditions: 
(1) if-else
(2) ternery operators: converting if-else into a single line. 
Syntax: Condition ? true Value : False Value 
(3) Switch case stmt.
*/
let a="apple"
if (a=="apple"){
    console.log("Yes it's a fruit")
}
else{ 
    console.log("No it's not a fruit")
}
// Converting above if-else into a ternery operator.
(a=="apple")?console.log("Yes it's a fruit"):console.log("No it's not a fruit");

/*
Loops -> are used for reducing the code duplicacy. 
In .js there are (3) loops: 
-> For 
-> While 
-> Do-While
*/
let number=4
while (number>5)
{
    console.log(number)
    number-=2
}
console.log("------")

let numberr=4
do
{
    console.log(numberr)
    numberr-=2
}
while(numberr>5)
console.log("------")
 
for(let n=10; n>5; n-=2)
{
    console.log(n)
}
// 'for of' loop && 'for each' loop

/*
Keywords: break -> whenver the code stmt reaches break the whole code will get terminated there.

, continue -> when pointer reaches continue, only that line of code get skipped.
*/

/*
JavaScript Interactions:
<All (3) are the pop-ups || window-elements> 
alert -> it will just display the msg || there's not cancel button.
prompt -> allows us to write anything.
confirm -> yes or no

String datatypes: backticks 
Syntax: `` => allows to fetch the value from the variable.
*/

// alert("Are you getting exhuasated")
// confirm("Are you getting exhuasated")
// prompt("Enter your name")

let Name = prompt ("enter your name")
alert(`Hope  ${Name} you're understanding and enjoying javascript`)

//Try it: Create a web-page that asks your age and if you're age > 18, you're eligible to vote, otherwise not. 









