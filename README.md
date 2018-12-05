# python-iam-token-manager

To install the module:

```
pip install -e "git+https://github.com/locke105/python-iam-token-manager#egg=python-iam-token-manager"
```

Using in code:

```python
import bxauth

# use a TokenManager to automagically refresh/get on expiration
token_manager = bxauth.TokenManager(api_key="...")
iam_token = token_manager.get_token()

# basic token getting, doesn't take care of refreshing
token_resp = bxauth.auth(apikey="...")
iam_token = token_resp.get('access_token')
```
