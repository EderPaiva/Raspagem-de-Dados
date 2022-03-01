from tech_news.database import find_news
from operator import itemgetter


# Requisito 10
def top_5_news():
    """Seu código deve vir aqui"""
    popularity = []
    notice_list = find_news()
    # print(notice_list)
    for notice in notice_list:
        notice["popularity"] = notice[
            "shares_count"] + notice["comments_count"]
        popularity.append(notice)

    ordened_by_popularity = sorted(popularity, key=itemgetter(
        "popularity", "title"), reverse=1)
    top_five = ordened_by_popularity[0:5]
    title_and_url = []
    for notice in top_five:
        title_and_url.append((notice["title"], notice["url"]))

    return title_and_url


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
    all_categories = []
    notice_list = find_news()
    for notice in notice_list:
        for category in notice['categories']:
            all_categories.append(category)

    category_ordened = sorted(all_categories)

    if not category_ordened:
        return []
    if len(category_ordened) <= 5:
        return category_ordened
    else:
        return category_ordened[0:5]
