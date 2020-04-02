

document.getElementById("submission").addEventListener("click", noReturn => {
	window.location = "submission.html";
	console.log("submission");
});


document.getElementById("changepass").addEventListener("click", noReturn => {
	document.getElementById("modalactivate").click();
	console.log("change pass");
});