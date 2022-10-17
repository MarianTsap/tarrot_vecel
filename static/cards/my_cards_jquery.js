$(document).ready(function(){
$("#div_meaning").click(function () {
        //var street = $(this).val();
        $(this).hide()
        var cards_array_json = JSON.stringify(cards_array);
        $.ajaxSetup({
            headers: {
                "X-CSRFToken": document.querySelector('[name=csrfmiddlewaretoken]').value,
            }
        });
        $.ajax({
        url: 'meaning',
        method: 'POST',
        data: {
          'cards_array': cards_array_json
        },
        dataType: 'json',
        success: function (data) {
           // $("#scode").empty();
            var foo = document.getElementById("display");
            var meaning=document.createElement("div");
            meaning.setAttribute('class',`container`);
            meaning.setAttribute('id',`meaning_text`);
            foo.appendChild(meaning);
            for (const [key, value] of Object.entries(data)) {
                meaning.innerHTML += "<p>Card - "+ value[0]+" <br><small>" + value[1]+"</small></p>";
            }
            var element = document.getElementById("meaning_text");
            element.scrollIntoView();
        }
      });
});
});