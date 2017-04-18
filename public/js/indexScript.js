$(document).ready(function () {
    setTimeout(function () {
        $('#links').animate({top: '250px'}, 'slow', function () {
            $('#learnMore').fadeIn('slow');
        });
    }, 5000);
});