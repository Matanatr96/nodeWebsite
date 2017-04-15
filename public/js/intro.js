$(document).ready(function () {
    setTimeout(function () {
        $('#img').fadeOut('slow', function () {
            $('#nonImage').fadeIn('slow');
        });
    }, 2000);
});
