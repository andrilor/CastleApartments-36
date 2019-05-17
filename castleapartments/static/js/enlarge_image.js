// Function-ið til að stækka myndinna, tekur inn id frá myndinni sem er seinni parturinn af url sem argument, - Fannar
function enlarge(val){
    // bý til breytu modal með tilteknu id - Fannar
    var modal = document.getElementById("myModal-"+val);
    //bý til breytu img með tiltekið class nafn- Fannar
    var img = document.getElementsByClassName("eign-uppl-img");
    // bý til breytu modalImg með tilteknu id - Fannar
    var modalImg = document.getElementById('https://i.imgur.com/'+val);
    // Ekki nýtt
    var captionText = document.getElementById("caption");
    //Virkir "block" stílin þegar ýtt er á myndinna - Fannar
    modal.style.display = "block";
    //modalImg.src = this.src; ekki verið að nota - Fannar
    // Aftur ekki verið að nota, þori ekki að taka út á þessum tímapunkti - Fannar
    captionText.innerHTML = this.alt;
}

function shrink(val) {
    // bý til breytu modal með tilteknu id - Fannar
    var modal = document.getElementById("myModal-"+val);
    var span = document.getElementsByClassName("close")[0];
    // Lokar á modal stílinn til að fela stærri myndina
    modal.style.display = "none";
}