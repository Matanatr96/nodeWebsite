var socket = io.connect('http://localhost');
socket.on('news', function (data) {
    console.log('test.js', data);
    socket.emit('my other event', {my: 'data'});
});