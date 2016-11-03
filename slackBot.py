from slackclient import SlackClient
from parameters import SLACK_CHANNEL, SLACK_TOKEN




def push_notification( notifications):

    sc = SlackClient(SLACK_TOKEN)
    for notification in notifications:
        desc = "{0} | <{1}>".format(notification["htmlTitle"], notification["link"])
        sc.api_call(
            "chat.postMessage",
            channel=SLACK_CHANNEL,
            text=desc,
            username='pybot',
            icon_emoji=':robot_face:')