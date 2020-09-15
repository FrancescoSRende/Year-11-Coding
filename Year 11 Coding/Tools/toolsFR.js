function isEven(a) {

	if (a % 2 == 0) {
		return true;
	}
		return false;
}
	

console.log("")
console.log("isEven")
console.log('Is 0 even?')
console.log(isEven(0))
console.log('Is 15 even?')
console.log(isEven(15))



function missing_char(str, n) {
	var new1 = str.slice(0, n);
	var new2 = str.slice(n+1);
	var new_str = new1 + new2;
	return new_str;
}


console.log("")
console.log("missing_char")
console.log(missing_char('Converge', 3))
console.log(missing_char('metal', 2))



function base2To10(str) {
	var total = 0;
	var i = 0;
	var length = str.length;
	while (i < length) {
		total = total + Number(str.charAt(length - i - 1)) * 2 ** i;

		i = i + 1
		
	}
		
	return total

}
	


console.log("")
console.log('base2To10')
console.log(base2To10('1011'))
console.log(base2To10('111111'))




function sumDigits(a) {
	var total = 0;
	var i = 0;
	var a = String(a);
	while (i < a.length) {
		total = total + Number(a.charAt(i));
		i = i + 1;
	}

	return total

}



console.log("")
console.log('sumDigits')
console.log(sumDigits('45'))
console.log(sumDigits('101'))
console.log(sumDigits('3'))



function scaleElementsA(a, b) {
	var i = 0;
	while (i < b.length) {
		b[i] = b[i] * a;

		i = i + 1;
	}

	return b
}


console.log("")
console.log('scaleElementsA')
console.log(scaleElementsA(2, [1,2,3]))
console.log(scaleElementsA(3, [4,3]))
console.log(scaleElementsA(0, [4,5,6,7]))




function scaleElementsB(a, b) {
	var i = 0;
	var z = [];
	while (i < b.length) {
		z = z.concat(b[i] * a);

		i = i + 1;
	}

	return z
}


console.log("")
console.log('scaleElementsB')
console.log(scaleElementsB(2, [1,2,3]))
console.log(scaleElementsB(3, [4,3]))
console.log(scaleElementsB(0, [4,5,6,7]))



function addStringsSmallLarge(a,b) {

	if (a.length < b.length) {
		return b + a;
	}

	else {
		return a + b;
	}
}

		
console.log('')
console.log('addStringsSmallLarge')
console.log(addStringsSmallLarge('aaa', 'bb'))
console.log(addStringsSmallLarge('aaa', 'bbbb'))
console.log(addStringsSmallLarge('aaa', 'bbb'))