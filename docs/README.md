# Understanding and Optimizing DBpedia Question Answering through Explanations 
Hi guys, I am Udit Arora.<br /> 
I am glad to share that I have been selected for GSoC 2022 for the project: [Understanding and Optimizing DBpedia Question Answering through Explanations].
I will work under the guidance of my mentors - [Andreas Both](https://www.linkedin.com/in/andreas-both-94267222/), [Aleksandr Perevalov](https://www.linkedin.com/in/alexander-perevalov-837780111/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3BU%2FpdNmPFSUqmoz82LyrZKA%3D%3D), [Ricardo Usbeck](https://www.linkedin.com/in/ricardo-usbeck/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3BQQw%2Bvv%2FvRwmEwkG30ZxSsQ%3D%3D), and [Ram Athreya](https://www.linkedin.com/in/ramgathreya/?lipi=urn%3Ali%3Apage%3Ad_flagship3_people_connections%3BQQw%2Bvv%2FvRwmEwkG30ZxSsQ%3D%3D) over the span of this project.
<br />
<br />

## Table of Contents
<a href="#community_period">GSOC Community Bonding period</a>   
<a href="#coding_period">GSOC Coding period</a><br /> 
<span>&#8226;</span> <a href="#coding_period_weekone">Week One</a><br /> 
<span>&#8226;</span> <a href="#coding_period_weektwo">Week Two</a><br /> 
<span>&#8226;</span> <a href="#coding_period_weekthree">Week Three</a> <br /> 
<span>&#8226;</span> <a href="#coding_period_weekfour">Week Four</a><br /> 
<span>&#8226;</span> <a href="#coding_period_weekfive">Week Five</a><br />
<span>&#8226;</span> <a href="#coding_period_weeksix">Week Six</a><br /> 
<span>&#8226;</span> <a href="#coding_period_weekseven">Week Seven</a><br /> 
<span>&#8226;</span> <a href="#coding_period_weekeight">Week Eight</a><br /> 
<span>&#8226;</span> <a href="#coding_period_weeknine">Week Nine</a><br /> 
<span>&#8226;</span> <a href="#coding_period_weekten">Week Ten</a><br /> 
<span>&#8226;</span> <a href="#coding_period_weekeleven">Week Eleven</a><br /> 
<span>&#8226;</span> <a href="#coding_period_weektwelve">Week Eleven</a><br /> 


<h3 id="community_period">GSOC Community Bonding period</h3>
I attended my first meeting with my mentors, other students who would be working on project under DBpedia, and their mentors. We all gave our introductions and share about the amazing and exciting projects that all of us would be pursing as a part of GSoC 2022. I enjoyed talking with everyone and am very excited and ready to start with the coding period for my project. <br> 

<h3 id="coding_period">GSOC Coding period</h3>

<h4 id="coding_period_weekone">Week one</h4>
I had a meeting with my mentors discussing more about my skills and about what tech-stack to we plan to use for the project.<br />
<ol>
    <li>Decided on new usecases/examples on how the future chatbot system.</li>
    <li>Went through the current system and made a holistic picture of it on <a href="https://github.com/UditArora2000/GSoC2022_Question_Answering#:~:text=Visualization%20of%20the%20current%20QA%20system%3A">Github</a>.<br />
    I created a Github repository and added the initial README.md file. I created a diagram of the current chatbot system using <a href="https://mermaid-js.github.io/mermaid/#/">Mermaid</a>.</li>
    <li>Completed the <a href="https://cloud.google.com/dialogflow/es/docs/tutorials/build-an-agent">Dialogflow tutorial</a> to learn about the implementation details.<br />
    I learned about how to create and customize agents, how to create intents with parameters, and how to create fulfillment using webhook.</li>
    <li>Read more on Function as a Service (<a href="https://www.sumologic.com/glossary/function-as-a-service/">FaaS</a>).<br />
    I got to know how it supports a server-less architecture and its impact on system scalability.</li>
</ol>


<h4 id="coding_period_weektwo">Week two</h4>
I had a meeting with my mentors where we dicussed the <a href="https://github.com/dbpedia/dbpedia-chatbot-frontend/issues/1">issues</a> I would be working on this week.<br />
<ol>
    <li>Evaluated the query "tell me an order of components list" and how it is handled by the current system.</li>
    <li>Composed SPARQL queries to extract entities recognized by the system<br />
    I encountered a bug in my queries, which I hope to get resolved in the next meeting.<br /></li>
    <li>Suggested new textual questions, that would help to enhance the user experience</li>
    <li>Tried to setup the chatbot locally on my system</li>
</ol>
I encountered errors in connecting with the server where the chatbot is hosted. I hosted the chatbot on heroku to be added as webhook for the fulfillment on the Dialogflow agent.

<h4 id="coding_period_weekthree">Week three</h4>
I had a meeting with my mentors where we dicussed the <a href="https://github.com/dbpedia/dbpedia-chatbot-frontend/issues/4">issues</a> I would be working on this week.<br />
<ol>
    <li>Resolved the doubt in my SPARQL query with the help of my mentors during the meeting</li>
    <li>Tried to setup the chatbot locally with some fixes suggested by the mentors<br />
    The app is still unable to reach the server</li>
    <li>Created three new intents on dialogflow based on the previously suggested textual questions</li>
</ol>

<h4 id="coding_period_weekfour">Week four</h4>
<ol>
    <li>Tried to get the RDF visualizer running</li>
    <li>Figured out there a server error, and a new Question Answering server had to be used for the fetching the graph information</li>
</ol>

<h4 id="coding_period_weekfive">Week five</h4>
<ol>
    <li>Fixed bugs in the SPARQL query of RDF visualizer that was fetching the annotations of the question</li>
    <li>Fixed a hosting bug by changing the host from localhost to a non-routable meta-address</li>
    <li>Got the final RDF visualizer running. Tested the sample graph. The service was hosted on the server</li>
</ol>

<h4 id="coding_period_weeksix">Week six</h4>
<ol>
    <li>Fixed the SSL configuration files</li>
    <li>Fixed bugs in the Webhook, hosted it using ngrok and got the Dialogflow API to get responses from the webhook</li>
</ol>

<h4 id="coding_period_weekseven">Week seven</h4>
<ol>
    <li>Tested the webhook responses</li>
    <li>Spotted multiple errors and unexpected behavior from the webhook implementations of the intent functionalitites</li>
    <li>Iterated through intents to test out their behavior and make appropriate fixes where necessary</li>
</ol>

<h4 id="coding_period_weekeight">Week eight</h4>
<ol>
    <li>Spotted and fixed multiple intents with functionalities in the webhook, but missing implementation on Dialogflow</li>
    <li>Started writing test cases in Javascript to add to the explainability of the QA pipeline</li>
    <li>Beutified the existing code base by fixing typos and enuring overall consistency by following naming conventions</li>
</ol>


<h4 id="coding_period_weeknine">Week nine</h4>
<ol>
    <li>A decision to shift to Python was made to ensure consistency across the Webhook and RDF Visualizaer</li>
    <li>Accordingly started converting the entire code to Python</li>
</ol>

<h4 id="coding_period_weekten">Week ten</h4>
<ol>
    <li>Converted majority of the Webhook functionality to Python</li>
    <li>Encountered errors in getting the appropriate graph id from the Qanary questions answering API</li>
</ol>

<h4 id="coding_period_weekeleven">Week eleven</h4>
<ol>
    <li>Wrote test cases for the implemented Webhook functionality</li>
    <li>Rearranged the code base for better readibility</li>
</ol>

<h4 id="coding_period_weektwelve">Week twelve</h4>
<ol>
    <li>Performed final finishing touches to the code</li>
    <li>Documented the progress in my GSoC project</li>
</ol>


Overall, I had an amazing time working on this project. I learnt a lot while working on this project and enjoyed overcoming the difficulties. I would like to thank all my mentors for constantly being their to help me and guide me throughout this project. I hope to stay in touch with them and continue contributing to DBpedia and to open source.