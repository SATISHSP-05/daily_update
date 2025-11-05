
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



// use data portions
fetch("https://jsonplaceholder.typicode.com/users/1")
  .then((response) => response.json())
  .then((data) => {
    const { name, email } = data;          // destructuring
    const { city } = data.address;         // nested destructuring

    console.log(`User ${name} lives in ${city} and can be reached at ${email}.`);
  })
  .catch((error) => console.log("Error:", error));

