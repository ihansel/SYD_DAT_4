# SYD DAT 5 Lab 1 - Git and Markdown

##Homework:
* Read about some [Markdown Techniques](http://daringfireball.net/projects/markdown/syntax)

##### Analyzing the Analyzers
###### Task: Write down 5 key points you took away from the article
Read [Analyzing the Analyzers](http://cdn.oreillystatic.com/oreilly/radarreport/0636920029014/Analyzing_the_Analyzers.pdf) for a useful look at the different types of data scientists. Write down 5 key points you took away from the article
* Survey mid-2012 of Data Scientist, four clusters: Data Business people, Data Creatives, Data Developers and Data Researchers. Aim to help define a newly burgenoing field, to set expectations around roles 
* Based on survey data, clustering self-identified skill areas
* Business, Creative/Hackers, Developers & Researchers
* T-shaped data scientists; the horizontal line in T the bredth of skills with one area of deep expertise (vertical line). Ref to the DS Venn diagram by Conway. The Business, REsearcher and Developer clusters seem to fit T pattern, the Creatives less so, perhaps because their skill is in being generalists
* Concluding section Examines educational backgrounds, place in org structure and a discussion on career paths. Rotation among different business teams suggested to hone business understanding/operation.

##### The Data Science Handbook: George Roumeliotis on 'How to develop Data Science skills'
###### Task: Write a summary of a chapter of [The Data Science Handbook](http://www.thedatasciencehandbook.com/) in Markdown and submit a pull request in the Lab Directory
* George is an Australian with a PhD in applied mathematics from USyd, entrepaneur associated with numerous tech companies, tech business history starting from before 90's .com crash. Bayesian image processing techniques for astronomical images
* Considers a good Data Scientist to be like a swiss army knife: advanced statistics, machine learning, SQL & Hadoop,
a mainstream programming language, combo of applied maths and CS + business understanding. 
* Difference between a data gopher and a data scientist is in the business understanding
* Learning R is important, he says it's 'kind of ugly' but the lingua franca - stay away from commercial proprietary packages - I read into this Matlab, ugh. 

| Skill                           | Weighting | Me                                        |
|---------------------------------|-----------|-------------------------------------------|
| SQL                             | 40%       | 7/10                                      |
| Hadoop                          | 30%       | 0/10                                      |
| R                               | 15%       | 0/10                                      |
| Mainstream programming language | 10%       | 5/10 (10yrs exp. non-mainstream language) |
| Mainstream scripting language   | 5%        | 8/10                                      |

* The most useful insight for me was about how academics communicate; George writes about how academics are deeply involved in process and communicate it linearely whereas business stakeholders want the main insights straight away - that resonated with me greatly as a corporate designer with an academic background: I go into too much detail when justifying design decsisions. 
* The comments about efficiency and results over 'knowledge for knowledge sake' again resonate, it's very easy to get wrapped up in a design or analytics problem because it is inherently interesting rather than interesting *and* useful. He also expands on this by saying 'don't fall in love with your ideas. Market feedback is the only thing that matters" (sic) - in Data Science, lol 
* Building relationships with non-technical stakeholders important, speak to all sorts of people, good advice for life too.
* Importance of business process, IMO Data Science and Buisness Analysts seem very close, with the former unleasing awesome data skills into their craft. Business understanding also very important for good designers. 
* "A successful data scientist changes the world around them" noice, likewise a sucessfull designer - however, the ethics and character of the Data Scientist is what makes this statement either good or bad.
* George says his CS degree didn't impart team work skills, I wonder if this is different now-a-days, group work was a constant in my undergrad uni experience, and seemed even more present when I got to teach some classes, however that was not in CS field. 
* Future: an explosion of consumer and enterprise apps built on data science - completely agree - there are so many interesting things sitting in the masses of data we are collecting but not looking at.

##### Project ideas
N.B - used a markdown table generator for below: http://www.tablesgenerator.com/markdown_tables
    
| Project idea                                                                    | Description                                                                                                                                           | Data                                                                                                         | Outcome                                                                                                                       | Model                                                                                                                       |
|---------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------|
| Project Idea 1: Model information seeking styles of customers                   | Model product behaviours of differetn skill levels of SaaS users: e.g. new intermediate and advanced, and the types of tech doc content they seek out | Product and web analytics,Audience/demographic data - incl. role, company/instance/team size                 | Use the analysis to inform info support content in-product and org of docs for the right people and time                      | ISS model, MLR, cluster, predictive model of tech docs needs at different stages.Ę                                          |
|                                                                                 |                                                                                                                                                       |                                                                                                              |                                                                                                                               |                                                                                                                             |
| Project Idea 2: 'Apdex' for technical docs                                      | A performance score for technical docs                                                                                                                | Product and web analytics                                                                                    | Measure ROI on docs content in supporting product use. Identify the types of content that most support customers software use | MLR of product/docs use, NLP, predictive modeling.                                                                          |
| Project Idea 3: Software work flow analysisĘ                                    | Analyse user task flows in a software UI                                                                                                              | Product analytics events, feature task flows scraped from 'how to' step-by-step docs (web)?)                 | Model common user work flows, surface problematic work flows in the product, focus design decisions                           | Markov chains for identifying common task flows. Completion rates and false-starts/errors in performing feature task flows. |
| Project Idea 4Ę: Survey feedback themes and sentiment                           | Use an nlp library to categorise themes in open text survey feedback                                                                                  | Survey/interview comments, reader (internal employee) scoring of sentiment (pos/neu/neg) to train algoryim.Ę | Monitor emerging and changing themes in ongoing survey feedback to prioritise product design decisions                        | NLP, predictive learning, ML.                                                                                               |
| Project Idea 5: UI discoverability index: how easy is it to find the next step? | Look at movement/hover and click time as an index of UI discoverability issues                                                                        | Product analytics events, heatmaps                                                                           | UI discoverability score for a given interface element/task                                                                   | Time/ Distribution statistics, signal detection.                                                                            |
        
