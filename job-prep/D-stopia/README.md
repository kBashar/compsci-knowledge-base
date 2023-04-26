## 1. Data extractor from News Article
Language: Python  
Frameworks: LangChain  
DataBase: PostgreSQL  
### Learning Goals  
* Relational Database
  * Indexing
  * ORMs
  * ACID
  * Transactions
  * N+1 problems
  * Normalization
  * Failure Modes
  * Profiling Performance
* LangChain data extraction
* Authentication
* Perodic Task execution (Celery)
* REST API (Django, DRF)
* Microservice
* GraphQL
* Message Queue (Redis)
* Web Crawling (Selenium, BeautifulSoap)
* Document Database for storing Articles (MongoDB)

### Task Breakdown  
1. Article Aquisition by web crawling
2. Periodic Article Aquisition
3. Article categorisation or labeling using word frequency or some pretrained models
4. Article Storage in Document DB
5. Article information extraction
   1. Incident Metadata extraction
   2. Incident Location extraction
6. Incident Identification
7. Incident Data store in Relational DB
8. REST API for Incident data access
9. Authentication & Authorization for REST API
10. Design and Develope Incident Map

#### 1. Article Collection
1. Write crawlers for DS, TBS, DT
2. Two kind of crawlers
   1. Article List crawler
   2. Article crawler
3. Run periodic crawler
4. Store Articles in MongoDB
5. Develope an Interface to level articles