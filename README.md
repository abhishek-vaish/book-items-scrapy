# Books to Scrap [Scrapy]
Fetching the data from the Books to Scrap website using the python framework Scrapy and storing the result to the CSV file.

## Project Structure
D:.<br>
│   .gitignore<br>
│   books.csv<br>
│   items.py<br>
│   middlewares.py<br>
│   pipelines.py<br>
│   README.md<br>
│   settings.py<br>
│   __init__.py<br>
│<br>
└───spiders<br>
        &emsp;&emsp;book_scraper.py<br>
        &emsp;&emsp;__init__.py<br>

## Project Setup
```bash
# create virtual environment
> python -m venv venv

# activate virtual environment
> venv\Scripts\activate

# install scrapy framework
> pip install scrapy

# create project
> scrapy startproject <project_name>
```

## Run Command
```bash
> scrapy crawl <spider_name> -o <csv_file>
```