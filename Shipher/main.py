vopr = input('Что вы хотите сделать? \n')
if vopr.lower() == 'расшифровать':
    shipher = input('Какой шифр был использован?\n')
    if shipher.lower() == 'rsa':
        import key_rsa
        decrypt = key_rsa
    elif shipher.lower() == 'aes':
        import AES256_cbc
        der = AES256_cbc
        import key_aes
        decrypt = key_aes

elif vopr.lower() == 'зашифровать':
    shipher = input('Какой шифр вы хотите использовать?\n')
    if shipher.lower() == 'rsa':
        import RSA
        der = RSA
        import crypt_rsa
        encrypt = crypt_rsa
    elif shipher.lower() == 'aes':
        import AES256_cbc
        der = AES256_cbc
        import crypt_aes
        shipher = crypt_aes
