
// navigation button part

document.getElementById("navbtn_profile").addEventListener("click", noReturn => {
	window.location = "profile.html"; // temporary
});

document.getElementById("navbtn_practice").addEventListener("click", noReturn => {
	window.location = "practice.html"; // temporary
});

document.getElementById("navbtn_signup").addEventListener("click", noReturn => {
	window.location = "signup.html";
});

// check for log in


// sign in
document.getElementById("signin").addEventListener("click", noReturn => {
	let email = document.getElementById("email").value.trim();
	let pass = document.getElementById("pass").value.trim();
	if(email == "" || pass == "") {
		showAlert("Wrong inputs.")
	} else {
		hideAlert();
		// sign in try
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

// forgot password
document.getElementById("forgot_pass").addEventListener("click", noReturn => {
	let email = document.getElementById("email").value.trim();
	if(email == "") showAlert("Email field is necessary.");
	else {
		hideAlert();
		// go for it
	}
});