# author - MayurM
# description - This program downloads random imgur images

__author__ = 'Mayur M'

import random
import urllib
import Image
import os

class ImgurDown:
    keys = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    def createURL(self):        
        r = ""
        for i in range(0,5):
            r = r + self.keys[random.randint(0,61)]
        s = "http://i.imgur.com/" + r + ".png"
        return s

    def download(self, n):       
        for i in range(0,n):
            url = self.createURL()
            while(urllib.urlopen(url).geturl() == "http://i.imgur.com/removed.png"):
                url = self.createURL()
                
            try:
                f = open(str(i) + ".png", "wb")
                print str(i) + " " + urllib.urlopen(url).geturl()
                f.write(urllib.urlopen(url).read())                
                f.close()
                im = Image.open(str(i) + ".png")
                
                if im.mode != "RGB":
                    im = im.convert("RGB")
                    
                im.save(str(i) + ".jpg")
                os.remove(str(i) + ".png")
                
            except Exception, e:
                print e
            

def main():  # test case    
    testobj = ImgurDown()
    testobj.download(100)

if __name__ == '__main__':
    main()
        
    

     
