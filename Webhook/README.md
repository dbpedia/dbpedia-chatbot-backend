# Contributors
* [Udit Arora](https://github.com/UditArora2000)
* [Annemarie Wittig](https://github.com/AnnemarieWittig)

# Tutorial
**Connecting a chatbot with a webhook**

 1. Create your chatbot in the [Dialogflow Webinterface](https://dialogflow.cloud.google.com/#/login)
 2. Go to Fullfillment  
    ![image](https://user-images.githubusercontent.com/59013332/185667430-8f07bb65-aa58-4359-b82b-0730b7888461.png)
 3. Enable webhooks and insert your webhook URL  
    ![image](https://user-images.githubusercontent.com/59013332/185667711-8468d1ca-6679-4120-a9cc-8be667b4f787.png)
 4. Pick the intent(s) that you want to connect to the webhook and navigate to them.
 5. At the end of the page, open the Fulfillment menu and press "ENABLE FULFILLMENT"
 6. Press "Enable Webhook call for this intent"
    ![image](https://user-images.githubusercontent.com/59013332/185671368-7768e3da-68bc-4039-9a8d-5b3e594456cd.png)
    
 **Notes**
    
The Webhook must fulfill certain requirements such as handling https POST requests with a certain body.
The webhook must handle requests with a [body like](https://cloud.google.com/dialogflow/es/docs/fulfillment-webhook#webhook_request):
```json
{
  "responseId": "response-id",
  "session": "projects/project-id/agent/sessions/session-id",
  "queryResult": {
    "queryText": "End-user expression",
    "parameters": {
      "param-name": "param-value"
    },
    "allRequiredParamsPresent": true,
    "fulfillmentText": "Response configured for matched intent",
    "fulfillmentMessages": [
      {
        "text": {
          "text": [
            "Response configured for matched intent"
          ]
        }
      }
    ],
    "outputContexts": [
      {
        "name": "projects/project-id/agent/sessions/session-id/contexts/context-name",
        "lifespanCount": 5,
        "parameters": {
          "param-name": "param-value"
        }
      }
    ],
    "intent": {
      "name": "projects/project-id/agent/intents/intent-id",
      "displayName": "matched-intent-name"
    },
    "intentDetectionConfidence": 1,
    "diagnosticInfo": {},
    "languageCode": "en"
  },
  "originalDetectIntentRequest": {}
}
```

and the response, if a [normal text message](https://cloud.google.com/dialogflow/es/docs/fulfillment-webhook#text_response), must look like:
```json
{
  "fulfillmentMessages": [
    {
      "text": {
        "text": [
          "Text response from webhook"
        ]
      }
    }
  ]
}
```

More elaborate response types as well as more information can be found in the [Documentaion](https://cloud.google.com/dialogflow/es/docs/fulfillment-webhook).
