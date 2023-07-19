function process() {
    let inputText = $("#input-text").val()
    let transformation = $("#transformation").val()
    let payload = {
        'transformation': transformation,
        'text': inputText
    }

    $.ajax({
        url: 'http://127.0.0.1:5000/process',
        type: "POST",
        data: JSON.stringify(payload),
        dataType: "json",
        headers: {
            "Content-Type": "application/json"
        },
        success: function(data) {
            $("#processed-text").html( data.transformed_text );
            $("#result").show(500);
        }
    });
}