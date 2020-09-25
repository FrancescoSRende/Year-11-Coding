#this one takes a band name and a genre, then looks at the band's wikipedia page
#to tell you if the band is that genre

#pre-condition: string inputs, valid band and genre names

import wikipedia

print("Please ensure you have proper capitalization of band names and genres.\n")

def genreTool(band,genre):

    page = wikipedia.page(band)




print('genreTool')
print(genreTool('Converge (band)','metalcore'))



print("")