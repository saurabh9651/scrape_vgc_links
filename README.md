# VGChartz Link Scraper

This project is a simple web scraper that extracts article links from a list of URLs using the Scrapy framework. The extracted links are then saved in a CSV file. The scraper is built to run concurrently using Python's multiprocessing module.

Check out full tutorial on [Medium](https://medium.com/@saurabhpatel.sjpco/scrapy-tutorial-extracting-article-links-with-multiprocessing-a4df13969b68?)

![image](https://user-images.githubusercontent.com/16968671/233770609-ffa07b7c-5af1-483e-af23-fb7db3763b87.png)

## Installation
1. Clone the repository:
```
git clone https://github.com/saurabh9651/scrape_vgc_links.git
```
2. Change into the project directory:
```
cd scrape_vgc_links
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

## Output
Create a `article_links.csv` file that contains URLs of all articles on VGChartz. It contians a header "Article Links".

### Applications of output data
1. URL validation check
2. Article content scraping

## License
This project is licensed under the MIT License.


