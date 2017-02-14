var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
    res.render('index', { title: 'Homepage'});
});

router.get('/aboutMe', function (req, res, next) {
    res.render('aboutMe', {title: 'About Me'})
});

router.get('/gt', function (req, res, next) {
    res.render('gt', {title: 'School'})
});



module.exports = router;
