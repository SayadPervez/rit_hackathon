var http = require("http");
var path = require('path');
const fs=require('fs');


function shell(func){
    const execSync = require('child_process').execSync;
    const output = execSync("python news.py ", { encoding: 'utf-8' });
    return(output);
}

function readRet() {
    arr.push(fs.readFileSync('./return.txt',{ encoding: 'utf8' }));
    console.log(arr+">>><<<");
}


async function stringToJson(data){
    return(JSON.parse(data.replace(/'/g, '"')));
}
function writeCall(content,cb1){
    fs.writeFileSync('./call.txt',content,'utf-8');
}

var server = http.createServer(function (req, res) {
    console.log(req.url);
    if(req.url === '/'){
        fs.readFile('./skeleton.html','UTF-8',(err,html)=>{
            res.writeHead(200,{'Content-Type':'text/html'});
            res.end(html);
        });
    }else if(req.url.match('\.css$')){
        var cssPath=path.join(__dirname,req.url);
        var fileStream= fs.createReadStream(cssPath,'UTF-8');
        res.writeHead(200,{'Content-Type':'text/css'});
        fileStream.pipe(res);
    }else if(req.url.match('\.js$')){
        var cssPath=path.join(__dirname,req.url);
        var fileStream= fs.createReadStream(cssPath,'UTF-8');
        res.writeHead(200,{'Content-Type':'text/javascript'});
        fileStream.pipe(res);
    }else{
        res.writeHead(200,{'Content-Type':'text/html'});
        res.end('<h1>Error 404 <br> Page not found !</h1>');
    }
    if (req.method=="POST"){
        console.log('Fuck yeah');
    
    let body = '';
    req.on('data', chunk => {
        body += chunk.toString();
    });
    req.on('end', () => {
        console.log(body);
        console.log(shell(body));
        res.end(shell(body));
    });
}



}).listen(3000,()=>{
    console.log('Listening at 3000');
});