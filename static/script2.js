function updateChatBox(chat){
    for(var i = 0; i < Object.keys(chat).length; i++){
    if(chat[i][1] == 1){
        var chatRoom = document.getElementById("chat-panel")
        var lapis1 = document.createElement("div");
        lapis1.className += "row no-gutters";
        var lapis2 = document.createElement("div");
        lapis2.className += "col-md-6 offset-md-6 text-right";
        var lapis3 = document.createElement("p");
        lapis3.className += "chat-bubble chat-bubble--right text-left";
        lapis3.innerHTML = chat[i][0];
        // var isi = document.createTextNode(chat[i][0]);
    }
    else{
        var chatRoom = document.getElementById("chat-panel")
        var lapis1 = document.createElement("div");
        lapis1.className += "row no-gutters";
        var lapis2 = document.createElement("div");
        lapis2.className += "col-md-6";
        var lapis3 = document.createElement("div");
        lapis3.className += "chat-bubble chat-bubble--left";
        lapis3.innerHTML = chat[i][0];
        // var isi = document.createTextNode(chat[i][0]);
    }
    console.log(lapis3);
    // lapis3.appendChild(isi);
    lapis2.appendChild(lapis3);
    lapis1.appendChild(lapis2);
    chatRoom.appendChild(lapis1);
    }
}
