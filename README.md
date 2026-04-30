# Mac Menu Information Decoder

This python program decodes and unpacks Mac meal details and information from a word(16-bit) input. 14-bits are used for the order information while the 3-bits in the beginning (starting from the MSB) are unused.
bit 3 tells us about the pickup info. (1 option)
bit 4 tells us about the payment method. (1 option)
bit 5 and 6 tells us about the type of sauce. (4 options)
etc...

## Important Note

There is also a system that takes only the first 16-bit only. So whenever the user inputs a HEX number that is more than 16-bits the number will be padded to 16-bit. 
However if the user inputs a HEX number less than 16-bit the number or the binary number will be leaded by zero inorder to read a whole word.

## Usage

1. Run the program
2. Enter a hexadecimal number when prompted
3. The program will output the details about the order

### Example

```bash3
Meal Details:
Meal: 40-piece Chicken McNuggets
Drink: Coca-Cola
Size: Extra Large
With/Without fries: With Fries
Sauce type: Mayo
Payment Method: Card
Pickup: In-Store
Enjoy!
