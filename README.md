# Wiki-Scrapper

Wiki Scrapper is created to extract data from wikipedia using Media Wiki API, Wikipedia Library and Wikipedia-API Library.

## Walkthrough
- First I created a list of all the queries to search wikipedia. 
- Then I used Wikipedia library's .search() method to get first 20 wikipedia titles for all the queries in the list.
- Titles is a list of 20 titles and there are 21 queries to search. So the "for loop" worked for 420 times.
- Every time it takes a title and extracts all the required info like text, images and links.
- Finally I added all the data to a list.
