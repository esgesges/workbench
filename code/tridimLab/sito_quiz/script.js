let APP = {
    answer1 : 0, answer2 : 0, answer3 : 0, answer4 : 0, answer5 : 0, answer6 : 0, answer7 : 0, answer8 : 0,
    start: function(e){
        $('.sel').on('click', APP.sposta);
        $('#send').on('click', APP.invia);
    },
    sposta: function(e){

        console.log(e.target.id);
        switch(e.target.id){
            case "sel1":
                if($('#ans1').is(':checked')){
                    APP.answer1 = 1;
                }
                if($('#ans2').is(':checked')){
                    APP.answer1 = 2;
                }
                if($('#ans3').is(':checked')){
                    APP.answer1 = 3;
                }
                console.log(APP.answer1)
            $('#change').text("");
            $('#opt1').text("");
            $('#opt2').text("");
            $('#opt3').text("");
            break;
        }
    },
    invia: function(e){
        if(APP.answer8 == 0){
            if($('#ans1').is(':checked')){
                APP.answer8 = 1;
            }
            if($('#ans2').is(':checked')){
                APP.answer8 = 2;
            }
            if($('#ans3').is(':checked')){
                APP.answer8 = 3;
            }
        }
        let username = "";
        do {
            username = prompt("Inserisci il tuo nome");
        } while(username == "");
        if (confirm("Do you want to send all the answers?")) {
            console.log("started sending...");
            data = { username : username, answer1: APP.answer1, answer2: APP.answer2, answer3: APP.answer3, answer4: APP.answer4, answer5: APP.answer5, answer6: APP.answer6, answer7: APP.answer7, answer8: APP.answer8 };
    
<<<<<<< HEAD
            fetch("http://13.61.9.50:8080", {
=======
            fetch("http://localhost:8000", {
>>>>>>> c58b4a150c753bd009155cfb6f16dae6411333bd
                method: "POST", // Use the POST method
                headers: {
                    "Content-Type": "application/json", // Specify JSON content
                },
                body: JSON.stringify(data), // Convert the data to a JSON string
            })
            .catch(error => {
                console.error("Error sending POST request:", error);
            });
            console.log("finished sending...");
        }
    },
}
$(document).ready(function () {
    APP.start();
}
);