// const, let, var  -> variables 

/* 
1. fucntion variables -> (local), (global)
    local -> variables that are defined inside the function and, it will be accessible only inside the function || gets stored in stack memory

2. global -> variables that are defiend outside the function || stored in heap memory || theese are accessible outside the functions.

3. Function Parameters -> the function definations
 and arguments -> function values.

4. return stmt 

5. storing function inside a variable. -> that variable is capable of performing all the operations that a calling function can do. 
*/

/* e.g. -> 
    global -> teacher
    local -> student 
*/

/*
const n1 = "The addition of two numbers is this: "
function addition(a,b)
{
    let n1=5  
    let n2=6
    let n3=n1+n2
    console.log(n3)

    console.log(n1)
    
}
console.log(n1)
*/
// n1 -> The addition of two numbers is this: || 5
// console.log(n)
// addition(5,6)


// addition(a=5,b=6)

//  local variables :
/*
 function checkProductDetails(expectedName, expectedPrice)
 {
    let productName="Apsara pencil"
    let productPrice=20

    let testPassed = productName === expectedName && productPrice === expectedPrice

    if(testPassed)
    {
        console.log("Product details are correct")
    }
    
    else{
        
        return ("Product details aren't correct, please check the backend!")
        
    }
 }
 checkProductDetails("Apsara pencil",20) // positive test case 
 checkProductDetails("Awesome pencil",25) //negative test case 
*/
 

 /*
function productDetails(prodName, prodPrice)
{
    console.log(`My selected product is ${prodName} and its price is ${prodPrice}`)
}
productDetails(prodName="pen", prodPrice=50)
console.log("--------")

// If you don't define any parameter while calling the function, .js automatically declare that undefined.
productDetails(5)
 //defining single parameter || o/p -> prodName = pencil and prodPrice = undefined

productDetails() // defininig no parameters || prodName = undefined = prodPrice

*/

// This thing can only be possible inside the .js -> naming a function. 

function checkingUsernameOfLoginProcess(expectedUsername)
{
    let correctUsername = "admin"

    if(correctUsername === expectedUsername){
        console.log("correct")
    }
    else{
    console.log("Not correct") }
}
const loginUsername=checkingUsernameOfLoginProcess;
loginUsername("admin")
loginUsername("hello")