// obtiene las funciones del modulo en una constante
const math = require( './math.js' );

console.log( math );

console.log( math.add ( 1, 2 ) );
console.log( math.substract ( 2, 1 ) );
console.log( math.multiply ( 1, 2 ) );
console.log( math.divide ( 1, 2 ) );
console.log( math.divide ( 1, 0 ) );