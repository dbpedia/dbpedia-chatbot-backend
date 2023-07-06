import uvicorn
from fulfillment.model import handle_request
from fastapi import FastAPI
from starlette.requests import Request
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

app = FastAPI(
    title="WebhookExample",
    version="0.0.1",
)


@app.post("/webhook",
          summary="Handle Dialogflow Webhook calls.",
          response_description="Request Information.",
          responses={
              200: {
                  "description": "An example result",
                  "content": {
                      "application/json": {
                          "example": {
                              "fulfillmentMessages":
                              [
                                  {
                                      "text": {
                                          "text": [
                                              "Text response from webhook"
                                          ]
                                      }
                                  }
                              ]
                          }
                      }
                  },
              }
          }
          )
async def call_recognition(req: Request):
    """
    Handle a Dialogflow webhook request with a structure as stated in their [docs](https://cloud.google.com/dialogflow/es/docs/fulfillment-webhook#webhook_request).
    """
    dialogflow_json = await req.json()
    return handle_request(dialogflow_json)


@app.get("/health",
         tags=["health"],
         summary="Check if the service is running and accessible.",
         response_description="An \"ok\" if all is well.",
         responses={
             200: {
                 "description": "Confirmation of service",
                 "content": {
                     "application/json": {
                         "example": {
                             "status": "ok"
                         }
                     }
                 }
             }
         }
         )
def am_i_ok():
    """
    Check if the service is addressable.
    """
    return {"status": "ok"}


if __name__ == '__main__':
    # log_config = uvicorn.config.LOGGING_CONFIG
    # log_config["formatters"]["access"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"
    # log_config["formatters"]["default"]["fmt"] = "%(asctime)s - %(levelname)s - %(message)s"

    # uvicorn.run("main:app",
    #             host="127.0.0.1",
    #             port=int(os.environ.get('PORT', 3000)),
    #             reload=True,
    #             debug=True
    #             )
    uvicorn.run("main:app")
