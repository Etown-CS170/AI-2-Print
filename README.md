# AI-2-Print

### Author: Phillip G.

AI-2-Print would be a Text to File program that will generate a STL model which can be used to
generate GCode that then can be used to 3D print the generated model.

**Users** :

- 3D printing hobbyists who want to print generated models
- 3D modelers and artists who want to build a model for a foundation
- Engineers and hobbyists who are brainstorming concepts for a project
- 
**Motivation** :
- AI-2-Print would make 3D printings and 3D modeling more enjoyable, adding a pathway
from start to finish. It would give beginner and advanced users a foundation to build on
- It would provide me personally a new aspect of my 3D printing hobby that I have been
involved in for 8 years

**Features** :
- User provides a text prompt that describes what they are looking for in the STL model
- The AI will be properly setup knowing that the user wants 3d model data
o This will avoid confusion as the user will not want instructions on how to model in
CAD software or anything unrelated to generating the STL
- AI-2-Print will use Sharp-E and OpenAI: https://github.com/openai/shap-e
- Generate/Render an image of the 3D model generated
- I might try to find a way to generate a GCode file if a user provides a printer profile or .fff file

It is important to keep expectations realistic since it is a one-person project with time constraints.
The goals that I think are most achievable for this project are the following:

1. Text prompt to STL Generation Functionality (No GUI)
2. Programing System Message for Optimal User Experience and to Keep functionally
    consistent.
3. Make Program Output to an organized file structure and render an image for each model.


