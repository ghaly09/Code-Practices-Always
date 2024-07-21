"use strict";
// Palindrome Number
/*
Given an integer x, return true if x is a
palindrome
, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
*/
function isPalindrome(x) {
    let leftNum = "";
    let rightNum = "";
    let stringNum = String(x);
    for (let i = 1; i < stringNum.length + 1; i++) {
        leftNum += stringNum[i - 1];
        rightNum += stringNum[stringNum.length - i];
    }
    return leftNum === rightNum;
    // return typeof stringNum;
}
console.log(isPalindrome(10));
