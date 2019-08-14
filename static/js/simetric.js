$(document).ready(() => {
    $("#simetric-c-button").click(() => {
        let message = $("#simetric-c-text").val();
        let key = $("#simetric-c-key").val();
        let resultElement = $("#simetric-c-result")

        $.ajax({
            type: 'GET',
            url: `simetric_encrypt/${message}/${key}`,
            success: (data) => {
                $(resultElement).val(data)
            }
        })
    });

    $("#simetric-d-button").click(() => {
         let message = $("#simetric-d-text").val();
        let key = $("#simetric-d-key").val();
        let resultElement = $("#simetric-d-result")

        $.ajax({
            type: 'GET',
            url: `simetric_decrypt/${message}/${key}`,
            success: (data) => {
                $(resultElement).val(data)
            }
        })
    })
});