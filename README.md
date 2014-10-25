Zaremba Alex
========================================================================================================================

DataCrawler - Search Engine System based on Django  infrastructure.

------------------------------------------------------------------------------------------------------------------------

- Set site url on db(SiteConfig)

Loading content on the path:
- http://domain-name/parse-content/

Search through the list of words
- http://domain-name/find-word?q=word


------------------------------------------------------------------------------------------------------------------------

The goal of this test is to create Search Engine System based on Django
infrastructure. Please pay special attention to the design, possible
future extensions and easy configuration by a user.
You can use Django Admin as the user interface

The system should include 3 major parts:
Data crawler - will connect to the list of web pages based on configuration,
 collect the page content and store it with the meta-data to the DB. The
 crawler should support both manual and automatic periodic execution.
Data analysis - will asynchronously execute the list of detection engines.
The engine gets the page content, run the logic and creates zero or more
 tags in case of hit. For the demo please create 2 engines:
an engine that looks for list of words. For each word found add the relevant tag.
an engine that looks for images links and if the page includes more than x images creates a tag.

Data presentation
    manage the crawler list of sites
    engines’ configuration - map between word and tag
    basic query of the results
        present list of sites with specified tag