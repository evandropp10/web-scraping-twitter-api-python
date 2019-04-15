import scraper
import analyzeGoogleData
import extractorTwitter


def main():
    print('>>> Scraping GOOGLE...')
    scraper.scrapGoogle('telemedicina')

    print('>>> Analyzing Data...')
    analyzeGoogleData.analyze()
    print('>>> FINISH. Please check 100.csv and domains.csv')

    print('>>> Extracting Twitter Data...')
    extractorTwitter.queryTwitter('telemedicina')

if __name__ == '__main__':
    main()

