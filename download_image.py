import random
import urllib3.request
from urllib3.request import urlretrieve

def download_web_image(url):
    name = random.randrange(1, 1000)
    fullname = str(name) + ".jpg"      # here we can't use name only without str because otherwise it will be a number and not a string and will give an error
    urllib3.request.urlretrieve(url, fullname)

download_web_image("https://www.facebook.com/photo.php?fbid=255629938361869&set=a.127097991215065.1073741826.100017445947001&type=3&source=11&referrer_profile_id=100017445947001")
