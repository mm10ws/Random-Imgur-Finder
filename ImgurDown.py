# author - MayurM
# description - This program downloads random imgur images

__author__ = 'Mayur M'

import random 
import urllib
import Image
import os
import shutil

class ImgurDown:
    # contains valid characters used to generate random imgur urls
    keys = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890" 

    def createURL(self):        
        r = ""
        for i in range(0, 5): # randomly generates 5 char string 
            r = r + self.keys[random.randint(0,61)]
        s = "http://i.imgur.com/" + r + ".png" # append to url
        return s

    def download(self, n):
        dirpath = os.path.dirname(__file__) # absolute dir
        relpath = "tmp"
        abspath = os.path.join(dirpath, relpath) # create path to image directory
        totalmisses = 0 # count total invalid URLs
        
        try:
            shutil.rmtree(abspath) # delete image directory if it exists
            
        except:
            print "creating directory"

        try:
            os.makedirs("tmp") # make the image directoy

        except:
            print "error making directoy"
            
            
        for i in range(0,n):
            miss = 0
            url = self.createURL() # generate random imgur url

            # test if the url is invalid 
            while(urllib.urlopen(url).geturl() == "http://i.imgur.com/removed.png"):
                miss = miss + 1 # count number of invalid URLs
                url = self.createURL() # if url is invalid try another

            totalmisses = totalmisses + miss # add up all invalid URLs
            dirpath = os.path.dirname(__file__) # absolute dir 
            relpath = "tmp/" + str(i) + ".png" # create path to image directory
            altpath = "tmp/" + str(i) + ".jpg" # final images will be jpg
            abspath = os.path.join(dirpath, relpath) # alternate path for png images
            finalpath = os.path.join(dirpath, altpath) # alternate path for jpg images
                
            try:           
                f = open(abspath, "wb")
                print str(i) + ". found valid URL: " + urllib.urlopen(url).geturl() + " after " + str(miss) + " failed attempts." 
                f.write(urllib.urlopen(url).read()) # get image from url              
                f.close()
                im = Image.open(abspath) 

                # use PIL to make final image compatible
                if im.mode != "RGB":
                    im = im.convert("RGB")
                    
                im.save(finalpath)
                os.remove(abspath) # remove png images
                
            except Exception, e:
                print e
                
        # printfinal stats of run
        print "There were " + str(n) + " successful attempts and " + str(totalmisses) + " failed attempts. "
        print "The success rate was " + "{0:.2f}".format(100 * (float(n) / (n + totalmisses))) + "%"
            

def main():  # test case    
    testobj = ImgurDown()
    testobj.download(20) # note change value to specify how many images should be fetched

if __name__ == '__main__':
    main()
        
    

     
