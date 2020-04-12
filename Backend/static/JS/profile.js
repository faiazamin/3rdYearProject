
let interval = setInterval(function(){ getData }, 1000);

function getData(){
	if(firebase.auth().currentUser === null) return;
	firebase.database().ref('user/' + firebase.auth().currentUser.uid).once('value').then(function(snapshot) {
	  document.getElementById("name").innerHTML =  snapshot.val().name;
	  document.getElementById("email").innerHTML =  snapshot.val().email;
	  document.getElementById("inst").innerHTML =  snapshot.val().instritution;
	  clearInterval(interval);
	}).catch(error => {
		console.log("error", error.message);
		clearInterval(interval);
	});
}


firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    if(user.emailVerified) {
    	getData();
    } else{
      signOut();
    }
  }
});

document.getElementById("submission").addEventListener("click", noReturn => {
	window.location = "submission.html";
	console.log("submission");
});


document.getElementById("changepass").addEventListener("click", noReturn => {
	document.getElementById("modalactivate").click();
	console.log("change pass");
});

$("#magic").show(3000, noReturn => {
	$(".gupon").fadeIn(1000);
});


