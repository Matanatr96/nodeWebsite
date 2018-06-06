var express = require('express');
var app = express();

var router = express.Router();
var MongoClient = require('mongodb').MongoClient;
var uri = "mongodb+srv://Windows-PC:135792468a@cluster0-bwznf.mongodb.net/test";
var bodyParser = require('body-parser');
var urlencodedParser = bodyParser.urlencoded({extended: false});
app.use(bodyParser);


router.post('/timeData', urlencodedParser, function (req, res, next) {
    MongoClient.connect(uri, function (err, client) {
        if (err) {
            console.log('Holy error batman');
        } else {
            client.db('test').collection('Quotes').insert(req.body);
            client.close();
        }
    });
    res.render('data/dataHome');
});

router.get('/', function (req, res, next) {
    MongoClient.connect(uri, function (err, client) {
        if (err) {
            console.log('Holy error batman');
        } else {
            var queried = client.db('test').collection('Quotes').find();
            queried.each(function (err, quote) {
                if (quote !== 'null') console.log(quote);
            });
            client.close();
        }
    });
    res.render('data/dataHome', {title: 'Homepage'});
});

module.exports = router;