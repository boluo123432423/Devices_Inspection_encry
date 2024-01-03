import base64
from Crypto.Cipher import AES


def remove_all_null_terminators(byte_data):
    while byte_data.endswith(b'\0'):
        byte_data = byte_data.rstrip(b'\0')
    return byte_data

def add_to_16(message):
    if isinstance(message, str):
        message = message.encode()
    while len(message) % 16 != 0:
        message += b'\0'
        # message = str(message)
    return message  # 返回bytes
# 加密方法
def encrypt_oracle(message,key_pri):
    # 初始化加密器
    #print(type(add_to_16(key_pri)))
    #print(type(AES.MODE_ECB))
    aes = AES.new(add_to_16(key_pri), AES.MODE_ECB)
    # 将明文转为 bytes
    message_bytes = message.encode('utf-8')
    # 长度调整
    message_16 = add_to_16(message_bytes)
    #先进行aes加密
    encrypt_aes = aes.encrypt(message_16)
    #用base64转成字符串形式
    encrypt_aes_64 = base64.b64encode(encrypt_aes)
    return encrypt_aes_64


# 解密方法
# def decrypt_oralce(message,key_pri):
#     # 初始化加密器
#     aes = AES.new(add_to_16(key_pri), AES.MODE_ECB)
#     #优先逆向解密base64成bytes
#     message_de64 = base64.b64decode(message)
#     # 解密 aes
#     message_de64_deaes = aes.decrypt(message_de64)
#     message_de64_deaes = remove_all_null_terminators(message_de64_deaes)
#     message_de64_deaes_de = message_de64_deaes.decode('utf-8')
#     return message_de64_deaes_de

key = input("请输入密钥：")
while 1:
    password = input("输入需要加密的密码：")
    print("加密密文："+encrypt_oracle(password, key).decode())
    # password21 = input("输入需要解密的密码：")
    #print("解密："+decrypt_oralce(encrypt_oracle(password, key), key))
