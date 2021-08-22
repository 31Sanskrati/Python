letter = ''' Dear <|NAME|>,

                        You are selected!

                        <|DATE|> '''

your = input("Enter your name\n")
date = input("Enter date \n")

letter = letter.replace("<|NAME|>", your)
letter = letter.replace("<|DATE|>", date)

print(letter)