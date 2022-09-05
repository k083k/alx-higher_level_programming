#!/usr/bin/node
arg1 = process.argv[2];
arg2 = process.argv[3];

if (isNaN(arg1) || isNaN(arg2) || !arg1 || !arg2){
	console.log('NaN')
}else{
	answer = Number(arg1) + Number(arg2)
	console.log(answer);
}

