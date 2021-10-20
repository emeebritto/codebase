const q = ['0','a','1','b','2','c','3','d','4','e','5','f','6','g','7','h','8','i','9','j','k','l','m','n','o','p','q','r','s','t','u','v','x','w','y','z','<','>','&','%','$','#','*','!','-','+','=']
const password = 'casad'
let map = [0]

let currentPass = ''
let currentPassMap = []

let t1 = new Date()

while (password != currentPass){

	for(let i = 0; i < map.length; i++){

		currentPassMap[i] = q[map[i]]
	}

	currentPass = currentPassMap.join('')
//	console.log(currentPass)
	
	map[0] += 1
	
	while(map.includes(48)){
		let index = map.indexOf(48)

		map[index] = 0

		if(map[index + 1] == undefined) {
			map[index + 1] = 0
		} else {
			map[index + 1] += 1
		}
	}
}

let t2 = new Date()
console.log('TIME: ' + (t2.getTime() - t1.getTime()) + 'ms << ===========================================')
console.log('RESULT: ' + currentPass + ' << ===========================================')