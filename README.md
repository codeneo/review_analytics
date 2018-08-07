# Review Analytics

## Overview
In this project we gather data from a website that has reviews for restaurants. This dataset has the following features:

- **restaurant_name**: The name of the restaurant.
- **restaurant_location**: The location of the restaurant.
- **restaurant_url**: The url of the restaurant. Additional information about the restaurant, if any, can be gathered from here.
- **review_rating**: A floating point rating for the said restaurant.
- **review_timestamp**: The published timestamp for the said review.
- **review_text**: The review for the said restaurant.
- **review_url**: The url of the review. Additional information, if any, can be gathered from here.
- **response_author**: The owner of the feedback for the said review.
- **response_text**: The feedback for the said review.

## Dependencies
This project is written in Python 2.7, however it should run on Python 3 as well. Apart from **bs4** all the libraries used **(sys, re, json)** are part of the python environment.

## Preparing the data

### Steps to prepare reviews.html
- Since this script does not operate live, scroll down and load all the reviews.
- Copy the element and it's child elements with xpath: `//*[@id="reviews-container"]`.
- Save it to `reviews.html`.

### Run the script
In a terminal or command window, execute `parse_reviews.py reviews.html` to get `reviews.json` with the structure defined above.

## Some insights
- What is the median of rating?
- Which is the most frequently visited locality?
- Which is the most frequently visited restaurant?
- What is the most frequent time of visit?

These are some of the few easily available insights. However with NLP we could have sentiment analysis. Moreover we could possibly recommend restaurants based on factor driving a good experience.
