
var firebaseConfig = {
  apiKey: "AIzaSyCdWCZC5gJghoFhkiIH_r3c7q8lr42N28w",
  authDomain: "rojroj-c8a0d.firebaseapp.com",
  databaseURL: "https://rojroj-c8a0d.firebaseio.com",
  projectId: "rojroj-c8a0d",
  storageBucket: "rojroj-c8a0d.appspot.com",
  messagingSenderId: "471314074654",
  appId: "1:471314074654:web:6bc17fb10c6fdb948a320f"
};
firebase.initializeApp(firebaseConfig);

firebase.auth().onAuthStateChanged(function(user) {
  if (user) {
    if(user.emailVerified) {
      firebase.database().ref('user/' + user.uid).once('value').then(function(snapshot) {
        document.getElementById("navbtn_profile").innerHTML =  snapshot.val().name;
      }).catch(error => console.log("error", error.message));
    } else{
      signOut();
    }
  } else {
    //... 
  }
});

function signOut(){
  firebase.auth().signOut();
}

function isSignedIn(){
  let now = firebase.auth().currentUser;
  if(now === null) return null;
  if(!now.emailVerified) return null;
  return now.uid;
}