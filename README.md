# python-iam-token-manager

To install the module:

```
pip install -e "git+https://github.com/locke105/python-iam-token-manager#egg=python-iam-token-manager"
```

Using in code:

```python
import bxauth

token_resp = bxauth.auth(apikey="...")
iam_token = token_resp.get('access_token')
```
