/* CHALLENGE
Given a string of text, return true or false indicating whether or not the text is a palindrome.
e.g palindromeChecker('racecar') // will return true
*/




function palindromeChecker(text) {
    //reverse text
    let reversed = text.LowerCase().split('').reverse().join('')
    //check if reverse version is the same as regular
    return reversed === text
}



module.exports = palindromeChecker;