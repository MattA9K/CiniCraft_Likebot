__author__ = 'Mateusz Andrzejczuk (CiniCraft on GitHub)'

import os
import pycurl
import cStringIO
import re
import random
import time
import datetime
import sys


# hashtags = ["mvp"]


def login(username, password):
    try:
        os.remove("pycookie.txt")
    except:
        pass

    buf = cStringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, "http://web.stagram.com")
    c.setopt(pycurl.COOKIEFILE, "pycookie.txt")
    c.setopt(pycurl.COOKIEJAR, "pycookie.txt")
    c.setopt(pycurl.WRITEFUNCTION, buf.write)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.setopt(pycurl.ENCODING, "")
    c.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6 (.NET CLR 3.5.30729)")
    c.perform()
    curlData = buf.getvalue()
    buf.close()

    clientid = re.findall(ur"href=\"https:\/\/api.instagram.com\/oauth\/authorize\/\?client_id=([a-z0-9]*)&redirect_uri=http:\/\/web.stagram.com\/&response_type=code&scope=likes\+comments\+relationships\">LOG IN",curlData)
    instagramlink = re.findall(ur"href=\"([^\"]*)\">LOG IN",curlData)


# CiniCraft

    buf = cStringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, instagramlink[0])
    c.setopt(pycurl.COOKIEFILE, "pycookie.txt")
    c.setopt(pycurl.COOKIEJAR, "pycookie.txt")
    c.setopt(pycurl.WRITEFUNCTION, buf.write)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.setopt(pycurl.ENCODING, "")
    c.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6 (.NET CLR 3.5.30729)")
    c.perform()
    curlData = buf.getvalue()
    buf.close()

    postaction = re.findall(ur"action=\"([^\"]*)\"",curlData)
    csrfmiddlewaretoken = re.findall(ur"name=\"csrfmiddlewaretoken\" value=\"([^\"]*)\"",curlData)





    postdata = 'csrfmiddlewaretoken='+csrfmiddlewaretoken[0]+'&username='+username+'&password='+password
# CiniCraft
    buf = cStringIO.StringIO()
    c = pycurl.Curl()
    c.setopt(pycurl.URL, "https://instagram.com"+postaction[0])
    c.setopt(pycurl.COOKIEFILE, "pycookie.txt")
    c.setopt(pycurl.COOKIEJAR, "pycookie.txt")
    c.setopt(pycurl.WRITEFUNCTION, buf.write)
    c.setopt(pycurl.FOLLOWLOCATION, 1)
    c.setopt(pycurl.ENCODING, "")
    c.setopt(pycurl.SSL_VERIFYPEER, 0)
    c.setopt(pycurl.REFERER, "https://instagram.com/accounts/login/?next=/oauth/authorize/%3Fclient_id%3D"+clientid[0]+"%26redirect_uri%3Dhttp%3A//web.stagram.com/%26response_type%3Dcode%26scope%3Dlikes%2Bcomments%2Brelationships")
    c.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6 (.NET CLR 3.5.30729)")
    c.setopt(pycurl.POST, 1)
    c.setopt(pycurl.POSTFIELDS, postdata)
    c.setopt(pycurl.POSTFIELDSIZE, len(postdata))# CiniCraft
    #c.setopt(pycurl.VERBOSE, True)
    c.perform()
    curlData = buf.getvalue()
    buf.close()



def like(hashtags, rate):
    likecount = 0
    totalLikecount = 0
    sleepcount = 0# CiniCraft
    for tag in hashtags:
        nextpage = "http://web.stagram.com/tag/"+tag+"/?vm=list"
        while nextpage != False:
            buf = cStringIO.StringIO()# CiniCraft
            c = pycurl.Curl()
            c.setopt(pycurl.URL, nextpage)
            c.setopt(pycurl.COOKIEFILE, "pycookie.txt")
            c.setopt(pycurl.COOKIEJAR, "pycookie.txt")
            c.setopt(pycurl.WRITEFUNCTION, buf.write)
            c.setopt(pycurl.FOLLOWLOCATION, 1)
            c.setopt(pycurl.ENCODING, "")
            c.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6 (.NET CLR 3.5.30729)")
            c.perform()
            curlData = buf.getvalue()
            buf.close()

            nextpagelink = re.findall(ur"<a href=\"([^\"]*)\" rel=\"next\">Earlier<\/a>",curlData)
            if len(nextpagelink)>0:
                nextpage = "http://web.stagram.com"+nextpagelink[0]
            else:# CiniCraft
                nextpage = False

            likedata = re.findall(ur"<span class=\"like_button\" id=\"like_button_([^\"]*)\">",curlData)

            if len(likedata) > 0:
                for imageid in likedata:
                    repeat = True
                    #print likedata
                    while repeat:
                        randomint = random.randint(1000,9999)# CiniCraft

                        postdata = 'pk='+imageid+'&t='+str(randomint)
                        buf = cStringIO.StringIO()
                        c = pycurl.Curl()
                        c.setopt(pycurl.URL, "http://web.stagram.com/do_like/")
                        c.setopt(pycurl.COOKIEFILE, "pycookie.txt")
                        c.setopt(pycurl.COOKIEJAR, "pycookie.txt")
                        c.setopt(pycurl.WRITEFUNCTION, buf.write)
                        c.setopt(pycurl.FOLLOWLOCATION, 1)
                        c.setopt(pycurl.ENCODING, "")
                        c.setopt(pycurl.USERAGENT, "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2) Gecko/20100115 Firefox/3.6 (.NET CLR 3.5.30729)")
                        c.setopt(pycurl.POST, 1)
                        c.setopt(pycurl.POSTFIELDS, postdata)
                        c.setopt(pycurl.POSTFIELDSIZE, len(postdata))
                        #c.setopt(pycurl.VERBOSE, True)
                        c.perform()
                        postData = buf.getvalue()
                        buf.close()# CiniCraft
                        if postData == '''{"status":"OK","message":"LIKED"}''':
                            likecount += 1
                            totalLikecount += 1
                            print "You liked #"+tag+" image "+imageid+"! Like count: "+str(likecount)
                            if likecount == rate:  # break after n likes to switch to a new hash tag
                                likecount = 0
                                print "Grand total of likes made in this run: " + str(totalLikecount)
                                hashtags.pop(0)
                                try:
                                    tag = hashtags[0]
                                except IndexError as e:
                                    print "No more hashtags remaining, Total likes made on this run: " + str(totalLikecount)
                                    sys.exit("likebot has been terminated")
                                break
                            repeat = False
                            sleepcount = 0
                            time.sleep(random.randint(1,2))
                        else:
                            print "Failed to like image, instead of 200 OK response you've recieved: " + postData
                            sleepcount += 1
                            print "Sleeping on #"+tag+" for "+str(sleepcount)+" minute(s)."
                            print datetime.datetime.now().time()
                            print ""
                            print "#"+tag+" will not be liked any further, moving on to the next one after sleep."
                            print "Grand total of likes made in this run: " + str(totalLikecount)
                            hashtags.pop(0)
                            time.sleep(60)
                            try:
                                tag = hashtags[0]
                            except IndexError as e:
                                print "No more hashtags remaining, Total likes made on this run: " + str(totalLikecount)
                                sys.exit("likebot has been terminated")
                            break

                            

def main():
    login()
    like()

if __name__ == "__main__":
    main()

# CiniCraft