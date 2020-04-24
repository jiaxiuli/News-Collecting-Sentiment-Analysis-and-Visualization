# -*- coding: utf-8 -*-
from flask import Flask, request
app = Flask(__name__)
import eventregistry
er = eventregistry.EventRegistry(apiKey = "23760d8a-beec-49ae-be16-250ff16e2e1f")
#from flask import Flask, request, jsonify
import json
from eventregistry import *
@app.route('/',methods=['GET'])
def search():

     if request.method == 'GET':
            key = request.args.get("keyword")
            lang0 = request.args.get("language")
            typ = request.args.get("type")
            
            
     if typ == "event":
            q = QueryEvents(lang = lang0,
                              keywords = key
                                #  sourceLocationUri  != None,
                              #dataType = ["news"])
                            )
     
            q.setRequestedResult(RequestEventsInfo(
    returnInfo = ReturnInfo(
     #   articleInfo = ArticleInfoFlags(location = True),
        locationInfo = LocationInfoFlags(geoLocation = True)
        )))
            res = er.execQuery(q)
    #        datalist = [[]*3]*100
    #        i = 0
            k = 0
            str0 = "["
            for art in res['events']['results']:
               if res['events']['results'][k]['location'] :    
# =============================================================================
#                   print(type(res['articles']['results'][k]['location']['lat']))
#                   templist = [res['articles']['results'][k]['location']['lat'],res['articles']['results'][k]['location']['long'],5]
#                   datalist[i] = templist
#                   i = i + 1
# =============================================================================
                    str0 = str0 + "[" + str(res['events']['results'][k]['location']['long'])+","+str(res['events']['results'][k]['location']['lat'])+","+str(1)+"]"+","
               k = k + 1
            str0 = str0[:-1]
            str0 = str0 + "]"
            fileObject = open("C:/xampp/htdocs/map/population.json", 'w') 
  #   for num in datalist:  
            fileObject.write(str0)
            fileObject.close()  
    # print(str0)
    
    
     if typ == "article":
          
            q = QueryArticles(lang = lang0,
                              keywords = key
                                #  sourceLocationUri  != None,
                              #dataType = ["news"])
                            )
     
            q.setRequestedResult(RequestArticlesInfo(
    returnInfo = ReturnInfo(
        articleInfo = ArticleInfoFlags(location = True),
        locationInfo = LocationInfoFlags(geoLocation = True)
        )))
            res = er.execQuery(q)
    #        datalist = [[]*3]*100
    #        i = 0
            k = 0
            str0 = "["
            for art in res['articles']['results']:
               if res['articles']['results'][k]['location'] :    
# =============================================================================
#                   print(type(res['articles']['results'][k]['location']['lat']))
#                   templist = [res['articles']['results'][k]['location']['lat'],res['articles']['results'][k]['location']['long'],5]
#                   datalist[i] = templist
#                   i = i + 1
# =============================================================================
                    str0 = str0 + "[" + str(res['articles']['results'][k]['location']['long'])+","+str(res['articles']['results'][k]['location']['lat'])+","+str(1)+"]"+","
               k = k + 1
            str0 = str0[:-1]
            str0 = str0 + "]"
            fileObject = open("C:/xampp/htdocs/map/population.json", 'w') 
  #   for num in datalist:  
            fileObject.write(str0)  
            fileObject.close()  
     print(key)
     print(lang0)
     print(typ)         
     print("sucess!")
     return json.dumps(res,ensure_ascii=False)
     return "ok"
 

if __name__ == '__main__':
    app.run()
