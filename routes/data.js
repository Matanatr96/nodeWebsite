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
            var jokeCollection = client.db('test').collection('Quotes');
            jokeCollection.find({}).toArray(function (err, jokeResult) {
                if (err) {
                    res.send(err);
                } else if (jokeResult.length) {
                    res.render('data/dataHome', {title: 'Data Home', data: jokeResult});
                }
            })
            client.close();
        }

    });

});

function isValid(testVar) {
    return testVar && testVar !== 'null' && testVar !== 'undefined';
}

module.exports = router;