from phishing import *
with open('domain-names_opensquat.txt', encoding='utf-8') as body_to_ban :
    bodyban_brute = body_to_ban.readlines()    
    bodyban_clean = []
    for i in bodyban_brute :
        clean = "" 
        for x in i :
            if x == '.' :
                break
            else :
                clean += str(x)
        bodyban_clean.append(str(clean))
    print(bodyban_clean)
    