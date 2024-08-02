# EducationGPT
## Project Overview
Starting from the roles of teachers and students, the project combines AI applications developed by large language models to reduce costs and increase efficiency for education, making education more intelligent and learning more efficient 

## Project Features:
1. Teachers' Intelligent Performance Analysis:
- Upload transcripts.
- Generate charts and graphs for performance analysis.
- Intelligent insights based on data.

2. Student Online Brushing Tool:

- Practice questions online.
- Get hints and answers for questions.
- Analyze responses and provide feedback.

3. Intelligent Question Generation:

- Generate questions based on simple descriptions.
- Use AI to create a diverse question bank.

4. Intelligent Online Class Summary:
Summarize online classes from provided links.
Enable questions about the summarized content.

5. Learning Plan Development Plugin:
- Develop personalized learning plans.
- Adapt plans based on student progress.

6. Language Essay Grading Plugin:
Grade essays and provide detailed feedback.
Improve writing skills through AI-generated suggestions.

7. Learning Video Recommendation Plugin:
Recommend educational videos from Bilibili.
Match recommendations with the student's learning needs.

8. Heuristic Learning Plugins:
Enhance critical thinking skills.
Provide problem-solving exercises and activities.

## Usage

1. Install the required packages using pip: 
```pip install -r requirements.txt```
2. Run the application using 
```python app.py```
3. Access the application through a web browser at `http://localhost:5000`
4. Use the application features as described in the documentation.

## Project structure
- common: Generic configurations class
- entity: Entity class
- exception: Exception class
- prompt: Encapsulates the prompt message
- resources: resource files
- service: The business layer, which is responsible for the interaction between the app and other methods
- util: Utilities

## Prequisites
- python 3.11
- google gemini/groq api