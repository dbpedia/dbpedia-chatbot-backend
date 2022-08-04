const express = require('express');
const axios = require('axios');
const https = require('https')
const fs = require('fs')
const {WebhookClient} = require('dialogflow-fulfillment');
const intent = require("./intent");
const qanaryComponents = require('./components'); 
let intentMap = new Map() 
const app = express()
const certsPath = './certs'
let isSSL = false
app.use(express.json())

let sslConfig = { 
}

// if (fs.existsSync(`${certsPath}/key.key`) && fs.existsSync(`${certsPath}/cert.cert`)) { 
//     sslConfig.key = fs.readFileSync(`${certsPath}/key.key`),
//     sslConfig.cert = fs.readFileSync(`${certsPath}/cert.cert`)
//     isSSL = true
// }

intentMap.set('Default Welcome Intent', intent.welcomeIntent)
intentMap.set('DBpedia Info Intent', intent.dbpediaInfoIntent)
intentMap.set('DBpedia contribute Intent', intent.dbpediaContributeIntent)
intentMap.set('Show component list Intent', intent.activeComponentsIntent)
intentMap.set('Reset list of components Intent', intent.resetComponentsListIntent)
intentMap.set('Deactivate component Intent', intent.deactivateComponentIntent)
intentMap.set('Activate component Intent', intent.activateComponentIntent) 
intentMap.set('Active Qanary components', intent.activeQanaryIntent) 
intentMap.set('Activate profile component', intent.activateProfileIntent) 
intentMap.set('Component startwith intent', intent.componentStartwithIntent) 
intentMap.set('show rdf visualization', intent.showRDFGraphIntent) 
intentMap.set('Create profile intent', intent.createProfileIntent) 
intentMap.set('Add components to profile', intent.addComponentsToProfile) 
intentMap.set('Remove component from profile', intent.removeComponentFromProfile) 
intentMap.set('Component information from profile', intent.componentInformationFromProfile) 
intentMap.set('Help Intent', intent.helpIntent)
intentMap.set('Empty component list', intent.Emptycomponentlist)  
intentMap.set('Ask Qanary Intent', intent.AskQanaryIntent)
intentMap.set('Default Fallback Intent', intent.fallBack)

app.post('/webhook', (request, response) => {
    console.log("webhook")
    let agent = new WebhookClient({
        request: request,
        response: response
    })
    // console.log(request)
    // console.log(response)
    // window.print(request)c
    agent.handleRequest(intentMap)
});

app.get('/health', (req, res) => {
    console.log("reached")
    res.status(200).end('OK')
});

(async function(){
    await qanaryComponents.getQanaryComponents() 
    if (isSSL) {
        https.createServer(sslConfig, app).listen(process.env.PORT || 3000, () => {
            qanaryComponents.updateComponents() 
            console.log('1')
            console.log('Server is Running on port 3000')
        })
    } else {
        app.listen(process.env.PORT || 3000, () => {
            qanaryComponents.updateComponents()
            console.log('2')
            console.log('Server is Running on port 3000')
        })
    }
    
})()

process.on('SIGINT', function() {
    console.log( "\nGracefully shutting down from SIGINT (Ctrl-C)" );
    process.exit(1);
});