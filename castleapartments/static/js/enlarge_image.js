function enlarge(val){
    var modal = document.getElementById("myModal-"+val);
    var img = document.getElementsByClassName("eign-uppl-img");
    var modalImg = document.getElementById('https://i.imgur.com/'+val);
    var captionText = document.getElementById("caption");
    modal.style.display = "block";
    //modalImg.src = this.src;
    captionText.innerHTML = this.alt;
}

function shrink(val) {
    var modal = document.getElementById("myModal-"+val);
    var span = document.getElementsByClassName("close")[0];
    modal.style.display = "none";
}