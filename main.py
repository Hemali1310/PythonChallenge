alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
data = input("Type encrypt for encryption and decrypt for decreption: ")
paintext = input("Enter text to encrypt: ").lower()
shift = int(input("Type shift number: "))

def ceasercipher(starttext, shift, direction):
  encryptedtext = ""
  if direction == 'decrypt':
    shift *= -1
  for i in starttext:
    place = alphabets.index(i)
    newplace = place + shift
    encryptedtext += alphabets[newplace]
  print(encryptedtext)
    
ceasercipher(paintext, shift, data)

# def encryption(plaintexts, shifts):
#   for i in plaintexts:
#     data = alphabets.index(i)
#     shiftdata = data + shifts
#     encryptedtext = alphabets[shiftdata]
#     print(encryptedtext)   

# def decryption(encryptedtext, shifts):
#   for i in encryptedtext:
#     data = alphabets.index(i)
#     shiftdata = data - shifts
#     decryptedtext = alphabets[shiftdata]
#     print(decryptedtext)

# encryption(paintext, shift)
# encryptedtext = input("Enter text to decrypt: ").lower()
# decryption(encryptedtext, shift)
# # print(encryptedtext)
