let APP = {
    callback_scrivi : function(){
        let op1 = parseInt($("#op1").val());
        let op2 = parseInt($("#op2").val());
        let res = op1 + op2;
        $("#text").text(res);
    },

    callback_scrivi_click : function(){
        $("#btn").on('click', APP.callback_scrivi);
    }
};


$(document).ready(function(){
    APP.callback_scrivi_click();
}
);
