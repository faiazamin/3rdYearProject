

var allId = document.getElementsByClassName("problemid");
var allName = document.getElementsByClassName("problemname");
//console.log(all);
for(let i = 0; i < allId.length; i++){
	allId[i].addEventListener("click", noReturn => {
		console.log(allId[i].innerHTML);
		// do the rest
	});
	allName[i].addEventListener("click", haha=>{
		console.log(allId[i].innerHTML);
		// do the rest
	});
}