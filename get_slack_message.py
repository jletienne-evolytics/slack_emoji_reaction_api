import yaml
import slack_sdk
from slack_sdk.errors import SlackApiError
import logging
import json


slack_token = yaml.safe_load(open('config.yaml'))['slack_token']
client = slack_sdk.WebClient(token=slack_token)

print(client)

channel_name = "abc"
conversation_id = None


channel_id = 'abc'
result = client.conversations_history(channel=channel_id)

x = result.data

# returns slack message as json
print(x['messages'][0])