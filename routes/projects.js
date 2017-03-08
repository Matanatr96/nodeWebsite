var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
    res.render('projects/projects', { title: 'Timeline'});
});

router.get('/timeline', function(req, res, next) {
    res.render('projects/timeline', { title: 'Timeline'});
});

router.get('/school', function(req, res, next) {
    res.render('projects/schoolProjects', { title: 'Timeline'});
});


module.exports = router;
