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