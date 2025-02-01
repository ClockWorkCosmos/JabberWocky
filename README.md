JabberWocky: Vigenère Cipher Encryption & Decryption Tool
---------------------------------------------------------

"JabberWocky is a command-line utility designed for encrypting and decrypting files using an extended version
of the Caesar cipher known as the Vigenère cipher."

Key Features :
* Encryption & Decryption: Uses the Vigenère cipher to encode and decode files.
* Key Management: Supports generating, customizing, and importing encryption keys.
* File Integrity Check: Allows users to compare files to detect changes and ensure successful decryption without file integrity loss.
* Color-Coded Interface: Enhances readability and usability in the terminal.

Usage :
* Users can run the script and follow the interactive menu options to perform encryption, decryption, or key management.

Process Overview :
* A key is imported.
* The data to be encrypted or decrypted is loaded.
* Each character in the data, key, and master key is converted into its corresponding ASCII value.
* Encryption: ASCII values are summed and converted back into characters to produce encrypted data.
* Decryption: ASCII values are subtracted to restore the original text.
* Key generation: A random set of ASCII values are generated and converted into characters to form a key. The key is encrypted with pure Caesar's cipher before storage.
* Custom Key Creation: A custom key is provided / typed by the user and stored under a desired text file name. The key is encrypted with pure Caesar's cipher before storage.
* File Comparison: Compares the individual characters of two text files and calculates the difference as a float or percentage. If the difference surpasses a predefined threshold, the system will issue a warning. -
  This feature can be used to verify the integrity of an encrypted and decrypted file by comparing it to the original, ensuring successful encryption and decryption with the selected key.

Technical Details :
* Programming Language: Python
* Relevant Skills: Cybersecurity, Cryptography, Vigenère Cipher

Required Libraries :
* random (Key generation)
* time (Timing operations)
* termcolor (Color-coded output)
* os (Optional, for file handling)

! Warning : Applying encryption keys more than once can
"corrupt" files, making decryption impossible. Use keys carefully
and ensure proper management with labeling and folder storage. !
