Colour = ["Pink","Brown","Black"]
Hair = ["Bald","Curly hair", "Straight hair","Long hair","Braided hair"]
Accesories = ["Tattoes", "Piercings"]
ball_comb = []

def ball_combinator(iC,iH,iA):
    
    ball_comb.append((Colour[iC],Hair[iH],Accesories[iA]))
    
    if iC != len(Colour)-1:
        iC += 1
        ball_combinator(iC,iH,iA)
    elif iH != len(Hair)-1:
        iC = 0
        iH += 1
        ball_combinator(iC,iH,iA)
    elif iA != len(Accesories)-1:
        iC = 0
        iH = 0
        iA += 1
        ball_combinator(iC,iH,iA)
    return ball_comb
print(list(ball_combinator(0,0,0)))