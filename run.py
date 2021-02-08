from front.web.main import app as appmain
from front.rest.api import app as apprest
 

apprest.run(debug=True)
#appmain.run(debug=True)