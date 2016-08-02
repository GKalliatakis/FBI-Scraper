########################################################################
# IMPORTS
########################################################################

import os
import urllib
import urlparse
import flickr

########################################################################
# Definitions
########################################################################

def get_biased_photos(tag, min_taken_date, max_taken_date):
	#Change Folder Path
	if os.path.isdir(tag):
		pass
	else:
		os.mkdir(tag)
	os.chdir(tag)

	#Run image download
	for page in range(1,8):
		photos = flickr.photos_search(tags=tag, page=page, per_page=500, tag_mode='all',
									  sort="interestingness-desc",
									  min_taken_date=min_taken_date,
									  max_taken_date=max_taken_date)
		for photo in photos:
			try:
				url = photo.getURL(size='Original', urlType='source')
				urllist.append(url)
				image = urllib.URLopener()
				image.retrieve(url, os.path.basename(urlparse.urlparse(url).path))
				print 'Downloading...', url
			except flickr.FlickrError:
				print 'Link no longer available (!)'
########################################################################
urllist = []
