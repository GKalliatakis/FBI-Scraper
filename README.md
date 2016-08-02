# FBI Scraper -- Flickr Bulk Image Scraper
### A simple, multithreaded image scraper implemented in Python for downloading all images from the Flickr web service for a given keyword and time period.

### Installation
You need git (distributed version control system) installed globally.
Open your favorite Terminal and run these commands.
```sh
$ sudo apt-get update
$ sudo apt-get install git
$ clone https://github.com/GKalliatakis/FBI_Scraper
```

Every Flickr API application needs to obtain an API 'key'. You can apply for a key by following this link
https://www.flickr.com/services/api/auth.howto.web.html.

Once the API_KEY and the API_SECRET are obtained, open flickr.py and set those variables accordingly.

### Usage
```sh
$ cd FBI_Scraper
$ python multigetphotos.py [KEYWORD(S)] [START DATE] [END DATE]
```
By default, a new folder called “KEYWORD” will be created in the working directory, containing all the downloaded images.


### Example: 

Scrape all images of sea bass which were uploaded between the 1st of January 2016 and 1st of June 2016.
```sh
$ python multigetphotos.py sea+bass 01-01-2016 01-06-2016
```

License
----


MIT


**This app is for learning purposes, and not meant for any use in production / commercial purposes.**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [@thomasfuchs]: <http://twitter.com/thomasfuchs>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [keymaster.js]: <https://github.com/madrobby/keymaster>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]:  <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
