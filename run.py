print("Find out your true colors.")

print("\n")

print("Each letter refers to a set of three words. \nRead the words and describe which of the four letter choices is most like you.")

print("\n")

print("Rank the one that is most like you with a 4. Then rank the next three letter choices from 3-1 in descending preference.")

print("\n")

print("Row One")

print("\n")

print("A: Active, Opportunistic, Spontaneous")
print("B: Parental, Traditional, Responsible")
print("C: authentic, harmonious, compassionate")
print("D: versatile, inventive, competent")

print("\n")

a = input("Rank for A from 4 (most) - 1 (least):")
b = input("Rank for B from 4 (most) - 1 (least):")
c = input("Rank for C from 4 (most) - 1 (least):")
d = input("Rank for D from 4 (most) - 1 (least):")

print("Row Two")

print("\n")

print("E: Curious, Conceptual, Knowledgeable")
print("F: Unique, Empathetic, Communicative")
print("G: Practical, Sensible, Dependable")
print("H: Competitive, Impetuous, Impactful")

print("\n")

e = input("Rank for E from 4 (most) - 1 (least):")
f = input("Rank for F from 4 (most) - 1 (least):")
g = input("Rank for G from 4 (most) - 1 (least):")
h = input("Rank for H from 4 (most) - 1 (least):")

print("\n")

print("Row Three")

print("\n")

print("I: Loyal, Conservative, Organized")
print("J: Devoted, Warm, Poetic")
print("K: Realistic, Open-minded, Adventuresome")
print("L: Theoretical, Seeking, Ingenious")

print("\n")

i = input("Rank for I from 4 (most) - 1 (least):")
j = input("Rank for J from 4 (most) - 1 (least):")
k = input("Rank for K from 4 (most) - 1 (least):")
l = input("Rank for L from 4 (most) - 1 (least):")

print("Row Four")

print("\n")

print("M: Concerned, Procedural, Cooperative")
print("N: Daring, Impulsive, Fun")
print("O: Tender, Inspirational, Dramatic")
print("P: Determined, Complex, Composed")

print("\n")

m = input("Rank for M from 4 (most) - 1 (least):")
n = input("Rank for N from 4 (most) - 1 (least):")
o = input("Rank for O from 4 (most) - 1 (least):")
p = input("Rank for P from 4 (most) - 1 (least):")

print("Row Five")

import operator


print("\n")

print("Q: Philosophical, Principled, Rational")
print("R: Vivacious, Affectionate, Sympathetic")
print("S: Exciting, Courageous, Skillful")
print("T: Orderly, Conventional, Caring")

print("\n")

q = input("Rank for Q from 4 (most) - 1 (least):")
r = input("Rank for R from 4 (most) - 1 (least):")
s = input("Rank for S from 4 (most) - 1 (least):")
t = input("Rank for T from 4 (most) - 1 (least):")

print("\n")

print("Your Results")

print("\n")

orange = a + h + k + n + s
green = b + g + i + m + t
blue = c + f + j + o + r
gold = d + e + l + p + q

print("Your orange number value is: "+str(orange))
print("Your green number value is: "+str(green))
print("Your blue number value is: "+str(blue))
print("Your gold number value is: "+str(gold))


colors = dict() 

colors["orange"] = orange
colors["green"] = green
colors["blue"] = blue
colors["gold"] = gold

max_color = max(colors, key=colors.get)

print("\n")

print("Your color is: " + str(max_color))


