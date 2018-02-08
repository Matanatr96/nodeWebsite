var express = require('express');
var router = express.Router();
var model = new (require('../models/ContentModel'));

router.get('/', function(req, res, next) {
    res.render('index/index', { title: 'Homepage'});
});

router.get('/intro', function (req, res, next) {
    res.render('index/intro', {title: 'Intro'})
});

router.get('/aboutMe', function (req, res, next) {
    res.render('index/aboutMe', {title: 'About Me'})
});





module.exports = router;
