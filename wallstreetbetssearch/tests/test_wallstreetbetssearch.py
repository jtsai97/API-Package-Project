from wallstreetbetssearch import wallstreetbetssearch

import pandas as pd
df = pd.read_csv('posts.csv')

def test_post_search():
    keyword = 'invest'
    expected = 17
    actual = wallstreetbetssearch.post_search(keyword,df).index[0]
    assert actual == expected
