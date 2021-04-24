function updateChatBox(chat){
    for(var i = 0; i < Object.keys(chat).length; i++){
    if(chat[i][1] == 1){
        var chatRoom = document.getElementById("chat-panel")
        var lapis1 = document.createElement("div");
        lapis1.className += "row no-gutters";
        var lapis2 = document.createElement("div");
        lapis2.className += "col-md-3 offset-md-9";
        var lapis3 = document.createElement("div");
        lapis3.className += "chat-bubble chat-bubble--right";
        var isi = document.createTextNode(chat[i][0]);
    }
    else{
        var chatRoom = document.getElementById("chat-panel")
        var lapis1 = document.createElement("div");
        lapis1.className += "row no-gutters";
        var lapis2 = document.createElement("div");
        lapis2.className += "col-md-3";
        var lapis3 = document.createElement("div");
        lapis3.className += "chat-bubble chat-bubble--left";
        var isi = document.createTextNode(chat[i][0]);
    }
    lapis3.appendChild(isi);
    lapis2.appendChild(lapis3);
    lapis1.appendChild(lapis2);
    chatRoom.appendChild(lapis1);
    }
}
