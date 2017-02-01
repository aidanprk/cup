class Class{
	constuctor(nclass, classcode){
		var classname = nclass;
		var classcode = classcode;
	}
	load(){
		title = getElementById('classtitle');
		title.innerHTML = self.classname;
	}
}

class Student{
	constuctor(name){
		var name = name;
		var problem = false;
	}
	getProblem(){
		problem = document.getElementById('probleminput').value
		self.problem = true;
	}
	loadInTeacher(){
		var cup;
		var studentTitle = "<p class = 'studentTitle' id = "+String(self)+ ">" + String(self) + "</p>";
		var stct = document.createElement('div');
		if(self.problem == false){
			cup = "<img id='upCup' class='cup' src = 'down.jpg' />"
		}
		else{
			cup = "<img id='upCup' class='cup' src = 'up.jpg' />"
		}
		stct.id = String(self);
		stct.innerHTML = cup;
		stct.innerHTML = studentTitle;
	}
}

function createClass(name, code){
	newClass = Class(name, classcode)
}

function loadPage(){
	
}

function newStudent(){
	uname = document.getElementById('unstudent');
	you = Student(uname);
	// Send "you" class to database
}

function newClass(name, code){
	name = document.getElementById('class');
	code = document.getElementById('code');
	nClass = Class(name, code);
}