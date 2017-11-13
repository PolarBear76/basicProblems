#leet speak translator

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
leetspeakbet = ["4", "8", "(", ")", "3", "}", "6", "#", "!", "]", "X", "|", "M", "N", "0", "9", "Q", "2", "Z", "7", "M", "V", "W", "X", "J", "Z"]

print "Please type what you want translated to leetspeak"
input = str(raw_input()).lower()
output = ""
for x in range(0, len(input)):
    try:
        output += leetspeakbet[alphabet.index(input[x])]
    except:
        output += input[x]
print output
