$(document).ready(() => {
    $("#cifre-button").click(() => {
        let message = $("#cifre-text").val();
        let key = $("#cifre-key").val();
        let resultElement = $("#cifre-result")

        $.ajax({
            type: 'GET',
            url: `cifre/${message}/${key}`,
            success: (data) => {
                $(resultElement).val(data)
            }
        })
    });

    $("#descifre-button").click(() => {
         let message = $("#descifre-text").val();
        let key = $("#descifre-key").val();
        let resultElement = $("#descifre-result")

        $.ajax({
            type: 'GET',
            url: `descifre/${message}/${key}`,
            success: (data) => {
                $(resultElement).val(data)
            }
        })
    })
});