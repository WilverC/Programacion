
/*
 * uso del modulo OS
const os = require( 'os' );

console.log( os.platform() );
console.log( os.release() );
console.log( 'free mem: ', os.freemem(), 'bytes' );
console.log( 'Total mem: ', os.totalmem(), 'bytes' );
*/


const fs = require( 'fs' );

//código asincrono
//crea un archivo y escribe 'linea uno'. la funcion recibe los errores
fs.writeFile( './texto.txt', 'linea uno', function(err){
    if( err ){
        console.log( err );
    }
    console.log( 'Archivo creado' );
} );

console.log( 'Ultima linea' );

//lee un archivo los datos son crudos convertir a string
fs.readFile( './texto.txt', function(err, datos){
    if( err ){
        console.log( err );
    }
    console.log( datos.toString() );
});