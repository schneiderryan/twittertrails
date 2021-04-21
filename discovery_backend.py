import json
from ibm_watson import DiscoveryV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('o2AHBjAYfudK0mXXt7dFmQFx8oaldIae5oG3du2iIf9K')
discovery = DiscoveryV1(
    version='2019-04-30',
    authenticator=authenticator
)

discovery.set_service_url('https://api.us-south.discovery.watson.cloud.ibm.com/instances/beff1375-93ea-4b19-b90a-10fbf38f45fd')

envID = '35ef0ced-f8c5-4f16-a57c-098c66505472'
colID = 'c7bf0198-9e14-40db-9e96-2b4d348585c1'

def getNLQ(tweet: str):
    areaFilter = '(latitude>' + str(eval("40 - .5")) + ',latitude<' + str(eval("40 - (.5) * -1")) + ',longitude>' + str(eval("(83 * 1) - .5")) + ',longitude<' + str(eval("(83 * 1) - (.5 * -1)")) + ')'
    DetailedResponse = discovery.query(environment_id = envID, collection_id = colID, filter = areaFilter, natural_language_query = tweet, count = 10)
    response = json.dumps(DetailedResponse.get_result(), indent = 2)
    response = json.loads(response)
    return response