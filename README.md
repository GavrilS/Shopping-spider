# Shopping-spider
A spider to gather shopping prices on products of interest.

# Set up
- Set up virtual environment:
    pip install virtualenv / apt install python3.8-venv
    python3 -m venv env??
- Activate virtual environment:
    source env/bin/activate
    To deactivate later you can use 'deactivate' in shell
- Add env folder to gitignore if not already there!!!
- Install scrapy: pip install scrapy

# Scrapy commands
- Using the shell: 
    scrappy shell
- Create a project:
    scrapy startproject <name-of-project>
- Create a spider(from within the project folder):
    scrapy genspider <name-of-spider>
- Run the spider:
    scrapy crawl <name-of-spider> (-a search=search)
