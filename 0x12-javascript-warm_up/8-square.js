#!/usr/bin/node
arg = process.argv[2];
const x = Number(arg);
if (!arg || isNaN(arg)){
	console.log('Missing size')
} else if (arg >= 1){
	let s = '';
	for (i = 0; i < arg; i++){
		s += 'X';
	}
	for(i = 0; i < x; i++){
		console.log(s);
	}
}
