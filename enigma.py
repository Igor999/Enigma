import re
def enigma(text, ref, rot1, shift1, rot2, shift2, rot3, shift3):
    text = text.upper()
    rotor0 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rotor1 = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"
    rotor2 = "AJDKSIRUXBLHWTMCQGZNPYFVOE"
    rotor3 = "BDFHJLCPRTXVZNYEIWGAKMUSQO"
    reflectorB = {"A":"Y", "Y":"A","B":"R","R":"B","C":"U","U":"C","D":"H","H":"D","E":"Q","Q":"E","F":"S","S":"F","G":"L","L":"G","I":"P","P":"I","J":"X","X":"J","K":"N","N":"K","M":"O","O":"M","T":"Z","Z":"T","V":"W","W":"V" }
    result = ""
    res_text = re.sub(r'[^A-Z]', '', text)
    if rot1==0 and rot2==0 and rot3==3:
        for i in res_text:
            symbol = i
            ind = rotor0.index(i)+shift3
            symbol = rotor3[ind]
            ind = rotor0.index(symbol)-shift3
            symbol = rotor0[ind]
            if ref==1:
                symbol = reflectorB[symbol]
            ind = rotor0.index(symbol)+shift3
            symbol = rotor0[ind]
            ind = rotor3.index(symbol)-shift3
            symbol = rotor0[ind]            
            result += symbol
        return result
    elif rot1==1 and rot2==0 and rot3==0:
        for i in res_text:
            symbol = i
            ind = rotor0.index(i)+shift1
            symbol = rotor1[ind]
            ind = rotor0.index(symbol)-shift1
            symbol = rotor0[ind]
            if ref==1:
                symbol = reflectorB[symbol]
            ind = rotor0.index(symbol)+shift1
            symbol = rotor0[ind]
            ind = rotor1.index(symbol)-shift1
            symbol = rotor0[ind]            
            result += symbol
        return result
    elif rot1==0 and rot2==2 and rot3==0:
        for i in res_text:
            symbol = i
            ind = rotor0.index(i)+shift2
            symbol = rotor2[ind]
            ind = rotor0.index(symbol)-shift2
            symbol = rotor0[ind]
            if ref==1:
                symbol = reflectorB[symbol]
            ind = rotor0.index(symbol)+shift2
            symbol = rotor0[ind]
            ind = rotor2.index(symbol)-shift2
            symbol = rotor0[ind]            
            result += symbol
        return result
    
    elif rot1==1 and rot2==2 and rot3==0:
        for i in res_text:
            symbol = i
            ind = rotor0.index(i)+shift2
            if ind>len(rotor0)-1:
                ind = ind-len(rotor0)
            symbol = rotor0[ind]
            symbol = rotor2[ind]
            ind = rotor0.index(symbol)
            ind = ind + (shift1-shift2)
            if ind > len(rotor0)-1:
                ind = ind - len(rotor0)
            symbol = rotor0[ind]
            symbol = rotor1[ind]
            ind = rotor0.index(symbol)
            ind = ind-shift1
            if ind > len(rotor0)-1:
                ind = ind - len(rotor0)
            symbol = rotor0[ind]
            symbol = rotor1[ind]
           
            if ref == 1:
                symbol = reflectorB[symbol]
               
            ind = rotor0.index(symbol)
            ind = ind+shift1
            if ind > len(rotor0)-1:
                ind = ind - len(rotor0)
            symbol = rotor0[ind]
           
            ind = rotor1.index(symbol)
            symbol = rotor1[ind]
            symbol = rotor0[ind]
            ind = ind-(shift1-shift2)
            if ind > len(rotor0)-1:
                ind = ind - len(rotor0)
            symbol = rotor2[ind]
            symbol = rotor0[ind]
            ind = rotor2.index(symbol)
            ind = ind-shift2
            if ind > len(rotor0)-1:
                ind = ind-len(rotor0)
            symbol = rotor0[ind]
            result += symbol
        return result
    
    elif rot1==1 and rot2==0 and rot3==3:
        for i in res_text:
            symbol = i
            ind = rotor0.index(i)+shift3
            if ind>len(rotor0)-1:
                ind = ind-len(rotor0)
            symbol = rotor0[ind]
            symbol = rotor3[ind]
            ind = rotor0.index(symbol)
            ind = ind + (shift1-shift3)
            if ind > len(rotor0)-1:
                ind = ind - len(rotor0)
            symbol = rotor0[ind]
            symbol = rotor1[ind]
            ind = rotor0.index(symbol)
            ind = ind-shift1
            if ind > len(rotor0)-1:
                ind = ind - len(rotor0)
            symbol = rotor0[ind]
            symbol = rotor1[ind]
           
            if ref == 1:
                symbol = reflectorB[symbol]
               
            ind = rotor0.index(symbol)
            ind = ind+shift1
            if ind > len(rotor0)-1:
                ind = ind - len(rotor0)
            symbol = rotor0[ind]
           
            ind = rotor1.index(symbol)
            symbol = rotor1[ind]
            symbol = rotor0[ind]
            ind = ind-(shift1-shift3)
            if ind > len(rotor0)-1:
                ind = ind - len(rotor0)
            symbol = rotor3[ind]
            symbol = rotor0[ind]
            ind = rotor3.index(symbol)
            ind = ind-shift3
            if ind > len(rotor0)-1:
                ind = ind-len(rotor0)
            symbol = rotor0[ind]
            result += symbol
        return result
    
    elif rot1==0 and rot2==2 and rot3==3:
        for i in res_text:
            symbol = i
            ind = rotor0.index(i)+shift3
            if ind>len(rotor0)-1:
                ind = ind-len(rotor0)
            symbol = rotor0[ind]
            symbol = rotor3[ind]
            ind = rotor0.index(symbol)
            ind = ind + (shift2-shift3)
            if ind > len(rotor0)-1:
                ind = ind - len(rotor0)
            symbol = rotor0[ind]
            symbol = rotor2[ind]
            ind = rotor0.index(symbol)
            ind = ind-shift2
            if ind > len(rotor0)-1:
                ind = ind - len(rotor0)
            symbol = rotor0[ind]
            symbol = rotor2[ind]
           
            if ref == 1:
                symbol = reflectorB[symbol]
               
            ind = rotor0.index(symbol)
            ind = ind+shift2
            if ind > len(rotor0)-1:
                ind = ind - len(rotor0)
            symbol = rotor0[ind]
           
            ind = rotor2.index(symbol)
            symbol = rotor2[ind]
            symbol = rotor0[ind]
            ind = ind-(shift2-shift3)
            if ind > len(rotor0)-1:
                ind = ind - len(rotor0)
            symbol = rotor3[ind]
            symbol = rotor0[ind]
            ind = rotor3.index(symbol)
            ind = ind-shift3
            if ind > len(rotor0)-1:
                ind = ind-len(rotor0)
            symbol = rotor0[ind]
            result += symbol
        return result
    elif rot1==0 and rot2==0 and rot3==0:
        for i in res_text:
            symbol = i
            
            if ref == 1:
                symbol = reflectorB[symbol]
                
            ind = rotor0.index(symbol)
            
            symbol = rotor0[ind]
            result += symbol
        return result
    #elif rot1==1 and rot2==2 and rot3==3:
    else:
        for i in res_text:
            symbol = i
            ind = rotor0.index(i)+shift3
            if ind>len(rotor0)-1:
                ind = ind-len(rotor0)
            symbol = rotor0[ind]
            symbol = rotor3[ind]
            ind = rotor0.index(symbol)
            ind = ind + (shift2-shift3)
            if ind > len(rotor0)-1:
                ind = ind - len(rotor0)
            symbol = rotor0[ind]
            symbol = rotor2[ind]
            ind = rotor0.index(symbol)
            ind = ind+(shift1-shift2)
            if ind > len(rotor0)-1:
                ind = ind - len(rotor0)
            symbol = rotor0[ind]
            symbol = rotor1[ind]
            ind = rotor0.index(symbol)
            ind = ind - shift1
            if ind > len(rotor0)-1:
                ind = ind - len(rotor0)
            symbol = rotor0[ind]
            
            if ref == 1:
                symbol = reflectorB[symbol]
            ind = rotor0.index(symbol)
            ind = ind+shift1
            if ind > len(rotor0)-1:
                ind = ind - len(rotor0)
            symbol = rotor0[ind]
           
            ind = rotor1.index(symbol)
            symbol = rotor1[ind]
            symbol = rotor0[ind]
            ind = ind-(shift1-shift2)
            if ind > len(rotor0)-1:
                ind = ind - len(rotor0)
            symbol = rotor2[ind]
            symbol = rotor0[ind]
            ind = rotor2.index(symbol)
            ind = ind-(shift2-shift3)
            if ind > len(rotor0)-1:
                ind = ind-len(rotor0)
            symbol = rotor3[ind]
            symbol = rotor0[ind]
            ind = rotor3.index(symbol)
            ind = ind-shift3
            if ind > len(rotor0)-1:
                ind = ind-len(rotor0)
            symbol = rotor0[ind]
            result += symbol
        return result
