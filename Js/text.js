




// const txt = 'lorem ipsum dolor sit amet, lorem des DES consectetur : : : : adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.';


// let arr = txt.split(' ').reduce((acc, word) => {
//     acc[word] = (acc[word] || 0) + 1 ;
//     return acc;
// }, {}) ;


// let result = Object.entries(arr).sort((a, b) => b[1] - a[1])[0] ;

// console.log(result) ;


// let resultDes = txt.split(' ').reduce((acc, word) => {
//     return 'des' === word.toLowerCase() ? acc + 1 : acc;
// }, 0 ) ;


// console.log(resultDes);

// const phrase = 'saàtion pour le test de la fonction de recherche de phrase dans un texte' ;

// let countA = phrase.split('').reduce((acc, word) => {
//     return 'a' === word.toLowerCase() ? acc + 1 : acc;
// } , 0) ;

// console.log(countA);









// matrix 9x9 avec des . et des #

const mat = [
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '#', '#', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '#', '.', '.'],
    ['.', '#', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '#', '#', '#', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '.', '#', '.', '.'],
    ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
];

const tournes = {
    'L' : {
        'E' : 'N' ,
        'N' : 'W' , 
        'W' : 'S' , 
        'S' : 'E' ,
    } , 
    'R' : {
        'E' : 'S' ,
        'S' : 'W' , 
        'W' : 'N' , 
        'N' : 'E' ,
    } , 
} ;


let directions = 'E' ;
let positions = [0, 0];
let echecs = 0 ; 



// "FFFFFRFFFRFFFLFFJRFRFLFFRFFLFR"
const Bande = "FFFFFRFFFRFFFLFFJRFRFLFFRFFLFR" ;

for(let instruction of Bande) {
    if(instruction === 'L' || instruction === 'R') {
        directions = tournes[instruction][directions] ;
    }else {
        let step = (instruction === 'J') ? 2 : 1 ;
        let newPosition = [...positions] ;


        if(directions === 'E') newPosition[1] += step ;
        else if(directions === 'W') newPosition[1] -= step ;
        else if(directions === 'S') newPosition[0] += step ;
        else if(directions === 'N') newPosition[0] -= step ;

        if(newPosition[0] < 0 || newPosition[0] >= mat.length || newPosition[1] < 0 || newPosition[1] >= mat[0].length || mat[newPosition[0]][newPosition[1]] === '#') {
            echecs++ ;
        }else {
            positions = newPosition ;
        }
    }
}


console.log( positions );
console.log( directions );
console.log( echecs );

















