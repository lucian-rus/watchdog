# activate the environment
. venv/bin/activate
# install pip depdenencies

# cd scraper
cd watchdog
# run watchdog / groups -> results in the output/groups.csv file
scrapy crawl groups

# run watchdog / members -> results in the output/members.csv file
scrapy crawl members

# run data collection
scrapy crawl data

