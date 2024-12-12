let APP = {
    ordGiusto: ["1", "2", "3", "4", "5", "6", "7", "8", "n"],
    ordCorrente: ["1", "2", "3", "4", "5", "6", "7", "n", "8"],
    start: function(e){
        $("button").on('click', APP.sposta)
    },

    sposta: function(e){
        let numClickato = $(e.target);
        let pos = APP.ordCorrente.indexOf(numClickato.text());
    
        if (pos !== -1 && APP.ordCorrente[pos + 1] === "n" && (pos + 1) % 3 !== 0) {
            APP.ordCorrente[pos + 1] = APP.ordCorrente[pos];
            APP.ordCorrente[pos] = "n";
            APP.set();
        } else if (pos !== -1 && APP.ordCorrente[pos - 1] === "n" && pos % 3 !== 0) {
            APP.ordCorrente[pos - 1] = APP.ordCorrente[pos];
            APP.ordCorrente[pos] = "n";
            APP.set();
        } else if (pos !== -1 && APP.ordCorrente[pos + 3] === "n") {
            APP.ordCorrente[pos + 3] = APP.ordCorrente[pos];
            APP.ordCorrente[pos] = "n";
            APP.set();
        } else if (pos !== -1 && APP.ordCorrente[pos - 3] === "n") {
            APP.ordCorrente[pos - 3] = APP.ordCorrente[pos];
            APP.ordCorrente[pos] = "n";
            APP.set();
        } else {
            console.log("non puoi spostarlo");
        }
        APP.checkWin();
    },

    set: function(){
        $("#1").text(APP.ordCorrente[0]);
        $("#1").val(APP.ordCorrente[0]);
        $("#2").text(APP.ordCorrente[1]);
        $("#2").val(APP.ordCorrente[1]);
        $("#3").text(APP.ordCorrente[2]);
        $("#3").val(APP.ordCorrente[2]);
        $("#4").text(APP.ordCorrente[3]);
        $("#4").val(APP.ordCorrente[3]);
        $("#5").text(APP.ordCorrente[4]);
        $("#5").val(APP.ordCorrente[4]);
        $("#6").text(APP.ordCorrente[5]);
        $("#6").val(APP.ordCorrente[5]);
        $("#7").text(APP.ordCorrente[6]);
        $("#7").val(APP.ordCorrente[6]);
        $("#8").text(APP.ordCorrente[7]);
        $("#8").val(APP.ordCorrente[7]);
        $("#9").text(APP.ordCorrente[8]);
        $("#9").val(APP.ordCorrente[8]);
    },

    checkWin: function(){
        if (APP.ordCorrente.join("") === APP.ordGiusto.join("")) {
            alert("Hai vinto!");
        }
    }

}


$(document).ready(function () {
    APP.start();
    APP.set();
}
);
