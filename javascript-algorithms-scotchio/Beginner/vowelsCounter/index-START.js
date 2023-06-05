/* CHALLENGE
Given a string of text, return the number of vowels found within the text
e.g vowelsCounter('anehizxcv') // will return 3
*/


function vowelsCounter(text) {
    //ITERATIVE APPROACH
    const vowels = ['a', 'e', 'i', 'o', 'u']
    let count = 0

    //set all characters to lowercase
    //iterate over each letter in string
    for (let char of text.toLowerCase()) {
        if (vowels.includes(char)) count++
    }
    return count;

    //REGULAR EXPRESSION
    // let matchingInstances = text.match(/[aeiou]/gi)
   
    // return (matchingInstances.length || 0)
    

    
}



module.exports = vowelsCounter;
