from googleapiclient.discovery import build
from filter import do_filter
from slackBot import push_notification
from parameters import MY_API_KEY, MY_CSE_ID




def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res['items']

def do_search(key_word):
    results = google_search(
        key_word, MY_API_KEY, MY_CSE_ID, num=10)

    filteredresults = do_filter(results)

    if filteredresults:
        push_notification(filteredresults)
    # for result in results:
    #     pprint.pprint(result)