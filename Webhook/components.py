import urllib.request
import ast
import fuzzyset

qanaryComponents = None
qanaryComponentNames = None

def getComponents():
    global qanaryComponents
    global qanaryComponentNames
    response = urllib.request.urlopen('http://demos.swe.htwk-leipzig.de:40111/components').read().decode()
    body = ast.literal_eval(response)
    qanaryComponents = fuzzyset.FuzzySet() 
    qanaryComponentNames = set()
    for i in range(len(body)):
        qanaryComponents.add(body[i]['name'])
        qanaryComponentNames.add(body[i]['name'])

def getQanaryComponentNames():
    global qanaryComponentNames
    getComponents()
    return qanaryComponentNames

def getQanaryComponents():
    global qanaryComponents
    getComponents()
    return qanaryComponents

# async def updateComponents():
#     try:
#         await asyncio.wait_for(getComponents, timeout=15)
#     except:
#         print("15 sec done")
