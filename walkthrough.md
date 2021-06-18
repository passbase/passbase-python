1. Add Passbase's SDK package to your requirements.txt. The SDK should work on both python 2.7 and 3+

```sh
pip install passbase && pip freeze | grep passbase >> requirements.txt
```

2. Import the required modules into your code

```python
import passbase
from pprint import pprint

configuration = passbase.Configuration()
configuration.api_key["X-API-KEY"] = "{{YOUR_SECRET_API_KEY}}"
api_client = passbase.ApiClient(configuration)
api_instance = passbase.IdentityApi(api_client)

try:
    # Get project settings
    api_response = api_instance.get_identity_by_id("<uuid>")
    pprint(api_response)

except Exception as e:
    print("Exception when calling IdentityApi->get_identity_by_id: %s\n" % e)

```
