var express = require('express'),
    http = require('http'),
    path = require('path'),
    logger = require('morgan'),
    favicon = require('serve-favicon'),
    cookieParser = require('cookie-parser'),
    bodyParser = require('body-parser'),

    app = express(),
    index = require('./routes/index'),
    projects = require('./routes/projects');

//routing to controllers
app.use('/projects', projects);
app.use('/', index);






// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

app.locals.basedir = path.join(__dirname); //set at /Website/
app.use(favicon(path.join(__dirname, 'public', '/images/favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));


// catch 404 and forward to error handler
app.use(function(req, res, next) {
  var err = new Error('Not Found');
  err.status = 404;
  next(err);
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;

/**
  Once i configure mongo
  Please refer to https://code.tutsplus.com/tutorials/build-a-complete-mvc-website-with-expressjs--net-34168

 MongoClient.connect('mongodb://' + config.mongo.host + ':' + config.mongo.port + '/fastdelivery', function(err, db) {
	if(err) {
		console.log('Sorry, there is no mongo db server running.');
	} else {
		var attachDB = function(req, res, next) {
			req.db = db;
			next();
		};
		app.all('/admin*', attachDB, function(req, res, next) {
			Admin.run(req, res, next);
		});
		app.all('/blog/:id', attachDB, function(req, res, next) {
			Blog.runArticle(req, res, next);
		});
		app.all('/blog', attachDB, function(req, res, next) {
			Blog.run(req, res, next);
		});
		app.all('/services', attachDB, function(req, res, next) {
			Page.run('services', req, res, next);
		});
		app.all('/careers', attachDB, function(req, res, next) {
			Page.run('careers', req, res, next);
		});
		app.all('/contacts', attachDB, function(req, res, next) {
			Page.run('contacts', req, res, next);
		});
		app.all('/', attachDB, function(req, res, next) {
			Home.run(req, res, next);
		});
		http.createServer(app).listen(config.port, function() {
		  	console.log(
		  		'Successfully connected to mongodb://' + config.mongo.host + ':' + config.mongo.port,
		  		'\nExpress server listening on port ' + config.port
		  	);
		});
	}
});
 MongoClient = require('mongodb').MongoClient,
 **/