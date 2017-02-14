var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
    res.render('projects/projects', { title: 'projects'});
});

router.get('/project1', function (req, res, next) {
    res.render('projects/project1', {title: 'Tic Tac Toe'})
});


module.exports = router;
