# pinterest_api
Pinterest API using Python3

----------
## Installation

### Setup

Simply run setup.py to check if there is dependencies missing for you to use API

### Dependencies

`requests` and  `pip`

# Quick Guide

## Before using

### ACCESS TOKEN
Go on [Pinterest Token page]("https://developers.pinterest.com/tools/access_token/") to get your access token and put it at `config.py`

### Functions
All functions are all correspond to each different functionality that [Pinterest API]("https://developers.pinterest.com/docs/api/users/") provides.
Functions are also sorted in that order in `pinterest_api.py`. If function seems to be missing, that is because that function was redundant.
All function returns a requests object, for more documentation, please look at [requests documentation page]("http://docs.python-requests.org/en/master/user/quickstart/#")

### Sample Use
```
  import pinterest_api

  p = Pinterest()

  current_user_info = p.get_current_user()
  current_user_board = p.get_current_user_board()

  id = current_user_info.json()["data"]["id"]
```

# License

MIT

## Legal

This code is in no way affiliated with, authorized, maintained, sponsored or endorsed by Pinterest or any of its affiliates or subsidiaries. This is an independent and unofficial API. Use at your own risk.
