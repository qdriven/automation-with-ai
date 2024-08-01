from qrpa.news.drission_page_fetcher import scrape_bbc_news


def test_scrape_bbc_news():
    news = scrape_bbc_news()

    # Print the results
    for item in news:
        print(f"Title: {item['title']}")
        print(f"Link: {item['link']}")
        print(f"Summary: {item['summary']}")
        print('---')