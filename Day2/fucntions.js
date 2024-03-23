// Today's content / learning would be : functions. 

/*
let's say-> 
database: correct username-> vishal
I am having a login functionality: 

s1: (username=="vishal")? print("yes"):print("no")   // o/p: yes
s2: (username=="vial")? print("yes"):print("no")     // o/p: no
s3: (username=="vihal")? print("yes"):print("no")   // o/p: no

code-duplicacy; 
solution-> functions(): helps in limiting the code duplicacy
*/ 

/*
syntax: 
function function_name(param1,param2)
{
    body........  (we write the main logic flow)
}
function_name(param1,param2) //calling a function
*/

// taking the login functionality
function loginTest(username, password, expectation)
{
    // loginTest("admin","admin",1)
    const loginSuccess = username === "admin" && password === "admin";  // ternery condition

    if (loginSuccess === expectation)
    {
        console.log("Login is succedded")
    }
    else { 
        console.log("login failed: please provide the correct credentials")
    }

}
loginTest("admin","admin",true) // s1: login succedded
loginTest("admin","invalid_password",0)  // wrong password entered
loginTest("wrong username","admin",0)    // wrong username entered 
loginTest("wrong username","wrong passowrd",0)   // wrong username + password got entered

