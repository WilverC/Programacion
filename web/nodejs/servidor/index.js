/* Creacion de servidor puro js
const http = require( 'http' );

const handleServer = function(req, res){
    res.writeHead( 200, { 'Content-type' : 'text/html' } );
    res.write( '<h1> Hola mundo </h1>' );
    res.end();
}

const server = http.createServer( handleServer );

server.listen(3000, function(){
    console.log( 'Server on port 3000' );
});*/

const express = require( 'express' );

const server = express();

server.get( '/', (req, res) => {
    res.send( '<h1> Hola Mundo con Express y node </h1>' );
    res.end();
});

server.listen( 3000, () => {
    console.log( 'Server on port 3000' );
}
);