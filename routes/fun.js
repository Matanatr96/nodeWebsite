var express = require('express');
var router = express.Router();
var path = require('path');

var server = require('http').Server(express);
var io = require('socket.io')(server);

router.get('/', function (req, res, next) {
    res.sendFile(path.join(__dirname, '../views/whiteboard/test.pug'));
});

io.on('connection', function (socket) {
    socket.emit('news', {hello: 'world'});
    socket.on('my other event', function (data) {
        console.log(data);
    });
});

module.exports = router;