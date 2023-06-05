/* CHALLENGE
Given a sentence containing two or more words, 
return the equivalent of the sentence when capitalised. E.g
  capSentence('the tales of scotch!') // would return 'The Tales Of Scotch!' 
*/




function capSentence(text) {
   //seperate words by space
   //iterate over each item
    //capitalize the first letter of the item
  
  //BUILT IN METHOD
  // return text.toLowerCase().split(' ').map(word => word[0].toUpperCase() + word.slice(1)).join(' ')

  //ITERATIVE METHOD
  let capString = ''
  for (let i = 0; i < text.length; i++) {
    if (i === 0) {
      capString += text[i].toUpperCase()
    }
    else if (text[i] == ' ') {
      capString += ' ' + text[i + 1].toUpperCase()
      i += 1
    }
    else {
      capString += text[i].toLowerCase()
    }

  }
  return capString
}



module.exports = capSentence