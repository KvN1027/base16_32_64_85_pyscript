import base64 

def decode_all(words):
    ## base 16
    try :
        print('b16 => ',base64.b16decode(str(words)))
    except: 
        print('base16 err')
    ## base 32
    try :
        print('b32 => ',base64.b32decode(str(words)))
    except: 
        print('base32 err')
    ## base 64
    try :
        print('b64 => ',base64.b64decode(str(words)))
    except: 
        print('base64 err')
    ## base 85
    try :
        print('b85 => ',base64.b85decode(str(words)))
    except: 
        print('base85 err')
    

flag = 'IZGECR33IRXSA6LPOUQGW3TPO4QGEYLTMUZTEIDFNZRW6ZDJNZTT67I='

decode_all(flag)
