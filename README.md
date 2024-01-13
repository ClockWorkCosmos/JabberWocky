Python; CyberSecurity; Secure storage

Encrypt / decrypt files using algorithms inspired by Cipher's Cipher; Generate random, create custom, or load keys for encryption / decryption.

Required modules / libraries:

Random
Time

Algorithms:

Caesar's Cipher

1. A key is imported
  Key's are composed of two parts
  1. External key ( a text file containing a randomly generated or custom created key )
  2. Internal / built-in master key ( a variable within the program )
  3. The final character in each key is a magic number between 0 and 9

  Keys are stored securely using a magic number (2) to adjust / increase ASCII values of each character in the key before storage

2. Data to encrypt / decrypt is imported
3. Each character of the imported data, imported key, and master key are converted into their corresponding ASCII chart values
4. During encryption, values are added together and converted back into their characterized form to create the encrypted version of the data
5. Elsewise for decryption, both key values are substracted from the encrypted data values to revert them back to their decrypted version(s)


Footnote: this program can be further improved in security by adjusting / changing the key length, master key, magic number size, and number of times to be encrypted.


