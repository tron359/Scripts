def main():
    print(shorten(input("text: ")))

def shorten(text):
    letters = ["a","e","i","o","u"]
    ltext = []
    for x in text:
        lx = x.lower() #create separate list containing lowered version
        if lx not in letters: #check if lowered -Doesn't- match target list
            ltext += x #if lowered DOESN'T match list, add the original to a new list
            #if lx IS in letters, then we do nothing with, effectively discarding it
    stext=''.join(ltext) #since we only added non-matches, this list has no vowels
    return stext

if __name__ == "__main__":
    main()
