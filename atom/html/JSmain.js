let APP = {
    callback_global: function (a) {
        let op1 = parseInt($("#op1").val());
        let op2 = parseInt($("#op2").val());
        let res;
        switch (a.valueOf()) {
            case 1:
                res = op1 + op2;
                break;
            case 2:
                res = op1 - op2;
                break;
            case 3:
                res = op1 * op2;
                break;
            case 4:
                res = op1 / op2;
                break;
        }
        $("#text").text(res);
    },
    callback_addizione: function () {
        let op1 = parseInt($("#op1").val());
        let op2 = parseInt($("#op2").val());
        let res = op1 + op2;
        $("#text").text(res);
    },
    callback_sottrazione: function () {
        let op1 = parseInt($("#op1").val());
        let op2 = parseInt($("#op2").val());
        let res = op1 - op2;
        $("#text").text(res);
    },
    callback_moltiplicazione: function () {
        let op1 = parseInt($("#op1").val());
        let op2 = parseInt($("#op2").val());
        let res = op1 * op2;
        $("#text").text(res);
    },
    callback_divisione: function () {
        let op1 = parseInt($("#op1").val());
        let op2 = parseInt($("#op2").val());
        let res = op1 / op2;
        $("#text").text(res);
    },

    callback_scrivi_click: function () {
/*
        $("#add").on('click', APP.callback_global(1));
        $("#min").on('click', APP.callback_global(2));
        $("#molt").on('click', APP.callback_global(3));
        $("#div").on('click', APP.callback_global(4));
*/
        $("#add").on('click', APP.callback_addizione);
        $("#min").on('click', APP.callback_sottrazione);
        $("#molt").on('click', APP.callback_moltiplicazione);
        $("#div").on('click', APP.callback_divisione);
    }
};


$(document).ready(function () {
    APP.callback_scrivi_click();
}
);
