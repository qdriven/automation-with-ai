from DrissionPage import ChromiumPage
import time

def scrape_bbc_news():
    # Initialize the ChromiumPage
    page = ChromiumPage()

    # Navigate to BBC News
    page.get('https://www.bbc.com/news')

    # Wait for the page to load
    time.sleep(5)

    # Find all news article elements
    articles = page.eles('xpath://div[@data-testid="edinburgh-article"]')

    news_data = []
    for article in articles[:10]:  # Limit to first 10 articles for this example
        try:
            # Extract title
            title = article.ele('xpath:.//h2').text

            # Extract link
            link = article.ele('xpath:.//a').attr('href')
            if not link.startswith('http'):
                link = 'https://www.bbc.com' + link

            # Extract summary (if available)
            summary = article.ele('xpath:.//p[@class="gs-c-promo-summary"]').text
        except:
            # If any element is not found, continue to the next article
            continue

        news_data.append({
            'title': title,
            'link': link,
            'summary': summary
        })

    # Close the browser
    page.quit()

    return news_data

# Run the scraper
