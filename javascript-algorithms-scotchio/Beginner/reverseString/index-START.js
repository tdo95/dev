/* CHALLENGE
Given a string of text, write an algorithm that returns the text received in a reversed format. 
E.g reverseString('algorithms') // should return 'smhtirogla'
*/



function reverseString(text) {
    // BUILT IN METHODS
    // return text.split('').reverse().join('')

    //FOR LOOP
    // let result = ''

    //Regular
    // for (let i = text.length - 1; i >= 0; i--) {
    //    result += text[i]
    // }

    //Es 6
    // for (let char of text) {
    //     result = char + result
    // }

    // return result

    //RECURSION
    // if (text === '') {
    //     return ''
    // } else {
    //     return reverseString(text.substr(1)) + text[0]
    // }

    //REDUCE
    return text.split('').reduce((acc, char) => char + acc, '')
}



module.exports = reverseString