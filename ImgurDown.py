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
        for i in range(0,5): # randomly generates 5 char string 
            r = r + self.keys[random.randint(0,61)]
        s = "http://i.imgur.com/" + r + ".png" # append to url
        return s

    def download(self, n):
        dirpath = os.path.dirname(__file__) # absolute dir
        relpath = "tmp"
        abspath = os.path.join(dirpath, relpath) # create path to image directory
        
        try:
            shutil.rmtree(abspath) # delete image directory if it exists
            
        except:
            print "creating directory"

        try:
            os.makedirs("tmp") # make the image directoy

        except:
            print "error making directoy"
            
            
        for i in range(0,n):            
            url = self.createURL() # generate random imgur url

            # test if theurl is invalid 
            while(urllib.urlopen(url).geturl() == "http://i.imgur.com/removed.png"):
                url = self.createURL() # if url is invalid try another

            dirpath = os.path.dirname(__file__) # absolute dir 
            relpath = "tmp/" + str(i) + ".png" # create path to image directory
            altpath = "tmp/" + str(i) + ".jpg" # final images will be jpg
            abspath = os.path.join(dirpath, relpath) # alternate path for png images
            finalpath = os.path.join(dirpath, altpath) # alternate path for jpg images
                
            try:           
                f = open(abspath, "wb")
                print str(i) + " " + urllib.urlopen(url).geturl() 
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
            

def main():  # test case    
    testobj = ImgurDown()
    testobj.download(10)

if __name__ == '__main__':
    main()
        
    

     
