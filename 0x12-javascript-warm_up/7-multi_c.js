#!/usr/bin/node
const { argv } = require('process');

const numberLoop = Number(argv[2]);

if (isNaN(numberLoop)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numberLoop; i++) {
    console.log('C is fun');
  }
}
