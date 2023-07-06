import json
from model import handle_request
import unittest
from helpers import intents, config


def identified_intent(response_message):
    start_ind = response_message.index(
        "recognized with the intent") + len("recognized with the intent ")
    end_ind = response_message.index(" in the session", start_ind)
    return response_message[start_ind:end_ind]


class TestIntents(unittest.TestCase):
    currentQanaryActiveComponents = ["SparqlExecuter", "QAnswerQueryBuilderAndQueryCandidateFetcher-EN-Wikidata-with-description", "QAnswerQueryBuilderAndQueryCandidateFetcher-RU-Wikidata", "LD-Shuyo", "AnswerTypeClassifier", "BirthDataQueryBuilder", "QE-Query-Filtering", "QAnswerQueryBuilderAndExecutor",
                                     "QAnswerQueryBuilderAndQueryCandidateFetcher", "QAnswerQueryBuilderAndQueryCandidateFetcher-EN-Wikidata", "NED-DBpediaSpotlight", "ComicCharacterAlterEgoSimpleDBpediaQueryBuilder", "OpenTapiocaNED", "QB-SimpleRealNameOfSuperHero", "ComicCharacterNameSimpleNamedEntityRecognizer", "WikidataQueryExecuter"]

    def test01_activateComponentIntent(self):
        request = json.load(open("../requests/activateComponent.json", "r"))
        sessionId = request['session'].split('/')[4]
        _ = handle_request(request)
        activated = "LD-Shuyo" in intents.sessionIdManagement[sessionId]['components']
        self.assertEqual(activated, True, "Activate component intent failed")

    def test02_activeQanaryComponentsIntent(self):
        request = json.load(
            open("../requests/activeQanaryComponents.json", "r"))
        response = handle_request(request).fulfillmentMessages[0].text.text[0]
        expectedList = sorted(self.currentQanaryActiveComponents)
        index = response.find("The components are ") + \
            len("The components are ")
        outputList = sorted(
            [component[1:-1] for component in list(map(str, response[index:].split(", ")))])
        self.assertEqual(outputList, expectedList,
                         "Active qanary components intent failed")

    def test03_createProfileIntent(self):
        request = json.load(open("../requests/createProfile.json", "r"))
        profile = request['queryResult']['parameters']['profilename']
        _ = handle_request(request)
        sessionId = request['session'].split('/')[4]
        created = sessionId+profile in intents.profiles
        self.assertEqual(created, True, "Create profile intent failed")

    def test04_addComponentToProfileIntent(self):
        request = json.load(
            open("../requests/addComponentToProfile.json", "r"))
        sessionId = sessionId = request['session'].split('/')[4]
        profile = request['queryResult']['parameters']['profilename']
        _ = handle_request(request)
        added = "LD-Shuyo" in intents.profiles[sessionId+profile]['components']
        self.assertEqual(added, True, "Add component to profile intent failed")

    def test05_componentInformationFromProfileIntent(self):
        request = json.load(
            open("../requests/componentInformationFromProfile.json", "r"))
        sessionId = sessionId = request['session'].split('/')[4]
        profile = request['queryResult']['parameters']['profilename']
        response = handle_request(request).fulfillmentMessages[0].text.text[0]
        expectedList = sorted(
            intents.profiles[sessionId+profile]['components'])
        index = response.find("contains components ") + \
            len("contains components ")
        if index == len("contains components ") - 1:
            outputList = []
        else:
            outputList = sorted(list(map(str, response[index:].split(", "))))
        self.assertEqual(outputList, expectedList,
                         "Component information from porfile intent failed")

    def test06_componentStartwithIntent(self):
        request = json.load(open("../requests/componentStartswith.json", "r"))
        startLetter = request['queryResult']['parameters']['startwith']
        response = handle_request(request).fulfillmentMessages[0].text.text[0]
        expectedList = sorted(
            [component for component in self.currentQanaryActiveComponents if component[0] == startLetter])
        index = response.find(
            f"starting with {startLetter} are ") + len(f"starting with {startLetter} are ")
        outputList = sorted(
            [component[1:-1] for component in list(map(str, response[index:].split(", ")))])
        self.assertEqual(outputList, expectedList,
                         "Component starts with intent failed")

    def test07_deactivateComponentIntent(self):
        request = json.load(open("../requests/deactivateComponent.json", "r"))
        sessionId = request['session'].split('/')[4]
        _ = handle_request(request)
        activated = "LD-Shuyo" not in intents.sessionIdManagement[sessionId]['components']
        self.assertEqual(activated, True, "Deactivate component intent failed")

    def test08_showActiveComponentsItent(self):
        request = json.load(open("../requests/showActiveComponents.json", "r"))
        sessionId = request['session'].split('/')[4]
        response = handle_request(request).fulfillmentMessages[0].text.text[0]
        expectedList = sorted(
            intents.sessionIdManagement[sessionId]['components'])
        index = response.find(
            "active components are: [") + len("active components are: [")
        outputList = sorted(
            [component[1:-1] for component in list(map(str, response[index:-1].split(", ")))])
        self.assertEqual(outputList, expectedList,
                         "Show activate components intent failed")

    def test09_emptyComponentsIntent(self):
        request = json.load(open("../requests/emptyComponents.json", "r"))
        sessionId = request['session'].split('/')[4]
        _ = handle_request(request)
        numComponents = len(
            intents.sessionIdManagement[sessionId]['components'])
        self.assertEqual(numComponents, 0, "Empty components intent failed")

    def test10_removeComponentFromProfileIntent(self):
        request = json.load(
            open("../requests/removeComponentFromProfile.json", "r"))
        sessionId = sessionId = request['session'].split('/')[4]
        profile = request['queryResult']['parameters']['profilename']
        _ = handle_request(request)
        removed = "LD-Shuyo" not in intents.profiles[sessionId +
                                                     profile]['components']
        self.assertEqual(
            removed, True, "Remove component from profile intent failed")

    def test11_resetComponentsIntent(self):
        request = json.load(open("../requests/resetComponents.json", "r"))
        sessionId = request['session'].split('/')[4]
        _ = handle_request(request)
        expectedList = sorted(config.defaultComponents)
        outputList = sorted(
            intents.sessionIdManagement[sessionId]['components'])
        self.assertEqual(outputList, expectedList,
                         "Reset components intent failed")


def run_tests():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite([loader.loadTestsFromTestCase(TestIntents)])
    runner = unittest.TextTestRunner()
    results = runner.run(suite)
    print(results)


if __name__ == "__main__":
    run_tests()
