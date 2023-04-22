# VGChartz Link Scraper

This project is a simple web scraper that extracts article links from a list of URLs using the Scrapy framework. The extracted links are then saved in a CSV file. The scraper is built to run concurrently using Python's multiprocessing module.

![image](https://user-images.githubusercontent.com/16968671/233770609-ffa07b7c-5af1-483e-af23-fb7db3763b87.png)

## Installation
1. Clone the repository:
```
git clone https://github.com/yourusername/article-link-scraper.git
```
2. Change into the project directory:
```
cd article-link-scraper
```
3. Create a virtual environment and activate it:
```
python -m venv venv
source venv/bin/activate # On Windows, use venv\Scripts\activate
```
4. Install the required dependencies:
```
pip install -r requirements.txt
```

## Usage
1. Update the `urls` list in the `main` section of the script with the URLs you want to scrape.
2. Run the script:
```
python article_scraper.py
```
3. Check the `article_links.csv` file for the extracted article links.
## License
This project is licensed under the MIT License.

Don't forget to replace `https://github.com/yourusername/article-link-scraper.git` with the actual URL of your GitHub repository.

