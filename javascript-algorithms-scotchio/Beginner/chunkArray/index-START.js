/* 
 Given two or more arrays, write a function that combines
 their elements into one array without any repetition. 
 E.g  mergeArrays([1,2,3,3,3], [1,4,5,2]) // should return [1,2,3,4,5]
*/

function chunkArray(array, size) {
    const chunks = []

    // for (let i = 0; i < array.length; i += size) {
    //     chunks.push(array.slice(i, i+size))
    // }
    // return chunks

    let result = []
    for (value of array){
        let lastArray = result[result.length -1 ]
        if(!lastArray || lastArray.length == size){
            result.push([value])
        } else{
            lastArray.push(value)
        }
    }
    return result
}

// console.log(chunkArray([2,1,2,2,1], 4))
module.exports = chunkArray