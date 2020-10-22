import requests, json

def get_pushshift_comments(**kwargs):
    """Gets comments from the beta pushshift ingest api using given parameters.

    kwargs is the payload.
    """
    base_url = 'https://beta.pushshift.io/search/reddit/comments'
    request = requests.get(base_url, params = kwargs)
    return request.json()['data']
