# DBpedia eXplainable Chatbot (DBpedia XChat) 
Hello everyone! I am Muskan Kothari, a participant in the Google Summer of Code 2023 program working with DBpedia. I am thrilled to be a part of this prestigious program and contribute to the DBpedia organization. As a Computer Science student, I am passionate about Big Data, NLP, and DevOps.

Throughout this summer, my project aims to build and enhance the [DBpedia eXplainable chatbot](https://forum.dbpedia.org/t/dbpedia-explainable-chatbot-dbpedia-xchat-gsoc-2023/2077) that provides answers that are explainable in terms of intermediate steps, queries, resources in DBpedia. I am excited to share my progress and achievements during each week of this program.

Now, let's dive into my weekly progress report!<br/>

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
<span>&#8226;</span> <a href="#coding_period_weektwelve">Week Twelve</a><br /> 


<h3 id="community_period">GSOC Community Bonding period</h3>
I attended my first meeting with my mentors, other students who would be working on project under DBpedia, and their mentors. We all gave our introductions and shared about the amazing and exciting projects that all of us would be pursing as a part of GSoC 2023. It was great connecting with the community and the interests that is being pursued in the developments taking place. I was ready to start with the coding period for my project. <br> 

<h3 id="coding_period">GSOC Coding period</h3>

<h4 id="coding_period_weekone">Week one</h4>
I had a meeting with my mentors discussing more about the project, grey areas, mode and frequency of communication, clarification of the approach wherever necessary and gaining access to the repositories and project board. All the tasks were created as issues and updated on the project board.<br />
<ol>
    <li>Went through the current system, code flow, analysed the current code base and compared it with the code bases from previous years (<a href="https://github.com/UditArora2000/GSoC2022_Question_Answering#:~:text=Visualization%20of%20the%20current%20QA%20system%3A">2022</a> , <a href="https://github.com/dbpedia/chatbot-ng">2021</a>) .<br />
    Updated the main Github repository in DBpedia with the code from GSoC 2022 contributions.</li>
    <li>Analysed the code in <a href="https://github.com/dbpedia/dbpedia-chatbot-backend/tree/main/dbpedia_website">Dbpedia website folder</a> to further decide on restructuring the repositories.<br /></li>
</ol>


<h4 id="coding_period_weektwo">Week two</h4>
I had a meeting with my mentors where we dicussed the updates on the <a href="https://github.com/dbpedia/dbpedia-chatbot-backend/issues">issues</a> created.<br />
<ol>
    <li>Discussed the findings on what is contained in the website folder and concluded on whether to remove it and restructure.</li>
    <li>Removed the dbpedia website folder.<br /></li>
    <li>Compared the main repo and with previous years to analyse whether the code is updated/duplicated. Went through the Webhook and rdf_visualization folders and noted the findings.</li>
</ol>

<h4 id="coding_period_weekthree">Week three</h4>
I had a meeting with my mentors where we dicussed the findings on the uptodateness of the main repository with the previous years codebase and the <a href="https://github.com/dbpedia/dbpedia-chatbot-backend/issues">issues</a> I would be working on this week.<br />
<ol>
    <li>Concluded on which folders to remove. Further instructed to import the Dialogflow agent and test in a new Dialogflow project.</li>
    <li>Started working on dockering two backend services - Webhook and rdf_visualization<br />
    Created two Dockerfiles and tested by running the application on local server.</li>
    <li>Fixed the errors while dockerising the services and updated dependencies.</li>
    <li>Completed dockerising the backend services, added details about running the .sh files to dockerise and rung the services. Tested the applications. Merged the PR of Dockerfiles.</li>
</ol>

<h4 id="coding_period_weekfour">Week four</h4>
<ol>
    <li>Analysed and understood the .yml file for GitHub Actions. </li>
    <li>Completed the build workflow for building and pushing the two Docker images. Fixed the errors.</li>
</ol>

<h4 id="coding_period_weekfive">Week five</h4>
<ol>
    <li>Started working on deploy workflow for building and pushing the two Docker images. Fixed the errors.</li>
    <li>Formatted all Python and JSON files on PEP8 guidelines. </li>
</ol>

<h4 id="coding_period_weeksix">Week six</h4>
<ol>
    
</ol>

<h4 id="coding_period_weekseven">Week seven</h4>
<ol>
   
</ol>

<h4 id="coding_period_weekeight">Week eight</h4>
<ol>
    
</ol>


<h4 id="coding_period_weeknine">Week nine</h4>
<ol>

</ol>

<h4 id="coding_period_weekten">Week ten</h4>
<ol>
    
</ol>

<h4 id="coding_period_weekeleven">Week eleven</h4>
<ol>
    
</ol>

<h4 id="coding_period_weektwelve">Week twelve</h4>
<ol>
</ol>


Overall, I had an amazing time working on this project. I developed and improved various skills in different frameworks by progressively overcoming the challenges. The experience raised the level of understanding the way open source works and the power of community in an open source organisation. I would like to thank all my mentors for constantly being their to help me and guide me throughout this project.