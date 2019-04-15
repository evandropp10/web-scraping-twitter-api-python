import scraper
import analyzeData
import extractorTwitter


def main():
    
    print('>>> Scraping GOOGLE...')
    scraper.scrapGoogle('telemedicina')

    print('>>> Analyzing Google Data...')
    analyzeData.analyzeGoogle()
    print('>>> FINISH. Please check 100.csv and domains.csv')
    
    print('>>> Extracting Twitter Data...')
    extractorTwitter.queryTwitter('telemedicina')
    
    print('>>> Analyzing Twitter Data...')
    analyzeData.analyzeTwitter()
    print('>>> FINISH. Please check Google_100.csv, Google_domains.csv, Twitter_users.csv, Twitter_dayweek.csv and Twitter_hour.csv')
    

if __name__ == '__main__':
    main()

