var express = require('express');
var app = express();
const axios = require("axios");
var cheerio = require("cheerio");
const rp = require('request-promise');


var port = process.env.PORT || 8000;

app.set('view engine', 'ejs');

app.use(express.static(__dirname + '/public'));

app.get('/', function(req, res) {


	res.render('index',{result:""});
});
app.get('/name', callName); 
  
function callName(req, res) { 
      

    var spawn = require("child_process").spawn; 

    var process = spawn('python',["./corona.py", 
                            req.query.firstname, 
                            req.query.lastname] ); 
  

	msg="";
    process.stdout.on('data', function(data) { 
		sum=(data.toString());
		if(req.query.lastname=="deaths")
		{
			msg=sum+" people died in "+req.query.firstname;
		}
		if(req.query.lastname=="confirmed")
		{
			msg="There are "+sum+" confirmed cases of Corona in "+req.query.firstname;
		}
		if(req.query.lastname=="recovered")
		{
			msg=sum+" people have been recoverd from Corona in "+req.query.firstname;
		}
		res.render('index',{result:msg}); 
    } ) 
} 

app.listen(port, function() {
	console.log('Corona details is running on http://localhost:' + port);
});
