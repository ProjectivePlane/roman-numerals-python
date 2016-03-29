#!/usr/bin/python
import roman_numerals
import unittest

class TestNumerals(unittest.TestCase):
    def setUp(self):
        self.numerals=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
        self.expected=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        self.numbers=[2016,1968]
        self.expected_number_lists=["MMXVI","MCMLXVIII"]

    def testNumerals(self):
        for n,rn in zip(self.numerals,self.expected):
            self.assertEquals(roman_numerals.toRoman(n),rn)

    def testNumbers(self):
        for n,rn in zip(self.numbers,self.expected_number_lists):
            self.assertEquals(roman_numerals.toRoman(n),rn)
            
class TestSplitNumber(unittest.TestCase):
    def setUp(self):
        self.numbers=[2016,1968,10,9,8,7,6,5,4,3,2,1]
        self.expectedLists=[[1000,1000,10,5,1],[1000, 900, 50, 10, 5, 1, 1, 1],[10],[9],[5,1,1,1],[5,1,1],[5,1],[5],[4],[1,1,1],[1,1],[1]]

    def testSplit(self):
        for n,ln in zip(self.numbers,self.expectedLists):
            self.assertEquals(roman_numerals.splitNumber(n),ln)

class TestConvertRomanNumeralToInteger(unittest.TestCase):
    def setUp(self):
        self.roman_numerals_upper=["I","II","III","IV","V","VI","VII","VIII","IX","X","XI","XII","XIII","XIV","XV","XVI","XVII","XVIII","XIX","XX","XL","XLV","L","LV","XC","XCV","C","CX","CD","CDL","D","CM","M"]
        self.roman_numerals_lower=["i","ii","iii","iv","v","vi","vii","viii","ix","x","xi","xii","xiii","xiv","xv","xvi","xvii","xviii","xix","xx","xl","xlv","l","lv","xc","xcv","c","cx","cd","cdl","d","cm","m"]
        self.integers=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,40,45,50,55,90,95,100,110,400,450,500,900,1000]

    def testConvertRomanNumeralToInteger(self):
        for r,n in zip(self.roman_numerals_upper,self.integers):
            self.assertEquals(roman_numerals.toInteger(r),n)
        for r,n in zip(self.roman_numerals_lower,self.integers):
            self.assertEquals(roman_numerals.toInteger(r),n)

class TestErrorHandling(unittest.TestCase):
    def setUp(self):
        self.valid_roman_examples=["I","II"]
        self.invalid_roman_examples=["A","B"]

    def testIsValid(self):
        for v in self.valid_roman_examples:
            self.assertTrue(roman_numerals.isValidRomanNumeral(v))
        for i in self.invalid_roman_examples:
            self.assertFalse(roman_numerals.isValidRomanNumeral(i))

    def testThrowsException(self):
        def testThrowsInvalidRomanNumeralException(self):
            with self.assertRaises(roman_numerals.InvalidNumeralException):
                roman_numerals.toInteger("A")
            
if __name__ == '__main__':
    unittest.main()            
