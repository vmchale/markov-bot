import markovify
import argparse
import itertools
import twitter

def parser():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--config', dest='filepath', metavar='CREDENTIALS', type=str, help='Path to config file')
    parser.add_argument('text', metavar='CORPUS', type=str, help='path to the text you wish to mimic') # filepath should be a flag; corpus an argument!
    parser.add_argument('--coke-binge', dest='coke_binge', action="store_true", default=False, help='Tweet excessively/emulate our POTUS') # instead of tweeting once, tweet a random number of times.
    parser.add_argument('-t', dest='test', action="store_true", default=False, help='Test text generation without tweeting.') # distance on markov chains?? distance on syntax trees? 
    return parser.parse_args()

def build_model(text):
    # Get raw text of markov chain as string.
    with open(text) as f:
        text = f.read()

    # Build the model.
    return markovify.Text(text)

def make_tweets(api, test, model, coke_binge_num):
    # Generate three randomly-generated sentences of no more than 140 characters and tweet them.
    selected = False
    for i in range(0, coke_binge_num):
        while selected is False:
            str_potentially = model.make_short_sentence(140)
            if not("http" in str_potentially):
                if not(test):
                    # tweet the generated text
                    status = api.PostUpdate(str_potentially)
                    print(status.text)  # verify it worked
                else:
                    # test mode; just display it
                    print(str_potentially)
                selected = True
        selected = False

# Function to help process credentials file
def drop_tag(str):
    parsed = itertools.dropwhile(lambda x: x!= ':', str)
    str2 = "".join(parsed)
    parsed2 = itertools.dropwhile(lambda x: x == ' ' or x == ':', str2)
    return "".join(parsed2)

# Process api keys etc.
def make_api_keys(filepath):
    # Open file with credentials
    with open(filepath) as f:
        content = f.readlines()
    # Strip irrelevant text
    content = [drop_tag(x.strip()) for x in content]
    # create twitter api object
    return twitter.Api(consumer_key=content[0],
                          consumer_secret=content[1],
                          access_token_key=content[2],
                          access_token_secret=content[3])
