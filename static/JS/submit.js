

document.getElementById("submit").addEventListener("click", noReturn => {
	let problemID = document.getElementById("problemid").value.trim();
	let language = document.getElementById("language").value;
	let code = document.getElementById("code").value.trim();
	console.log(problemID, language, code);
	if(code == "" || language == "" || problemID == "") {
		document.getElementById("modalactivate").click();
	}
});

function sendCode(problemID, language, code){

}