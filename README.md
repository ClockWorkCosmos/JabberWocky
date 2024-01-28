Python; CyberSecurity; Vigenere Cipher

Encrypt / decrypt files using an extension of Caesar's Cipher called Vigenere Cipher; Generate random, create custom, or import keys for encryption / decryption

Observed error during testing : 
  * Certain characters with ASCII values less than 40, in combination with certain keys, may result in error during the decryption process in which the ASCII value falls out of range. Try removing punctuation from the
    text file.

Required modules / libraries:
1. Random
2. Time
3. Termcolor
4. OS #Optional

Algorithm(s):

Vigenere Cipher

1. A key is imported. Key's are composed of two parts. The first part is the external key ( a text file containing a randomly generated or custom created key ). The second part is the internal / built-in master key ( a variable within the program ). The final character in each key is a magic number between 0 and 9. Keys are stored using a magic number (2) to adjust / increase ASCII values of each character in the key before storage


2. Data to encrypt / decrypt is imported
3. Each character of the imported data, imported key, and master key are converted into their corresponding ASCII chart values
4. During encryption, values are added together and converted back into their characterized form to create the encrypted version of the data
5. Elsewise for decryption, both key values are substracted from the encrypted data values to revert them back to their decrypted version(s)
