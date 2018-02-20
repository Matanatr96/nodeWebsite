var express = require('express');
var router = express.Router();
var model = new (require('../models/ContentModel'));

router.get('/', function (req, res, next) {
    res.render('photos/photosHome', {title: 'Photos'})
});

module.exports = router;