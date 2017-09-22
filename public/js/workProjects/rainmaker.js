/**
 * Created by Anush on 5/4/2017.
 */
$(document).ready(function () {
    $('#imageLink').on('click', function () {
        var src = $(this).attr('image');
        $('#modalImage').attr('src', src);
        $('#myModal').css('display', 'block');
        $('#caption').text($(this).attr('caption'));
    });

    $('.close').on('click', function () {
        $('#myModal').css('display', 'none');
    });
});

