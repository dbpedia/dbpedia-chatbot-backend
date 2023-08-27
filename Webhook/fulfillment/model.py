from helpers import intents
from helpers.file_saver import file_saver
import json
from typing import List
from pydantic import BaseModel, Field
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../helpers'))

saver = file_saver()


class Information(BaseModel):
    message: str = Field(
        title="A text that was sent by the chatbot.",
        example="I have a question!"
    )
    intent: str = Field(
        title="The recognized intent by the chatbot.",
        example="QuestionIntent"
    )
    session: str = Field(
        title="The session in which the question was asked.",
        example="1235456789"
    )


class FullfillmentText(BaseModel):
    text: List[str] = Field(
        title="Text response from webhook.", example="Your answer!"
    )


class FulfillmentMessage(BaseModel):
    text: FullfillmentText = Field(
        title="A list of response texts.", example=["Your answer!", "And another one!"]
    )


class FulfillmentMessages(BaseModel):
    fulfillmentMessages: List[FulfillmentMessage] = Field(
        title="A list of responses. Can be adjusted to fit other response types."
    )


intentMap = {}

intentMap['qanary-ActivateComponent'] = intents.activateComponentIntent
intentMap['qanary-ActiveQanaryComponents'] = intents.activeQanaryComponentsIntent
intentMap['qanary-AddComponentToProfile'] = intents.addComponentToProfileIntent
intentMap['qanary-AskQanary'] = intents.askQanaryIntent
intentMap['qanary-ComponentInformationFromProfile'] = intents.componentInformationFromProfileIntent
intentMap['qanary-ComponentStartsWith'] = intents.componentStartwithIntent
intentMap['qanary-CreateProfile'] = intents.createProfileIntent
intentMap['qanary-DeactivateComponent'] = intents.deactivateComponentIntent
intentMap['qanary-EmptyComponents'] = intents.emptyComponentsIntent
intentMap['qanary-GetExplanationOfPrevAnswer'] = intents.getExplanationOfPrevAnswerIntent
intentMap['qanary-RemoveComponentFromProfile'] = intents.removeComponentFromProfileIntent
intentMap['qanary-ResetComponents'] = intents.resetComponentsIntent
intentMap['qanary-ShowActiveComponents'] = intents.showActiveComponentsIntent
intentMap['qanary-ShowRdfVisualization'] = intents.showRdfVisualizationIntent


def save_dicts():
    root = "./dict_jsons/"
    json.dump(intents.sessionIdManagement, open(
        f"{root}sessionIdManagement.json", "w"))
    json.dump(intents.lastKbquestion, open(f"{root}lastKbquestion.json", "w"))
    json.dump(intents.lastGraphId, open(f"{root}lastGraphId.json", "w"))
    json.dump(intents.profiles, open(f"{root}profiles.json", "w"))


def set_dicts():
    root = "./dict_jsons/"
    intents.sessionIdManagement = json.load(
        open(f"{root}sessionIdManagement.json", "r"))
    intents.lastKbquestion = json.load(open(f"{root}lastKbquestion.json", "r"))
    intents.lastGraphId = json.load(open(f"{root}lastGraphId.json", "r"))
    intents.profiles = json.load(open(f"{root}profiles.json", "r"))


def handle_request(request_information):
    print(request_information, flush=True)
    # for multiple workers
    # set_dicts()
    message = intentMap[request_information['queryResult']
                        ['intent']['displayName']](request_information)
    # for multiple workers
    # save_dicts()
    fulltext = FullfillmentText(text=[message])
    fullmsg = FulfillmentMessage(text=fulltext)

    return FulfillmentMessages(fulfillmentMessages=[fullmsg])
