#!/usr/bin/node
if (!process.argv[2]){
	console.log('Missing number of occurences');
} else if (process.argv[2] >= 1) {
	for (i = 0; i < process.argv[2]; i++){
		console.log('C is fun');
	}
}
