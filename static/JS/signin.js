

document.getElementById("signin").addEventListener("click", noReturn => {
	let email = document.getElementById("email").value.trim();
	let pass = document.getElementById("pass").value.trim();
	if(email == "" || pass == "") {
		showAlert("Wrong inputs.")
	} else {
		hideAlert();
		signin(email, pass);
	}
});

document.getElementById("email").addEventListener("keypress", hideAlert);

document.getElementById("pass").addEventListener("keypress", hideAlert);

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
		//forgotPassSuccess();
	}
});

function forgotPassSuccess(){
	document.getElementById("modalactivate").click();
}

function signin(email, pass){
	firebase.auth().signInWithEmailAndPassword(email, pass).then(noReturn => {
		window.location = "practice.html" + extend();
	}).catch(error => {
		showAlert(error.message);
	});
}