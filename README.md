Simple Word Encoder/Decoder in Python
This Python script encodes and decodes text messages using a basic word manipulation technique:

Input: User enters a message and chooses encoding (0) or decoding (1).

Encoding:

Words with 3 or more letters are transformed by:

Moving the first letter to the end.

Adding random strings (dfg at the start, ede at the end).

Short words (less than 3 letters) are simply reversed.

Decoding:

Removes the added strings.

Restores the original word order by moving the last character back to the front.

Short words are reversed back to normal.

Output: The transformed message is displayed.
