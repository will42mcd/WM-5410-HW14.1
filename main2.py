zero = "zero"
thousand = "onethousand"
units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
teens = ["", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
tens = ["", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def countCharacters(start, end):
    word_nums = []
    word = ""
    for num in range(start, end+1, 1):
        if num == 0:
            word = zero
            word_nums.append(word)
            long_string = "".join(word_nums)
            word_nums.append(long_string)
            continue
        elif num == 1000:
            word = thousand
            word_nums.append(word)
            continue

        if num >= 100:
            word += units[num // 100] + "hundred"
            num %= 100

        if 10 < num < 20: 
            word += teens[num - 10]
        else:
            if num >= 20:  
                word += tens[num // 10]
                num %= 10
                if num > 0:
                    word += "" + units[num]
            elif num == 10: 
                word += tens[num // 10]
            elif num < 10:  
                word += units[num]
        
        word_nums.append(word)
    
    print("word:    ",word_nums[-1], "\nnum of char:  ", len(word_nums[-1]), "\n")
    
if __name__ == "__main__":
    countCharacters(1, 3)
    countCharacters(41,41)
    countCharacters(101,101)