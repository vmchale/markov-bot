import argparse

def parser() =
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--config', dest='filepath', metavar='CREDENTIALS', type=str, help='Path to config file')
    parser.add_argument('text', metavar='CORPUS', type=str, help='path to the text you wish to mimic') # filepath should be a flag; corpus an argument!
    parser.add_argument('--coke-binge', dest='coke_binge', action="store_true", default=False, help='Tweet excessively/emulate our POTUS') # instead of tweeting once, tweet a random number of times.
    parser.add_argument('-t', dest='test', action="store_true", default=False, help='Test text generation without tweeting.') # distance on markov chains?? distance on syntax trees? # default to test or default to tweet??
    return parser.parse_args()

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
    let content = [drop_tag(x.strip()) for x in content]
    # create twitter api object
    return twitter.Api(consumer_key=content[0],
                          consumer_secret=content[1],
                          access_token_key=content[2],
                          access_token_secret=content[3])
