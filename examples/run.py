# pip install apify-client
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("datagrit/ted-contract-expiry-radar").call(run_input={
    "queries": [
        "software"
    ],
    "expiresAfterMonths": 0,
    "expiresBeforeMonths": 12,
    "maxItems": 20
})
items = client.dataset(run["defaultDatasetId"]).list_items().items
print(len(items), "records")
print(items[0] if items else None)
