def inverse(a, n):
    t = 0
    newT = 1
    r = n
    newR = a
    while newR != 0:
        quotient = r // newR
        t, newT = newT, t - quotient * newT
        r, newR = newR, r - quotient * newR

    if r > 1:
        print("a isn't invertible")
    if t < 0:
        t = t + n
    return t


class PrivateSide:
    def __init__(self):
        self.a = [2, 5, 18, 26, 82, 135, 280]  # privateKey
        self.q = 1209
        self.r = 1003
        self.r1 = inverse(self.r, self.q)

    def generatePublicKey(self):
        b = []
        for i in range(len(self.a)):
            b.append(self.r * self.a[i] % self.q)
        return b

    def decrypt(self, value):  # convert 2074 back to A
        # get the converted sum
        newSum = value * self.r1 % self.q  # the new sum is 142
        str1 = ''  # used to hold the binary form of the decrypted value
        for i in range(len(self.a) - 1, -1, -1):
            if newSum >= self.a[i]:
                newSum = newSum - self.a[i]
                str1 = '1' + str1
            else:
                str1 = '0' + str1

    # convert binary to int
        dec_val = int(str1, 2)
        char_val = chr(dec_val)
        return char_val


class PublicSide:
    def __init__(self):
        self.b = []

    def takeInPublicKey(self, a):
        self.b = a

    def encrypt(self, char):  # convert A into 2074
        ascii_code = ord(char)  # when char is A, ascii = 65
        bin_code = bin(ascii_code)[2:]  # when ascii = 65 -- binary is 1000001
        while len(bin_code) < 7:  # we need to append 0s to the head of the string
            bin_code = '0' + bin_code
        result = 0
        for i in range(len(bin_code)):
            if bin_code[i] == '1':
                result = result + self.b[i]
        return result


class TestEncryption:
    def __init__(self):
        self.encryption = PublicSide()
        self.decryption = PrivateSide()
        self.encryption.takeInPublicKey(self.decryption.generatePublicKey())
        self.inputText = ''

    def setInput(self, text):
        self.inputText = text

    def cipher(self):
        result = []
        for char in self.inputText:
            encrypted_number = self.encryption.encrypt(char)
            result.append(encrypted_number)
        return result

    def decipher(self, cipherList):
        result = ''
        for num in cipherList:
            result = result + self.decryption.decrypt(num)
        return result


p = PrivateSide()
b = PublicSide()
b.takeInPublicKey(p.generatePublicKey)

test = TestEncryption()
test.setInput("Have I not commanded you? Be strong and courageous. Do not be afraid; do not be discouraged, "
              "for the Lord your God will be with you wherever you go.")
ciphered = test.cipher()
print(ciphered)
plainText = test.decipher(ciphered)
print(plainText)
