import fuzzyset
import components
import ast
from SPARQLWrapper import SPARQLWrapper, JSON, POST
import requests
import sys
import os
from dotenv import load_dotenv

load_dotenv()
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

defaultComponents = ["NED-DBpediaSpotlight", "SparqlExecuter",
                     "OpenTapiocaNED", "BirthDataQueryBuilder", "WikidataQueryExecuter"]
profileComponents = []
vizURL = "https://dbpedia-rdf-viz.herokuapp.com/visualize/"
sessionIdManagement = {}
lastKbquestion = {}
lastGraphId = {}
lastKbAnswer = {}
profiles = {}
profileComponents = []
DEFAULT_COMPONENTS = ["NED-DBpediaSpotlight", "SparqlExecuter",
                      "OpenTapiocaNED", "BirthDataQueryBuilder", "WikidataQueryExecuter"]


def activateComponentIntent(agent):
    activateComponent = agent['queryResult']['parameters']['activatecomponent'][0]
    qanaryComponentList = components.getQanaryComponents()
    activateResult = qanaryComponentList.get(activateComponent)
    if activateResult == None:
        output = activateComponent + \
            ' not available to know more about the active components use command \'list of active qanary components\'.'
    else:
        addComponent = activateResult[0][1]
        sessionId = agent['session'].split('/')[4]
        if sessionId not in sessionIdManagement:
            sessionIdManagement[sessionId] = {
                'components': DEFAULT_COMPONENTS.copy()}
        getComponent = sessionIdManagement.get(sessionId)
        localcomponentList = getComponent['components']
        index = localcomponentList.index(
            addComponent) if addComponent in localcomponentList else -1
        if index == -1:
            localcomponentList.append(addComponent)
            sessionIdManagement[sessionId] = {'components': localcomponentList}
            output = 'Successfully added ' + addComponent + \
                ' you can add more components by saying \'add\' plus the name of the component.'
        else:
            output = addComponent + ' already exists in the list to know more about active components use command \'list of active qanary components\'.'
    return output


def activeQanaryComponentsIntent(agent):
    fuzzy = components.getQanaryComponentNames()
    output = 'Currently ' + \
        str(len(fuzzy)) + ' are active. The components are ' + \
        ', '.join([f'\"{x}\"' for x in fuzzy])
    return output


def getAnswerFromDbpedia(query):
    endpointUrl = os.getenv('DBPEDIA_SPARQL_URL')
    sparql = SPARQLWrapper(endpointUrl)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    sparql.setMethod(POST)
    result = sparql.queryAndConvert()
    print(result)
    return result['results']['bindings'][0]['answer']['value']


def getAnswerFromQanary(graphId):
    endpointUrl = os.getenv('SPARQL_URL')
    output = "No answer available."
    query = """
            PREFIX oa: <http://www.w3.org/ns/openannotation/core/>
            PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
            PREFIX qa: <http://www.wdaqua.eu/qa#>
            SELECT *
            FROM <"""+graphId+""">
            WHERE {
                ?s rdf:type qa:AnnotationOfAnswerSPARQL.
                ?s oa:hasBody ?resultAsSparqlQuery.
            }
    """
    sparql = SPARQLWrapper(endpointUrl)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    sparql.setMethod(POST)
    result = sparql.queryAndConvert()
    print(result)
    dbpediaQuery = result['results']['bindings'][0]['resultAsSparqlQuery']['value']
    result = getAnswerFromDbpedia(dbpediaQuery)
    if result is not None:
        output = result
    return output


def askQanaryIntent(agent):
    sessionId = agent['session'].split('/')[4]
    lastKbquestion[sessionId] = agent['queryResult']['queryText']
    print(sessionIdManagement)
    getComponent = sessionIdManagement[sessionId]

    show = getComponent['components']
    print(show)
    params = {
        "question": lastKbquestion[sessionId],
        "componentlist[]": show
    }
    response = requests.post(os.getenv('QANARY_PIPELINE_URL'), params)
    responseDict = ast.literal_eval(response.text)
    print(responseDict)
    currentGraphId = responseDict['inGraph']
    lastGraphId[sessionId] = currentGraphId
    output = getAnswerFromQanary(currentGraphId)
    lastKbAnswer[sessionId] = output
    return output


def getExplanationOfPrevAnswerIntent(agent):
    # sessionId = agent['session'].split('/')[4]
    # try:
    #     lastGraphIdOfSession = lastGraphId[sessionId]
    # except:
    #     lastGraphIdOfSession = None
    explanation = "Sorry, there was no previously asked question in this session."
    # if lastGraphIdOfSession is not None:
    endpointUrl = 'http://pie.qanary.net:8000/sparql'
    output = "No explanation available."
    graphId = "24a1132b-6c7d-4770-8f30-e87cd43f8cf8"
    queryAnnotationsOfPrevQuestion = """PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        PREFIX oa: <http://www.w3.org/ns/openannotation/core/>
        PREFIX qa: <http://www.wdaqua.eu/qa#>
        SELECT *
        FROM <"""+graphId+"""> 
        WHERE {
            ?annotationId rdf:type ?type.
            ?annotationId oa:hasBody ?body.
            ?annotationId oa:hasTarget ?target.
            ?annotationId oa:annotatedBy $X .
        }"""
    sparql = SPARQLWrapper(endpointUrl)
    sparql.setQuery(queryAnnotationsOfPrevQuestion)
    sparql.setReturnFormat(JSON)
    sparql.setMethod(POST)
    result = sparql.queryAndConvert()

    return result if not None else explanation


def activateProfileIntent(agent):
    profileName = agent['queryResult']['parameters']['profilename']
    defaultcomponent = fuzzyset.FuzzySet()
    defaultcomponent.add("default component")
    checkProfile = defaultcomponent.get(profileName)
    sessionId = agent['session'].split('/')[4]
    if checkProfile == None:
        if sessionId + profileName in profiles:
            getComponent = profiles.get(sessionId + profileName)
            show = getComponent['components']
            sessionIdManagement[sessionId] = {'components': show}
            output = profileName + \
                ' Activated successfully to know about active components use command \'list of active components\'.'
        else:
            output = profileName + \
                ' profile not defined by you (or by the admin).'
    else:
        sessionIdManagement[sessionId] = {
            'components': ['NED-DBpediaSpotlight', 'QueryBuilderSimpleRealNameOfSuperHero', 'SparqlExecuter', 'OpenTapiocaNED', 'BirthDataQueryBuilder', 'WikidataQueryExecuter']
        }
        output = profileName + \
            ' activated successfully to know about active components use command \'list of active components\'.'
    return output


def addComponentToProfileIntent(agent):
    profileName = agent['queryResult']['parameters']['profilename']
    sessionId = sessionId = agent['session'].split('/')[4]
    print(sessionId)
    if sessionId+profileName in profiles:
        componentName = agent['queryResult']['parameters']['componentname']
        qanaryComponentList = components.getQanaryComponents()
        finalComponentAdd = qanaryComponentList.get(componentName)[0][1]
        if finalComponentAdd == None:
            output = 'Component ' + componentName + \
                ' is not available. To see the active components use command \'list of active qanary components\'.'
        else:
            exists = finalComponentAdd in profiles[sessionId +
                                                   profileName]['components']
            if not exists:
                profiles[sessionId +
                         profileName]['components'].append(finalComponentAdd)
                output = 'Successfully added \'' + finalComponentAdd + '\' to the profile \'' + profileName + \
                    '\'. You can add more components by saying \'add\' followed by the name of the component.'
            else:
                output = finalComponentAdd + ' already exists in the list.'
    else:
        output = profileName + ' does not exists, to create new profile you can say \'create profile and then profile name\' like create profile country.'
    return output


def componentInformationFromProfileIntent(agent):
    profileName = agent['queryResult']['parameters']['profilename']
    sessionId = sessionId = agent['session'].split('/')[4]
    if sessionId+profileName in profiles:
        show = profiles[sessionId+profileName]['components']
        if len(show) == 0:
            output = f"Component list for profile '{profileName}' is empty."
        else:
            output = f"{profileName} contains components {', '.join(show)}"
    else:
        output = profileName + ' does not exists, to create new profile you can say \'create profile and then profile name\' like create \'profile country\'.'
    return output


def componentStartwithIntent(agent):
    startWithName = agent['queryResult']['parameters']['startwith']
    fuzzy = components.getQanaryComponentNames()
    startWithCompare = list(fuzzy)
    startsWith = [x for x in startWithCompare if x[0] == startWithName.upper()]
    if len(startsWith) == 0:
        output = 'Component name starting with ' + startWithName + ' are not available.'
    else:
        ans = ', '.join([f'\"{x}\"' for x in startsWith])
        output = 'Components starting with ' + startWithName + ' are ' + ans
    return output


def createProfileIntent(agent):
    profileName = agent['queryResult']['parameters']['profilename']
    sessionId = agent['session'].split('/')[4]
    if sessionId+profileName in profiles:
        output = 'Profile \'' + profileName + '\' already exists.'
    else:

        profiles[sessionId +
                 profileName] = {'components': profileComponents.copy()}
        output = ' Profile \'' + profileName + '\' added successfully. Now to use this profile you can say \'start ' + \
            profileName + '\' to activate the profile.'
    return output


def deactivateComponentIntent(agent):
    deactivate = agent['queryResult']['parameters']['componentname']
    qanaryComponentList = components.getQanaryComponents()
    deactivateResult = qanaryComponentList.get(deactivate)
    if deactivateResult == None:
        return deactivate + ' is not available, to see the active components use command \'list of active qanary components\'.'

    deactivateComponent = deactivateResult[0][1]
    sessionId = agent['session'].split('/')[4]
    if sessionId not in sessionIdManagement:
        output = deactivateComponent + \
            ' do not exists in the local list of active components to know more about active components use command \'list of active components\'.'
    else:
        getComponent = sessionIdManagement[sessionId]
        localcomponentList = getComponent['components']
        index = localcomponentList.index(
            deactivateComponent) if deactivateComponent in localcomponentList else -1
        if index == -1:
            output = deactivateComponent + \
                ' do not exists in the local list of active components to know more about active components use command \'list of active components\'.'
        else:
            localcomponentList.remove(deactivateComponent)
            sessionIdManagement[sessionId] = {'components': localcomponentList}
            output = "Successfully removed " + \
                deactivateComponent + " from the components list."
    return output


def emptyComponentsIntent(agent):
    sessionId = agent['session'].split('/')[4]
    sessionIdManagement[sessionId] = {'components': []}
    output = 'Components list is now empty.'
    return output


def removeComponentFromProfileIntent(agent):
    profileName = agent['queryResult']['parameters']['profilename']
    sessionId = sessionId = agent['session'].split('/')[4]
    if sessionId+profileName in profiles:
        componentName = agent['queryResult']['parameters']['componentname']
        qanaryComponentList = components.getQanaryComponents()
        finalComponentRemove = qanaryComponentList.get(componentName)[0][1]
        if finalComponentRemove == None:
            output = 'Component ' + componentName + \
                ' is not available. To see the active components use command \'list of active qanary components\'.'
        else:
            exists = finalComponentRemove in profiles[sessionId +
                                                      profileName]['components']
            if exists:
                profiles[sessionId +
                         profileName]['components'].remove(finalComponentRemove)
                output = 'Successfully removed \'' + finalComponentRemove + \
                    '\' from the components list of the profile \'' + profileName + '.'
            else:
                output = finalComponentRemove + ' not available in list to know more about ' + \
                    profileName + ' the component use command \'show components of ' + profileName + '\''
    else:
        output = profileName + ' does not exists, to create new profile you can say \'create profile and then profile name\' like create profile country.'
    return output


def resetComponentsIntent(agent):
    sessionId = agent['session'].split('/')[4]
    sessionIdManagement[sessionId] = {
        'components': DEFAULT_COMPONENTS.copy()}
    output = 'Reset successfully, the components list is now set to default component list.'
    return output


def showActiveComponentsIntent(agent):
    sessionId = agent['session'].split('/')[4]
    if sessionId not in sessionIdManagement:
        return 'Currently, there are no active components, you can add components by saying "add" and then name of the component.'
    getComponent = sessionIdManagement[sessionId]
    show = getComponent['components']
    if len(show) == 0:
        output = "Currently there are no active components"
    else:
        output = f"Currently active components are: {show}"
    return output


def showRdfVisualizationIntent(agent):
    sessionId = agent['session'].split('/')[4]
    currentGraphId = lastGraphId[sessionId]
    output = f"Go to this link to see the RDF visualization: {os.getenv('RDF_VIZ_HOST_URL')}{currentGraphId}"
    return output
