import urllib2
import goslate

proxy_handler = urllib2.ProxyHandler({"http" : "http://172.31.100.27:3128"})
proxy_opener = urllib2.build_opener(urllib2.HTTPHandler(proxy_handler),
                                    urllib2.HTTPSHandler(proxy_handler))

gs_with_proxy = goslate.Goslate(opener=proxy_opener)
#with open('spoken.txt', 'r') as myfile:
#    spoken_text = myfile.read()
translation = gs_with_proxy.translate("hello world", "hi")
print translation
