const path = require('path')
const {spawn} = require('child_process')
var express = require('express');
var server = express();




//Execution du script toutes les 6h
function runScript(){
  console.log("Execution run script");
    return spawn('python', [
    "-u",
    path.join(__dirname, 'botEDT_ScreenShot.py'),
    "--foo", "some value for foo",
    ]);

  }
  setInterval(() => {
    runScript();
  }, 3600000);


//Serving static file / route principale
server.get('/', function(req, res) {
  /**
    * Run python myscript, pass in `-u` to not buffer console output
    * @return {ChildProcess}
  */
  
    
  server.use(express.static('./'));
  var dirPath = __dirname;
  
	res.sendFile(`${dirPath}/index.html`);
});




server.listen(8080);
