# encoding: utf-8
import sys, re, json
from bs4 import BeautifulSoup
reload(sys) 
sys.setdefaultencoding('utf8')


filename = sys.argv[1]
review_objects = []

print("Reading Data from {}...".format(filename))
with open(filename, 'r') as reviews_html:
   reviews_html_string = reviews_html.read()

reviews_html_soup = BeautifulSoup(reviews_html_string, 'html.parser', from_encoding='utf-8')
# print(reviews_html_soup.prettify('utf-8'))
reviews_html_soup = reviews_html_soup.find_all('div', class_='ui segments res-review-body res-review clearfix item-to-hide-parent js-activity-root stupendousact feedroot res-review')
review_count = len(reviews_html_soup)
print("Found {} Reviews.".format(review_count))
for review_html_soup in reviews_html_soup:
   restaurant_location = review_html_soup.find('div', class_='res-review-header') \
                                         .find('div', class_='mb5') \
                                         .find('span', class_='grey-text fontsize5') \
                                         .get_text(strip=True)
   restaurant_soup = review_html_soup.find('div', class_='res-review-header') \
                                     .find('div', class_='mb5') \
                                     .find('a', class_='res_name')
   restaurant_name = restaurant_soup.get_text(strip=True)
   restaurant_url = restaurant_soup.get('href')
   review_meta_soup = review_html_soup.find('div', class_='res-review-header') \
                                      .find('div', class_='mb5 clearfix') \
                                      .find('a', class_='res-review-date fontsize5')
   review_url = review_meta_soup.get('href')
   review_timestamp = review_meta_soup.find('time').get('datetime')
   review_text_soup = review_html_soup.find('div', class_='res-review-body') \
                                      .find('div', class_='res-review-body res-review-small clearfix') \
                                      .find('div', class_='rev-text')
   review_rating = review_text_soup.select('div.ttupper.fs12px.left.bold.zdhl2.tooltip')[0] \
                                   .get('aria-label') \
                                   .replace('Rated ', '')
   review_text = review_text_soup.find_all(text=True, recursive = False)
   review_text = "\n".join(text.strip() for text in review_text).strip()
   
   try:
      restaurant_response_soup = review_html_soup.find('div', class_='plr15 ui secondary segment pt0 pb0 brbot') \
                                                 .find('div', class_='plr15 pt0 pb5 brbot review-replies-thread-root clearfix ui secondary segment remove-segment-border') \
                                                 .find('div', class_='review-replies-container mtop') \
                                                 .find('div', class_='review-replies-item comment') \
                                                 .find('div', class_='review-reply-text zblack content')
      restaurant_response_author = restaurant_response_soup.find('div', class_='author').get_text(strip=True)
      restaurant_response_text = restaurant_response_soup.find('div', class_='text').get_text(strip=False).strip().replace("\t","")
   except:
      restaurant_response_author = None
      restaurant_response_text = None

   review_object = {
      "restaurant_url"        : restaurant_url,
      "restaurant_location"   : restaurant_location,
      "restaurant_name"       : restaurant_name,
      "review_rating"         : review_rating,
      "review_text"           : review_text,
      "review_timestamp"      : review_timestamp,
      "review_url"            : review_url,
      "response_author"       : restaurant_response_author,
      "response_text"         : restaurant_response_text
   }
   review_objects.append(review_object)
   review_count -= 1

with open("reviews.json", 'w') as output_json_file:
    output_json_file.write(json.dumps(review_objects, indent=4, sort_keys=True))
