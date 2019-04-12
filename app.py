import scraper
import analyzeGoogleData


def main():
    print('>>> Scraping GOOGLE...')

    scraper.scrapGoogle('telemedicina')

    print('>>> Analyzing Data...')

    analyzeGoogleData.analyze
    
    print('>>> FINISH. Please check 100.csv and domains.csv')

if __name__ == '__main__':
    main()

