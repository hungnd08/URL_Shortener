#Import the library that we defined
import url_shortener
import sys

#Opening the file that contains URLs
url_file = open(sys.argv[1], 'r')

#Reading all the URLs line-by-line
lines = url_file.readlines()

#Opening the file in which we will write the shortened URLs
url_file_shortened = open(r"url_file_shortened.txt", "w+")

#Shortening each URL, printing n console and writing them in a text
for url in lines:
    url_short = url_shortener.make_shorten(url.strip('\n'))
    print(url_short)
    url_file_shortened.write(url_short)
    url_file_shortened.write("\n")

#Closing both the files
url_file.close()
url_file_shortened.close()