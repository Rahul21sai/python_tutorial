#creating the command line utility


import argparse
import requests


def download(url, loc):
    loc = url.split('/')[-1]
    #note the stream = True parameter below
    with requests.get(url,stream= True) as r:
        r.raise_for_status()
        with open(loc, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return loc
parser = argparse.ArgumentParser()

#add command line arguments
parser.add_argument("url",help="Url of the file to download")
parser.add_argument("output",help="by which name do you want to save your file")

#prase the arguments
args = parser.parse_args()

#use the arguments in your code
print(args.url)
print(args.output)
download(args.url,args.output)

#running the program
# python paste the url link and add file name

