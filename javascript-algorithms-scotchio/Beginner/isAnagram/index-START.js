/* CHALLENGE
Given a two strings, write an algorithm to check if they are anagrams
of each other. Return true if the pass the test and false if they
don't. E.g
    isAnagram('silent', 'listen') // should return true
*/



function isAnagram(stringA, stringB) {
    const sortedA = stringA.split('').sort().join('')
    const sortedB = stringB.split('').sort().join('')

    return sortedA === sortedB


    //Alternative you can create a map counting the character amount in each string then compare each value, any value is not the same return false, else return true
}


module.exports = isAnagram