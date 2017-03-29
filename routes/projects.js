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

router.get('/scribbler2', function (req, res, next) {
    res.render('projects/schoolProjects/scribbler2', {title: 'Python Fun'});
});

module.exports = router;
