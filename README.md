# ECS171_Group7

**Group 7:** Akshita Gandra, Amy Cu, Austin Mayerhofer, Brandon Aranzamendez, David Jimenez, Lei Chen, Lukas Nixon, Zhecheng Huang, Zonghan Yue

# Topic: Predicting California Forest Fires

## Project Goal: 
To identify correlations between weather attributes (e.g. temperature) and the area burned in forest fires to predict the anticipated burn area of California fires given existing weather data. We are using the UCI Forest Fires dataset (517 * 13) to create, test, & train our model (likely polynomial, logistic, or linear regression). We will also use CA Environment Dataset (128126 * 19), CA WildFire Incidents Dataset (1636 * 40), and pull weather data of specific fires to further test & train our model.

## Timeline, Responsibilities, & Milestones:

### Data Management & Data Visualization— Weeks 3-4: Leads: Amy & David
Data preprocessing to filter relevant and meaningful data and data visualization to generate graphs of classification / regression patterns. Matching various datasets to work together.

#### Milestones (Week 3-4): 
- Preprocessing (Cleaning up data to remove irrelevant / missing instances, outliers)
- Exploratory data analysis (Identifying possible trends, Testing correlation, etc.)
- Visualization (Linear, Polynomial, or Logistic regression graphs)

### SWE & UI/UX— Weeks 4-8: Leads: Lei & Zhecheng
Develop a static web page to show design style and develop front-end and back-end features for the web app to present the project. Work with the ML team and satisfy their needs.
- Node.js and html
- Predict the area being affected based on the model created from Machine Learning group

#### Milestones:
- End of week 4 — static design demo.
- End of week 5 — list of functionalities (e.g. way data shows, interactive parameters, etc.) 
- End of Week 8 — a dynamic interactive design.

### Machine Learning & Algorithms — Weeks 3-8  Leads: Luka & Zonghan 
Develop machine learning models to predict and form conclusions based on the training dataset.

#### Milestones:
- Week 4 - Finding the suitable target as dependent variable + identify problem
- Week 4 - Ensure Data is complete and thorough.
- Week 5 - Decide how data will be partitioned into training and test data (80/20)
- Week 5-6 - Design the proper algorithms. (Polynomial regression, KNN or the Decision Tree) using sklearn, pytorch.aa 
- Week 6-8 - Try to use a Neural Network to increase the accuracy of the prediction.
- Week 6-8 - Combining different results from our algorithms and choosing the best model.
- Week 6-8 - Prevent the model from overfitting training data.

### Quality Assurance — Weeks 6-8   Leads: Austin & Brandon
Evaluate accuracy of model, efficiency of model, scout for bugs in the software development backend/UI frontend, evaluate data visualization to ensure data is accurately presented
#### Evaluation metrics to determine best ML model:
- Area Under Curve, F1 Score, etc.
- Consider training time
- Depends on classification/regression
#### Milestones: 
- Weeks 3-5 researching metrics
- Weeks 6-8 putting metrics into practice

### Project Management — Weeks 2-8: Project Lead: Akshita Gandra
Time management, communication, Trello Kanban board, meetings, assign responsibilities, etc.  

## Resources:
### Portugal Forest Fires Dataset
https://archive.ics.uci.edu/ml/machine-learning-databases/forest-fires/
### California Wildfires Dataset (1636 rows x 40 columns)
https://www.kaggle.com/ananthu017/california-wildfire-incidents-20132020 
### California Weather and Environment Dataset
https://www.kaggle.com/chelseazaloumis/cimis-dataset-with-fire-target 
### Weather data
https://www.weather.gov/
### Web App: 
url: https://ecs171-group7.glitch.me
