function isEven(a) {

	if (a % 2 == 0) {
		return true;
	}
		return false;
}
	

console.log('Is 0 even?')
console.log(isEven(0))
console.log('Is 15 even?')
console.log(isEven(15))


function missing_char(str, n) {

  return str[0:n] + str[n+1:len(str)]

}

print(missing_char('Converge', 3))
print(missing_char('metal', 2))