/*
Write a function to return the nth element in Fibonacci sequence,
where the sequence is:
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, …]
*/


function fibonacci(n) {
    // Code goes here
    if (n < 0) return 0
    else if (n === 0) return 1
    else return fibonacci(n - 2) + fibonacci(n - 1)
}

module.exports = fibonacci