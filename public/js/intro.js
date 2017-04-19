$(document).ready(function () {
    alert('Please note: This website is under development. What you see now may or may not be in the final version of this site.');
    setTimeout(function () {
        $('#img').fadeOut('slow', function () {
            $('#nonImage').fadeIn('slow');
        });
    }, 2000);
});
