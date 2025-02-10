let APP = {
    answers: [0, 0, 0, 0],
    counter: 0,
    quizScore: 0,
    q: [
        "1. Quale tecnologia di stampa 3D utilizza filamenti di plastica fusi per creare oggetti strato dopo strato?",
        "2. Quale di questi materiali NON è comunemente utilizzato nella stampa 3D FDM?",
        "3. Qual è il principale svantaggio della stampa 3D rispetto alla produzione tradizionale?",
        "4. Quale parametro è più importante per determinare la qualità di stampa in una stampante 3D FDM?",
        "5. Quale di questi problemi può verificarsi se la temperatura dell’estrusore è troppo bassa?",
    ],
    selectedButton: "",
    a: [
        "a) SLA (Stereolitografia)",
        "b) FDM (Fused Deposition Modeling)",
        "C) SLS (Selective Laser Sintering)",
        "D) DLP (Digital Light Processing)",
        "A) PLA",
        "B) ABS",
        "C) Nylon",
        "D) Ceramica",
        "A) Tempi di produzione più lunghi",
        "B) Maggiore difficoltà nella personalizzazione",
        "C) Impossibilità di creare prototipi",
        "D) Costo più elevato rispetto allo stampaggio a iniezione per grandi volumi",
        "A) Velocità di stampa",
        "B) Diametro dell’ugello",
        "C) Altezza dello strato",
        "D) Colore del filamento",
        "A) Sovraestrusione",
        "B) Strati che non aderiscono bene tra loro",
        "C) Filamento che si scioglie troppo velocemente",
        "D) Effetto “stringing” e “oozing” eccessivo"
    ],
    
    start: function(){
        $('.sel').on('click', APP.buttonClick);
    },

    buttonClick: function(e){
        APP.selectedButton = e.target.id;
        let num = parseInt(APP.selectedButton);

        APP.answers[APP.counter] = num;
        APP.counter += 1;
        
        switch(APP.counter){
            case 1:
                document.getElementById("question").innerHTML = APP.q[0]
                document.getElementById("1").innerHTML = APP.a[0]
                document.getElementById("2").innerHTML = APP.a[1]
                document.getElementById("3").innerHTML = APP.a[2]
                document.getElementById("4").innerHTML = APP.a[3]
            break;
            case 2:
                document.getElementById("question").innerHTML = APP.q[1]
                document.getElementById("1").innerHTML = APP.a[4]
                document.getElementById("2").innerHTML = APP.a[5]
                document.getElementById("3").innerHTML = APP.a[6]
                document.getElementById("4").innerHTML = APP.a[7]
            break;
            case 3:
                document.getElementById("question").innerHTML = APP.q[2]
                document.getElementById("1").innerHTML = APP.a[8]
                document.getElementById("2").innerHTML = APP.a[9]
                document.getElementById("3").innerHTML = APP.a[10]
                document.getElementById("4").innerHTML = APP.a[11]
            break;
            case 4:
                document.getElementById("question").innerHTML = APP.q[3]
                document.getElementById("1").innerHTML = APP.a[12]
                document.getElementById("2").innerHTML = APP.a[13]
                document.getElementById("3").innerHTML = APP.a[14]
                document.getElementById("4").innerHTML = APP.a[15]
            break;
            case 5:
                document.getElementById("question").innerHTML = APP.q[4]
                document.getElementById("1").innerHTML = APP.a[16]
                document.getElementById("2").innerHTML = APP.a[17]
                document.getElementById("3").innerHTML = APP.a[18]
                document.getElementById("4").innerHTML = APP.a[19]
            break;
            case 6:
                document.getElementById("question").style.display = "none"; // Hide
                document.getElementById("selection").style.display = "none"; // Show
                document.getElementById("form").style.display = "block"; // Show

            break;
            
        }
        if(APP.counter == 7){
            APP.sendAll();
        }
    },

    sendAll: function(){
        let username = document.getElementById("username").value;
        data = {username: username, answer1: APP.answers[0], answer2: APP.answers[1], answer3: APP.answers[2], answer4: APP.answers[3]};
        fetch("https://16.170.201.57", { 
            method: "POST",
            mode: "cors", // Important!
            headers: {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            body: JSON.stringify(data),
        })
        
        .catch(error => {
            console.error("Error sending POST request:", error);
        });
        console.log("finished sending...");
        APP.thankYou();
    },

    checkScore: function(){
        let score = 0;
        answers[0] == 2 ? score += 1 : score += 0;
        answers[1] == 4 ? score += 1 : score += 0;
        answers[2] == 1 ? score += 1 : score += 0;
        answers[3] == 3 ? score += 1 : score += 0;
        answers[4] == 2 ? score += 1 : score += 0;
	return score
    },

    thankYou: function() {
	window.location.replace("thankyou.html");
    }

};

$(document).ready(function () {
//   document.getElementById("question").style.display = "none";
//    document.getElementById("selection").style.display = "none";
    document.getElementById("form").style.display = "none";
    APP.start();
});
