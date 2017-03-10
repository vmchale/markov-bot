import markovify
import twitter
import itertools
import argparse

## Command line parser
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('filepath', metavar='CREDENTIALS', type=str, help='an integer for the accumulator')
parser.add_argument('--text', dest='corpus', metavar='CORPUS', type=str, help='path to the text you wish to analyze')
args = parser.parse_args()

## Function to help process credentials file
def drop_tag(str):
    parsed = itertools.dropwhile(lambda x: x!= ':', str)
    str2 = "".join(parsed)
    parsed2 = itertools.dropwhile(lambda x: x == ' ' or x == ':', str2)
    return "".join(parsed2)

## Open file with credentials
with open(args.filepath) as f:
    content = f.readlines()

## Process api keys etc.
content = [drop_tag(x.strip()) for x in content] 

# Get raw text of markov chain as string.
with open(args.corpus) as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# create twitter api object
api = twitter.Api(consumer_key=content[0],
                      consumer_secret=content[1],
                      access_token_key=content[2],
                      access_token_secret=content[3])

# Generate three randomly-generated sentences of no more than 140 characters and tweet them.
selected = False
while selected == False:
    str_potentially = text_model.make_short_sentence(140)
    if not("http" in str_potentially):
        status = api.PostUpdate(str_potentially)
        print(status.text) # verify it worked
        selected = True

