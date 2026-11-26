#!/usr/bin/node

const numbers = process.argv.slice(2).map(Number);

numbers.sort((a, b) => a - b);
console.log(numbers.length < 2 ? 0 : numbers[numbers.length - 2]);
