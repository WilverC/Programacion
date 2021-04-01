/* Creacion de un objeto*/
const Mathe = {};

function add(x1, x2){
    return x1 + x2;
}

function substract(x1, x2){
    return x1 - x2;
}

function multiply(x1, x2){
    return x1 * x2;
}

function divide(x1, x2){
    if( x2 == 0 ){
        console.log('no se puede dividir por 0');
    }else{
        return x1 / x2;
    }
}

/* Sirve para que las funciones en este archivo pueda ser ocupado por
 * otro archivo, es decir exportarlo.
 * exporta una propiedad de un objeto
exports.add = add;
exports.substract = substract;
exports.multiply = multiply;
exports.divide = divide;
*/

/* Se adjuta las funciones al objeto*/ 
Mathe.add = add;
Mathe.substract = substract;
Mathe.multiply = multiply;
Mathe.divide = divide;
// se exporta el objeto
// exporta objetos, funciones, variables y cualquier dato de java script
module.exports = Mathe;