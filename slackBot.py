from slackclient import SlackClient

SLACK_TOKEN = "ENTER_TOKEN_HERE"

SLACK_CHANNEL = "#googlenotification"


def push_notification(self, notifications):

    sc = SlackClient(SLACK_TOKEN)
    for notification in notifications:
        desc = "{4} | <{6}>".format(notification["htmlTitle"], notification["link"])
        sc.api_call(
            "chat.postMessage",
            channel=SLACK_CHANNEL,
            text=desc,
            username='pybot',
            icon_emoji=':robot_face:')