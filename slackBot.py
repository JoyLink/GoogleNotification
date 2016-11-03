from slackclient import SlackClient

SLACK_TOKEN = "ENTER_TOKEN_HERE"

SLACK_CHANNEL = "#googlenotification"


def push_notification(self, notification):

    sc = SlackClient(SLACK_TOKEN)
    desc = "{0} | <{4}>".format(notification["htmlTitle"], notification["link"])
    sc.api_call(
        "chat.postMessage",
        channel=SLACK_CHANNEL,
        text=desc,
        username='pybot',
        icon_emoji=':robot_face:')