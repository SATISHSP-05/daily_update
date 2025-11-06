// try_catch
async function pro() {
  try {
    let result = await new Promise((resolve, reject) => {
      setTimeout(() => reject("rejected"), 3000);
    });
    console.log(result);
  } catch (error) {
    console.log("network error:", error);
  }
}

pro();

// await
async function wait() {
  console.log("Wait");
  let promise = new Promise(resolve => setTimeout(() => resolve("Done"), 2000));
  
  let result = await promise;
  console.log(result);
}
wait();

// parallel
async function parallel() {
const p1 = new Promise(res => setTimeout(() => res("Task 1 done"), 1000));
const p2 = new Promise(res => setTimeout(() => res("Task 2 done"), 1000));
const results = await Promise.all([p1, p2]);
console.log(results);
}
parallel();


// values
async function addNumbers(a, b) {
  return a + b;
}
async function main() {
  let result = await addNumbers(10, 20);
  console.log("Sum:", result);
}
main();




// along with github practice..
