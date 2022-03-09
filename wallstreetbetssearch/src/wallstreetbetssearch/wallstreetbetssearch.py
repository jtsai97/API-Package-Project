def get_results(limit_only,token):
    """
    This function to obtain posts from WallStreetBets subreddit. 
    Parameters: limit_only - the maximum number of items to return. 
    Typical example: 
    |subreddit      |title                     |selftext             |upvote_ratio|ups  |downs|score|created_utc
    |wallstreetbets |Daily Discussion Thread...|Your daily trading...|0.90        |245.0|0.0  |245.0|2021-12-16T06:00:12Z
    """
    requests.get('https://oauth.reddit.com/api/v1/me.json', headers=headers)
    if limit_only == limit_only:
        limit = limit_only
    response = requests.get('https://www.reddit.com/r/wallstreetbets/hot.json',
                headers=headers,params={'limit':limit})
    print(response)
    df = pd.DataFrame()
    for post in r.json()['data']['children']:
        df = df.append({
            'subreddit': post['data']['subreddit'],
            'title': post['data']['title'],
            'selftext': post['data']['selftext'],
            'upvote_ratio': post['data']['upvote_ratio'],
            'ups': post['data']['ups'],
            'downs': post['data']['downs'],
            'score': post['data']['score'],
            'created_date': datetime.fromtimestamp(post['data']['created_utc']).strftime('%Y-%m-%d'),
        },ignore_index=True)
    return df

def post_search(keyword, df):
    """
    This function is primarily used to search for keywords within posts. 
    Parameters: keyword - the function will search for the keyword in the title and post's text, df - the dataframe used.
    Typical example:
    |subreddit     |title                         |selftext                         |upvote_ratio|ups  |downs|score|created_utc
    |wallstreetbets|Are you buying the Reddit ipo?|Are you buying the Reddit ipo?...|0.91        |903.0|0.0  |903.0|2021-12-16T08:48:49Z
    """
    search = '|'.join(keyword)
    df = df[(df['title'].str.lower().str.contains(keyword,na=False))|(df['selftext'].str.lower().str.contains(keyword,na=False))]
    return df

def upvotes_search(low, high, df):
    """
    This function will search for posts with a certain number of upvotes that are between the given parameter. 
    Parameters: low/high - the number of upvotes should between these two numbers, df - the dataframe used. 
    Typical example: 
    |subreddit     |title                     |selftext                               |upvote_ratio|ups  |downs|score|created_utc
    |wallstreetbets|Daily Discussion Thread...|Your daily trading discussion thread...|0.90        |245.0|0.0  |245.0|2021-12-16T06:0012Z
    """
    try:
        if low < 0: raise Error()
        if high < 0: raise Error()
        if high < low: raise Error()
        else:
            df = df[df['ups'].between(low,high)]
            return df
    except: 
        print('Please input different values.')
        pass

def upvote_ratio(low,high,df):
    """
    This function will search for posts with a certain ratio of upvotes that are between the given parameter. 
    Parameters: low/high - the ratio should be between these two numbers, df - the dataframe used. 
    """
    try:
        if low < 0 or low > 1: raise Error()
        if high < 0 or high > 1: raise Error()
        if high < low: raise Error()
        else:
            df = df[df['upvote_ratio'].between(low,high)]
            return df
    except: 
        print('Please input different values.')
        pass
