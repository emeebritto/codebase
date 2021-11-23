document.addEventListener('keydown', function(){
	if (event.key == 'Enter'){createMsg();}
})

function createMsg(){
	let tagText = document.createElement("p");
	const newMsg = document.createTextNode(`${document.getElementById('input_DM').value}`);
	tagText.appendChild(newMsg);
	document.querySelector('.container').appendChild(tagText);
	document.getElementById('input_DM').value = '';
}

/*
{'hello': {'Hello', 'comprimento'}}
{'Hi': {'Hi', 'comprimento'}}
comprimentos = {'Hello', 'Hi'}
{'everything_well?': {'everything_well?', 'askAbout': {'MoodStates'}}}
moodStates = {'happy', 'bad'}
*/
/* // create a new div element
  const newDiv = document.createElement("div");

  // and give it some content
  const newContent = document.createTextNode("Hi there and greetings!");

  // add the text node to the newly created div
  newDiv.appendChild(newContent);*/


class Nexa  = {
	constructor(){
		this.name = 'Nexa'
		this.age = 19
		this.mood = 'happy'
		this.levelMood = [happy, soso, bad]
		this.listening = true;

		this.lastResponse = null
		this.sequencePhase =[]
	}

	updateMood(level){
		this.mood = this.levelMood[level]
	}

	listen(phase){
		this.listening = true
		this.sequencePhase.push(phase)
	}

	reason(){

	}

	speak(){
		this.listening = false
		return this.reason()
	}
}

export default IA = new Nexa()



const response = () => {
	*.STATES.PHASEINPUT.RESPONSE
	updateMood()
}

{
	STATES {
		PHASEINPUT {
			RESPONSE
		}
		HI {},
		HELLO {}		
	},
	HAPPY {},
	ANXIERY {},
	SOSO {},
	CONCERT {}
}
