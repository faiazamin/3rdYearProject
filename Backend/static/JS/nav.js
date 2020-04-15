/*
	Stores all navigation activities.
	also other pages activites too which requires small and independent code
*/

let nav_logo = document.getElementById("logo");
let nav_practice = document.getElementById("navbtn_practice");
let nav_profile = document.getElementById("navbtn_profile");
let nav_signin = document.getElementById("navbtn_signin");
let nav_signup = document.getElementById("navbtn_signup");
let nav_signout = document.getElementById("navbtn_signout");
let home_signin = document.getElementById("navbtn_signin2");
let home_signup = document.getElementById("navbtn_signup2");
let problem_submit = document.getElementById("problem_submit");

if(nav_logo !== null){
	nav_logo.addEventListener("click", noReturn => {
		window.location = "/";
	});
}

if(nav_practice !== null){
	nav_practice.addEventListener("click", noReturn => {
		window.location = "/practice"  ;
	});
}

if(nav_profile !== null){
	nav_profile.addEventListener("click", noReturn => {
		window.location = "/profile" ;
	});
}

if(nav_signin !== null){
	nav_signin.addEventListener("click", noReturn => {
		window.location = "/signin"  ;
	});
}

if(nav_signout !== null){
	nav_signout.addEventListener("click", noReturn => {
		signOut();
		window.location = "/index"  ;
	});
}

if(nav_signup !== null){
	nav_signup.addEventListener("click", noReturn => {
		window.location = "/signup"  ;
	});
}

if(home_signin !== null){
	home_signin.addEventListener("click", noReturn => {
		window.location = "/signin"  ;
	});
}


if(home_signup !== null){
	home_signup.addEventListener("click", noReturn => {
		window.location = "/signup"  ;
	});
}

if(problem_submit !== null){
	problem_submit.addEventListener("click", noReturn => {
		window.location = "/submit"  ;
	});
}