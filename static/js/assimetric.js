$(document).ready(() => {
    $("#button-assimetric_get_key").click(() => {
        let resultElement = $("#assimetric_get_key");

        $.ajax({
            type: 'GET',
            url: `get_public_key`,
            success: (data) => {
                $(resultElement).html(data)
            }
        })
    });

    $("#button-assimetric_get_key_p").click(() => {
        let resultElement = $("#assimetric_get_key_p")

        $.ajax({
            type: 'GET',
            url: `get_private_key`,
            success: (data) => {
                $(resultElement).val(data)
            }
        })
    })
});