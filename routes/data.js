var express = require('express');
var router = express.Router();
var model = new (require('../models/ContentModel'));
var MongoClient = require('mongodb').MongoClient;
var uri = "mongodb+srv://Windows-PC:135792468a@cluster0-bwznf.mongodb.net/test?retryWrites=true";

router.get('/', function (req, res, next) {
    res.render('data/dataHome', {title: 'Homepage'});
});

router.get('/timeData', function (req, res, next) {
    MongoClient.connect(uri, function (err, client) {
        if (err) {
            console.log('Holy error batman');
        } else {
            const collection = client.db("test").collection("randomData");
            // perform actions on the collection object
            client.close();
        }
    });

    res.render('data/dataHome');
});

module.exports = router;