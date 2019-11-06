
   // It should handle errors for empty strings 
   // or strings which don't represent a decimal number

   // "asdfadsf"
   // "312341234"
   // "1234.1324132"

   // if argument is string decimal representation of a lucky ticket number,
   //  true 
   // else for all other numbers.
   //  false 

function luckCheck(str) {
    
    if (str === "" || /^[A-Za-z]+$/.test(str) ) {
        console.log("Error");  
    } else {
        let strMiddle = str.length / 2;
        let lefthalf = str.slice(0, Math.floor(strMiddle));
        let righthalf = str.slice(Math.ceil(strMiddle));
        console.log(sumAdd(lefthalf) === sumAdd(righthalf));
    }
}   

function sumAdd(str) {
    let n = 0;
    str.split('').forEach(num => {
        n += +num;
    })
    return n;
}

luckCheck("abcdef");
luckCheck('003111')
luckCheck('123321')
luckCheck('123456')