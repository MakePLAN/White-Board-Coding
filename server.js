var Firebase = require("firebase");
var myFirebaseRef = new Firebase("https://whiteboardcoding.firebaseio.com/Vote");
var fs = require('fs');

myFirebaseRef.on("value", function(datasnapshot){
	var choice1 = datasnapshot.val().Choice;
	fs.writeFile('file.txt', choice1, function(err){
				console.log(choice1 + " was saved!");
	});
});