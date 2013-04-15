from datetime import datetime
from django.db import models
from django.test.client import Client

from BeautifulSoup import BeautifulSoup

# create a client
client = Client()

class Inspection(models.Model):
    started = models.DateTimeField(default=datetime.now)
    start_path = models.CharField(max_length = 1024, default="/")
    
    def start_inspection(self):
        self.save()
        path = Path(
            inspection=self,
            path=self.start_path
            )     
        
        # seed it with the first path
        uninspected_paths = [path]
        
        # are there any uninspected pages left?
        while uninspected_paths:

            # check it for a response and further paths
            uninspected_paths[0].inspect()

            # find uninspected_paths
            uninspected_paths = self.paths.filter(response_code=None)
             
            print self.paths.filter().count(), 
            print "found, or which", uninspected_paths.count(), "remain to be inspected"
        

class Path(models.Model):
    inspection = models.ForeignKey(Inspection, related_name = "paths")
    path = models.CharField(max_length = 1024)
    referrer = models.ForeignKey('self', blank=True, null=True, related_name = "referred")
    response_code = models.IntegerField(blank=True, null=True)
    content_type = models.CharField(max_length = 255, blank=True, null=True)
    django_error = models.CharField(max_length = 1024, blank=True, null=True)
    
    def inspect(self):  
        
        print self.path,
        
        # we need to catch *any* exception that might be thrown
        try:
            response = client.get(self.path) 
            self.response_code = response.status_code
        except Exception, e:
            self.django_error = e
            self.response_code = 0
            response = {}

        print self.response_code,

        self.content_type = response.get("content-type", "")
        self.save()
       
        # we are only interested in HTML documents 
        if "text/html" in self.content_type:

            # examine the page for new hrefs
            soup = BeautifulSoup(''.join(response.content)) 

            # make a list of hrefs
            hrefs = [path.path for path in self.inspection.paths.all()]

            # for each anchor href that starts with / and is not in hrefs already
            for href in [anchor["href"] for anchor in soup.findAll('a', href=True) if anchor["href"].startswith("/") and not anchor["href"] in hrefs]: 
                
                path = Path(
                    inspection=self.inspection,
                    path=href, 
                    referrer=self
                    ).save()
