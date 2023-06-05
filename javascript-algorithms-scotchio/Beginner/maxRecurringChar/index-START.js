/* CHALLENGE
Given a string of text, find and return the most recurring character. 
e.g maxRecurringChar('aabacada') // will return 'a'
*/



function maxRecurringChar(text) {
    //count chars in string
    const charCountMap = {}
    for (let char of text) {
        //add count to existing
        if (charCountMap[char])
            charCountMap[char] += 1
        //create property add one
        else charCountMap[char] = 1   
    }
    let largestValue = 0
    let largestLetter = ''
    //find largest value in map
    for (let char in charCountMap)
        if (charCountMap[char] > largestValue) {
            largestValue = charCountMap[char]
            largestLetter = char
        }
    return largestLetter

    

}



module.exports = maxRecurringChar;