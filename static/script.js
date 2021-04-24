var userChat = '{{userChat|tojson}}';
userChat = JSON.parse(userChat);
var botChat = '{{botChat|tojson}}';
botChat = JSON.parse(botChat);

for(var i = 0; i < Object.keys(userChat).length; i++){
  var chatRoom = document.getElementById("chat-panel")
  var lapis1 = document.createElement("div");
  lapis1.className += "row no-gutters";
  var lapis2 = document.createElement("div");
  lapis2.className += "col-md-3 offset-md-9";
  var lapis3 = document.createElement("div");
  lapis3.className += "chat-bubble chat-bubble--right";
  var isi = document.createTextNode(userChat[i]);
  console.log(userChat[i])
  // console.log(isi);
  // console.log(lapis3);
  lapis3.appendChild(isi);
  lapis2.appendChild(lapis3);
  lapis1.appendChild(lapis2);
  chatRoom.appendChild(lapis1);
}
for(var i = 0; i < Object.keys(botChat).length; i++){
  var chatRoom = document.getElementById("chat-panel")
  var lapis1 = document.createElement("div");
  lapis1.className += "row no-gutters";
  var lapis2 = document.createElement("div");
  lapis2.className += "col-md-3";
  var lapis3 = document.createElement("div");
  lapis3.className += "chat-bubble chat-bubble--left";
  var isi = document.createTextNode(botChat[i]);
  console.log(botChat[i])
  lapis3.appendChild(isi);
  lapis2.appendChild(lapis3);
  lapis1.appendChild(lapis2);
  chatRoom.appendChild(lapis1);
}