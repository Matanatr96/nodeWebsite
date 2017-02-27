var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
    res.render('projects/projects', { title: 'Timeline'});
});

router.get('/timeline', function(req, res, next) {
    res.render('projects/timeline', { title: 'Timeline'});
});


module.exports = router;
