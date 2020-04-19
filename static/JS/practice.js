

var allId = document.getElementsByClassName("problemid");
var allName = document.getElementsByClassName("problemname");
//console.log(all);
for(let i = 0; i < allId.length; i++){
	allId[i].addEventListener("click", noReturn => {
		//console.log(allId[i].innerHTML);
		// do the rest
		gotoproblem(allId[i].innerHTML);
	});
	allName[i].addEventListener("click", haha=>{
		//console.log(allId[i].innerHTML);
		// do the rest
		gotoproblem(allId[i].innerHTML);
	});
}

function gotoproblem(ID){
	window.location = "problem.html/" + ID + extend();
}