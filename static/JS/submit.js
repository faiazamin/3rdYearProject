

document.getElementById("submit").addEventListener("click", noReturn => {
	let problemID = document.getElementById("problemid").value.trim();
	let language = document.getElementById("language").value;
	let code = document.getElementById("code").value.trim();
	if(code == "" || language == "" || problemID == "") {
		document.getElementById("modalactivate").click();
	} else{
		sendCode(problemID, language, code);
	}
});

function sendCode(problemID, language, code){
	data = {
		problemid: problemID,
		language: language,
		code: code
	}
  $.post("/submit", data, response => {
  	if(response.Result == "success") {
		  //window.location = response.Location;
		  console.log(response);
  	}
  	else {
  		alert("Failed");
  	}
  });
}