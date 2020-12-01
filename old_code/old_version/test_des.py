import des

def test_encrypt_raw_int():
    d = des.DES()

    # http://extranet.cryptomathic.com/descalc/index?key=0e329232ea6d0d73&iv=0000000000000000&input=0123456789ABCDEF&mode=ecb&action=Encrypt&output=31AA59FEB64386A6
    # Same key and msg from the website produce 
    website_enc_msg = 0x31AA59FEB64386A6

    key = 0x0e329232ea6d0d73
    int_msg = 0x0123456789ABCDEF
    int_enc_msg = d.encrypt(int_msg, key)

    assert  int_enc_msg == website_enc_msg, "these should be the same!"


def test_if_encrypt_decrypt_produces_same():
    d = des.DES()
    msg = "test"
    hex_msg = msg.encode()
    int_msg = int.from_bytes(hex_msg, byteorder="big")

    key = 0x0e329232ea6d0d73 
    
    int_enc_msg = d.encrypt(int_msg, key)
    int_dec_msg = d.encrypt(int_enc_msg, key, decrypt = True)

    assert  int_msg == int_dec_msg, "these should be the same!"