$('#ymd').on('submit', function(event){
    event.preventDefault();
    $.ajax({
        url: 'result',
        type: 'get',
        dataType: 'json',
        data: $('form#ymd').serialize(),
        success: function(data) {
                   console.log(data);
                   $("#result").html(data.result);
                 }
    });
});
