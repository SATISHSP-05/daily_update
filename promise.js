// promise resolve reject 
let promise1 = new Promise((resolve, reject)=>{
    let success = false;
    if(success){
        resolve("seccess");
    } else
    {
        reject("failed");
    }
});
promise.then((msg)=>console.log(msg))
.catch((err)=>console.log(err));

// settimeout

let promise2 = new Promise((resolve, reject)=>{
    console.log("hello");
    setTimeout(()=>{console.log("time set")},2000)
});
promise.then((msg)=>console.log(msg))
.catch((err)=>console.log(err));




// json.js

fetch("https://jsonplaceholder.typicode.com/posts/1")
  .then((response) => response.json())
  .then((data) => { console.log("API Data Received:", data);
  })
  .catch((error) => { console.error(" API Error:", error);
 });

 

// chaining promise
new Promise ((resolve)=>{
    resolve(10);
})
.then((num)=>{
    console.log("number1",num);
    return num+1;
})
.then((num)=>{
    console.log("number2",num);
    return num+1;
})
.then((num)=>{
    console.log("final",num);
    return num;
})





