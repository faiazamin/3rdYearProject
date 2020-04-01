
// navigation button part

document.getElementById("navbtn_profile").addEventListener("click", noReturn => {
	window.location = "profile.html"; // temporary
});

document.getElementById("navbtn_practice").addEventListener("click", noReturn => {
	window.location = "practice.html"; // temporary
});

document.getElementById("navbtn_signin").addEventListener("click", noReturn => {
	window.location = "signin.html"; // temoporary
	console.log("click");
});

// check for log in


// sign up
document.getElementById("signup").addEventListener("click", noReturn => {
	let name = document.getElementById("name").value.trim();
	let email = document.getElementById("email").value.trim();
	let inst = document.getElementById("inst").value.trim();
	let pass = document.getElementById("pass").value.trim();
	let conpass = document.getElementById("conpass").value.trim();
	if(name == "" || email == "" || inst == "" || pass == "" || conpass == ""){
		showAlert("Missing informations.");
	}else if(pass !== conpass){
		showAlert("Wrong password");
	}else {
		hideAlert();
		// sign up
	}
});


function showAlert(text){
	document.getElementById("alert").classList.remove("hide");
	document.getElementById("alerttext").innerHTML = text;
}

function hideAlert(){
	document.getElementById("alert").classList.add("hide");
	document.getElementById("alerttext").innerHTML = "";
}