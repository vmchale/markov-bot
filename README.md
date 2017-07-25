# Trump Markov Chain Twitter Bot

Written in python with the aid of markovify and python-twitter.

## Install

`python setup.py install`

## Use

Put your API keys in a file (e.g. .api-keys-trump) like so:

```
api-key: API_KEY
api-sec: API_SECRET_KEY
tok:     TOKEN
tok-sec: SECRET_TOKEN
```

Then run:

```
python bin/markovbot.py PATH_TO_API_KEYS --text PATH_TO_CORPUS.txt
```

to send one tweet at a time. 
