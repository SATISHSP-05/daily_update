

//write text 
fs.writeFileSync("notes.txt", "JavaScript Practice\n");
fs.appendFileSync("notes.txt", "This file using Node.js\n");
fs.appendFileSync("notes.txt", " files easily.\n");


// Read show content
const data = fs.readFileSync("notes.txt", "utf8");
console.log("Current File Content:\n", data);

// more lines
fs.appendFileSync("notes.txt", "Now adding \n");
fs.appendFileSync("notes.txt", "Learning fs module is simple\n");

// Read again 
const updated = fs.readFileSync("notes.txt", "utf8");
console.log("\n Updated File Content:\n", updated);

// Overwrite
fs.writeFileSync("notes.txt", "File has been reset with new content.\n");

// Check after overwrite
const afterReset = fs.readFileSync("notes.txt", "utf8");
console.log("\nAfter Reset:\n", afterReset);

// Finally, delete the file
fs.unlinkSync("notes.txt");
console.log("\n File deleted successfully");
