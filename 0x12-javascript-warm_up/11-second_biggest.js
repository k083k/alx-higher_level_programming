#!/usr/bin/node
const { argv } = require('process');

if (argv.length <= 3) {
  console.log(0);
} else {
  const numbers = [];
  for (let i = 2; i < argv.length; i++) {
    numbers.push(Number(argv[i]));
  }
  let largest = numbers[0];
  let secondLargest = numbers[1];
  for (let i = 0; i < numbers.length; i++) {
    if (numbers[i] > largest) {
      secondLargest = largest;
      largest = numbers[i];
    } else if (numbers[i] < largest && numbers[i] > secondLargest) {
      secondLargest = numbers[i];
    }
  }
  console.log(secondLargest);
}
