## If you are on GitHub this is a mirror, the original repository with the latest updates is at [https://forgejo.neoeden.org/ergo/otp-encryption](https://forgejo.neoeden.org/ergo/otp-encryption)
---

A tool to encrypt and decrypt files using the simple bitwiseXOR operation with a randomly generated key of equal length to the data to be encrypted. This is the same method as the one time pad but adapted to byte data instead of only encrypting ASCII text.

This encryption method has perfect secrecy however the downside is the key is very big and can only be used once.

There is a CLI tool and a GUI tool, both have the same functionality but a different interface.

![Image1](/image2.png)

![Image2](/image1.png)

![Image3](/image3.png)
