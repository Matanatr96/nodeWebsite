var express = require('express');
var router = express.Router();

router.get('/', function(req, res, next) {
    res.render('timeline/timeline', { title: 'Timeline'});
});



module.exports = router;