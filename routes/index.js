var express = require('express');
var router = express.Router();

var model = new (require('../models/ContentModel'));

router.get('/', function(req, res, next) {
    res.render('index/index', { title: 'Homepage'});
});

//keep these here till i add more view to each "controller"
router.get('/aboutMe', function (req, res, next) {
    res.render('index/aboutMe', {title: 'About Me'})
});

router.get('/gt', function (req, res, next) {
    model.h
    res.render('index/gt', {title: 'School'})
});



module.exports = router;
