
// // promise allsettled
// const api1 = fetch("https://jsonplaceholder.typicode.com/users/1")
// .then(res => res.json());
// const api2 = fetch("https://jsonplaceholder.typicode.com/posts/1")
// .then(res => res.json());
// const api3 = fetch("https://jsonplaceholder.typicode.com/comments/1")
// .then(res => res.json());

// Promise.all([api1, api2, api3])
//   .then((results) => {
//     console.log("User:", results[0]);
//     console.log("Post:", results[1]);
//     console.log("Comment:", results[2]);
//   })
//   .catch((error) => {
//     console.log("One of the requests failed:", error);
//   });



// // get perticular portion of the data
// fetch("https://jsonplaceholder.typicode.com/users/1")
//   .then((response) => response.json()) 
//   .then((data) => console.log("username:",data.username))
//   .catch((error) => console.log("Error:", error));



// // use data portions
// fetch("https://jsonplaceholder.typicode.com/users/1")
//   .then((response) => response.json())
//   .then((data) => {
//     const { name, email } = data;          
//     const { city } = data.address;         

//     console.log(`User ${name} lives in ${city} and can be reached at ${email}.`);
//   })
//   .catch((error) => console.log("Error:", error));


// fetch("https://jsonplaceholder.typicode.com/users/1")
//   .then((response) => response.json()) 
//   .then((data) => console.log("userId",data.username))
//   .catch((error) => console.log("Error:", error));



// //  async function
// async function getData() {
//   return "Hello Async!";
// }
// getData().then(result => console.log(result)); 



async function prac() { 
  try {
  let result =await new Promise((resolve,reject)=>{
    setTimeout((msg)=>console.log("trial"),1000)
  });
  console.log(result)
}
catch(err){
  console.log("error",err)
}
}
prac();