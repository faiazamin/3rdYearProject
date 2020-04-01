
// navigation button part

document.getElementById("navbtn_profile").addEventListener("click", noReturn => {
	window.location = "profile.html"; // temporary
});

document.getElementById("navbtn_practice").addEventListener("click", noReturn => {
	window.location = "practice.html"; // temporary
});

document.getElementById("navbtn_signout").addEventListener("click", noReturn => {
	// sign out
});

// check for log in


// problem click
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