let form = document.getElementById('form');
let action_default = form.getAttribute("action");

$('button.open-popup').click(function() {
    let comment_id = $(this).attr('value');

    if (!!comment_id) {
        let new_action = action_default + "?comment_id=" + comment_id;
        form.setAttribute("action", new_action);
    }


    $('.popup-bg').fadeIn(600);
});
$('.close-popup').click(function() {
    form.setAttribute("action", action_default);
    $('.popup-bg').fadeOut(600);
});


$('button.open-file').click(function() {
    let file_id = $(this).attr('value');
    let file_format = file_id.split('.').pop();

    if (file_format == 'jpg' || file_format == 'png' || file_format == 'gif') {
        document.getElementById('file_img').src = file_id;
    }
    if (file_format == 'txt') {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', file_id);
        xhr.onload = function() {
          if (xhr.status === 200) {
            document.getElementById('file_text').innerHTML = xhr.responseText.replace(/\n/g, '<br>');
          }
          else {
            console.error('Failed to load file');
          }
        };
        xhr.send();
    }



    $('.open-file-popup-bg').fadeIn(600);
});
$('.file-close-popup').click(function() {
    document.getElementById('file_img').src = "";
    document.getElementById('file_text').textContent = "";
    $('.open-file-popup-bg').fadeOut(600);
});


var params = window
    .location
    .search
    .replace('?','')
    .split('&')
    .reduce(
        function(p,e){
            var a = e.split('=');
            p[ decodeURIComponent(a[0])] = decodeURIComponent(a[1]);
            return p;
        },
        {}
    );

$('#sort_id').val(params["sort"]);