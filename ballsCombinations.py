skin_colour = ["Pink skin","Brown skin","Black skin"]
hair = ["Bald","Curly hair", "Straight hair","Long hair","Braided hair"]
hair_colour = ["Brown hair","Blond hair"]
accesories = ["Tattoes", "Piercings"]
ball_comb = []

def ball_combinator(iSC,iH,iHC,iA):
    
    ball_comb.append((skin_colour[iSC],hair[iH],hair_colour[iHC],accesories[iA]))
    
    if iSC != len(skin_colour)-1:
        iSC += 1
        ball_combinator(iSC,iH,iHC,iA)
    elif iH != len(hair)-1:
        iSC = 0
        iH += 1
        ball_combinator(iSC,iH,iHC,iA)
    elif iHC != len(hair_colour)-1:
        iSC = 0
        iH = 0
        iHC += 1
        ball_combinator(iSC,iH,iHC,iA)
    elif iA != len(accesories)-1:
        iSC = 0
        iH = 0
        iHC = 0
        iA += 1
        ball_combinator(iSC,iH,iHC,iA)
    return ball_comb
print(list(ball_combinator(0,0,0,0)))