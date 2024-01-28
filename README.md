Python; CyberSecurity; Vigenere Cipher

Encrypt / decrypt files using an extension of Caesar's Cipher called Vigenere Cipher; Generate random, create custom, or import keys for encryption / decryption

! WARNING: DO NOT APPLY ENCRYPTION KEYS MORE THAN ONCE OR ELSE FILES MAY BE AT RISK FOR CORRUPTION !

Required modules / libraries:
1. Random
2. Time
3. Termcolor
4. OS #Optional

Algorithm(s):

Vigenere Cipher

1. A key is imported
2. Data to encrypt / decrypt is imported
3. Each character of the imported data, imported key, and master key are converted into their corresponding ASCII chart values
4. During encryption, values are added together and converted back into their characterized form to create the encrypted version of the data
5. Elsewise for decryption, both key values are substracted from the encrypted data values to revert them back to their decrypted version(s)
