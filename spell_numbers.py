"""Convert numbers from digits to words in Estonian."""
from argparse import ArgumentParser
import sys
LANGUAGES = [
# uncomment "est" below if you implement Estonian numbers,
# or "eus" if you implement Basque numbers
"est",
# "eus",
]
def est(number):
    """Convert an integer into its Estonian number spelling.

    Args:
    number (int): An integer between 0 and 999999, inclusive.

    Returns:
    str: The number spelled out in Estonian."""
    number_words = ["null","üks", "kaks", "kolm","neli", "viis", "kuus", "seitse", "kaheksa", "üheksa" , "kümme"]
    if number >= 0 and number <= 10 :
       return number_words[number] 
    elif number%10 >= 1 and number%10 <= 9 and number >= 11 and number <=19:
       return (number_words[number%10] + "teist")
    elif (number//10) >=2 and (number//10) <= 9 and (number%10) == 0  :
       return (number_words[number//10] + "kümmend")
    elif number >= 20  and  number <= 99:
       if (number%10) >=1 and (number%10)<=9:
        return (number_words[(number//10)] + "kümmend" + " " + number_words[number%10])
    elif (int(number/100)) >=1 and (int(number/100)) <=9 and (number%100 ==0):
       if (number) == 100:
           return "sada"
       else:
           return (number_words[int(number/100)] + "sada")   
    elif number >= 101 and number <= 999:
        hundreds_part = (number // 100) * 100
        remainder = number % 100
        return est(hundreds_part) + " " + est(remainder)
    elif (number) >=1000   and (number) <= 999999 :
       thousands_part = (number//1000) 
       remainder = (number%1000)
       if (number) == 1000:
           return ('tuhat')
       if (thousands_part) == 1 and (thousands_part)<= 1009:
           return ('tuhat ' + est(remainder))
       if (number%1000) == 0:
           return(est(thousands_part) + " tuhat")
       elif (number) > 1000:
           return (est(thousands_part) +" tuhat " + est(remainder))
       
# (along with any helper functions, constants, etc. that you want to write)
def main(language_code,  input_file, output_file):
    """Convert numbers from an input file into Estonian words.

Args:
    language_code (str): The three-letter code for the supported language.
    input_file (str): The path to the file containing numbers.
    output_file (str): The path to the output file to create.

Side effects:
    Reads from the input file and writes the converted numbers to the
    output file.

Raises:
    ValueError: If the language code is not "est".
"""
    if language_code  != "est":
        raise ValueError("Unsupported language code")
    with open(input_file, "r", encoding="utf-8") as infile, \
         open(output_file, "w", encoding="utf-8") as outfile:
            for line in infile:
                number = int(line.strip())
                outfile.write(f"{number} = {est(number)}\n")
def parse_args(arglist):
    """Parse command-line arguments.
    Three arguments are required, in the following order:
    lang (str): the ISO 639-3 language code of the language the user wants
    to convert numbers into.
    input_file (str): path to a file containing numbers expressed as digits.
    output_file (str): path to a file where numbers will be written as words
    in the target language.
    Args:
    arglist (list of str): list of command-line arguments.
    Returns:
    namespace: the parsed arguments as a namespace. The following attributes
    will be defined: lang, input_file, and output_file. See above for
    details.
    """
    parser = ArgumentParser()
    parser.add_argument("lang", help="ISO 639-3 language code")
    parser.add_argument("input_file", help="input file containing numbers")
    parser.add_argument("output_file", help="file where output will be stored")
    return parser.parse_args(arglist)
if __name__ == "__main__":
    args = parse_args(sys.argv[1:])
    main(args.lang, args.input_file, args.output_file)
