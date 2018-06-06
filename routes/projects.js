var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
    res.render('projects/projects', { title: 'Projects'});
});

router.get('/timeline', function(req, res, next) {
    res.render('projects/timeline', { title: 'Timeline'});
});

router.get('/buzzMovieSelector', function(req, res, next) {
    res.render('projects/schoolProjects/buzzMovieSelector', { title: 'Android App'});
});

router.get('/tsys', function (req, res, next) {
    res.render('projects/workProjects/tsysDictionary', {title: 'Tsys Dictionary'});
});

router.get('/scribbler2', function (req, res, next) {
    res.render('projects/schoolProjects/scribbler2', {title: 'Python Fun'});
});

router.get('/rainmaker', function (req, res, next) {
    res.render('projects/workProjects/rainmaker', {title: 'Rainmaker'});
});

router.get('/flappyBird', function (req, res, next) {
    res.render('projects/schoolProjects/flappyBird', {title: 'Flappy Bird'});
});

router.get('/sentimentAnalysis', function (req, res, next) {
    res.render('projects/personalProjects/sentimentAnalysis', {title: 'NLP Text Classification'});
});

module.exports = router;
