# Problem 4

## Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

## Notes

* First solution through brute force
* the palindrome destection is done with strings

>   Solution from the wesbsite's forum. Knowing that the number is a multiplication of two 3 digit numbers, the product is expressed a 

    The palindrome can be written as:
    abccba
    Which then simpifies to:
    100000a + 10000b + 1000c + 100c + 10b + a
    And then:
    100001a + 10010b + 1100c
    Factoring out 11, you get:

    11(9091a + 910b + 100c)
    