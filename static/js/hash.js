$(document).ready(() => {
    $("#hash-button").click(() => {
        let message = $("#hash-message").val()
        let result = $("#hash-result")


        $.ajax({
            type: 'GET',
            url: `hash/${message}`,
            success: (data) => {
                $(result).html(data)
            }
        })
    })

})