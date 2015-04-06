var Firebase = require("firebase");
var myFirebaseRef = new Firebase("https://whiteboardcoding.firebaseio.com/");

myFirebaseRef.child("Vote").once(value, function(datasnapshot){
	console.log(datasnapshot.value());
})