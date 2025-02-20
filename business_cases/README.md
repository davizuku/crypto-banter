# Crypto School - Business Cases

## Proposals

Please review overview of Crypto School and suggest 3 highlevel AI related solutions you would
recommend that are befitting in our business and why we should consider these as viable options.

Here are my proposals:

1. **Automatic grader chatbot**
    - **What**: An conversation-like interface capable of establishing the grade of potential students so that they can directly start on their appropriate level.
    - **Why**: Someone accessing the crypto school for the first time might be a bit overwhelmed by the number of options, or a bit unsure about which course to choose.
    - **Viability**: It directly improves the front of the funnel of potential students and streamlines new subscriptions. Also, students will be happier accessing a course matching their level of expertise, and avoids frustration of having acquired the wrong course.
2. **Personalized Learning Recommendations**
   - **What:** An AI-driven recommendation engine that curates personalized course content and learning paths for each student.
   - **Why:** Leveraging historical data, this solution increases engagement and retention by tailoring content to each user’s interests and learning pace.
   - **Viability:** It directly improves the student experience, leading to higher course completions and customer satisfaction.
3. **AI-Powered Virtual Assistant for Student Support**
   - **What:** A chatbot/virtual assistant that uses Natural Language Processing (NLP) to handle common support queries across your website and social channels (X, Facebook, YouTube).
   - **Why:** By automating FAQs and basic support tasks, this solution reduces the workload on your Customer Support Agents and ensures quick, consistent responses.
   - **Viability:** Faster response times and lower operational costs can drive higher customer satisfaction, while the solution can easily scale with growing student numbers.


## 30-60-90 plan for "Automatic grader chatbot"

### 30-Day Plan: Discovery & Requirements Gathering

#### Objectives:
- Understand the scope and define key requirements.
- Establish baseline metrics and gather necessary data.
- Prototype a conversational flow.

#### Key Actions:
- **Stakeholder Meetings:**
  - Organize a kick-off meeting with key stakeholders (Product Manager, Director: Talent and Operations, Customer Support, and Data Analyst) to align on objectives and expectations.

- **Requirements Gathering:**
  - Identify common student pain points during initial course selection.
  - Review existing enrollment data and historical assessment patterns to determine key grading criteria.
  - Define success metrics (e.g., reduction in course mismatch, increased conversion rates, improved student satisfaction).

- **Data & Technology Review:**
  - Audit existing data sources (Mixpanel, SQL, Google Analytics, BigQuery) for historical student behavior and course enrollment.
  - Evaluate available chatbot frameworks and NLP tools (e.g., Rasa, Dialogflow, or custom solutions built with Python and FastAPI).

- **Initial Conversation Flow Design:**
  - Draft a conversation script that includes screening questions to gauge student knowledge.
  - Map out decision trees for directing students to beginner, intermediate, or advanced courses.

#### Success Metrics:
- Completion of a detailed requirements document.
- A basic conversational flow prototype and initial FAQ list.
- Stakeholder approval to move into development.


### 60-Day Plan: Prototype Development & Pilot Testing

#### Objectives:
- Develop an MVP version of the chatbot.
- Integrate the MVP with existing systems for a pilot test.
- Collect and analyze user feedback.

#### Key Actions:
- **Development of MVP:**
  - Implement the chatbot using the chosen tech stack (e.g., Python, FastAPI, and an NLP framework).
  - Build the conversation engine based on the defined flow and grading criteria.
  - Connect the chatbot to internal data sources (e.g., CRM or enrollment databases) to personalize the experience.

- **Integration & Testing:**
  - Integrate the chatbot with the front-end (website and/or social channels).
  - Perform internal QA tests to ensure the chatbot accurately grades users and suggests appropriate courses.
  - Set up logging and analytics to track interactions, response times, and decision accuracy.

- **Pilot Launch:**
  - Roll out the chatbot to a controlled subset of new users.
  - Collect qualitative and quantitative feedback regarding usability, accuracy of grading, and overall user experience.

#### Success Metrics:
- A working MVP that successfully interacts with pilot users.
- Reduction in the time users spend selecting a course.
- A measurable improvement in user satisfaction from pilot feedback (target >70% positive responses).

### 90-Day Plan: Full Rollout & Optimization

#### Objectives:
- Refine and optimize the chatbot based on pilot feedback.
- Deploy the chatbot across all relevant channels.
- Monitor performance and continuously improve the system.

#### Key Actions:
- **Feedback Incorporation & Optimization:**
  - Analyze pilot data and adjust the conversation flow and grading algorithms as needed.
  - Enhance the NLP model using machine learning techniques trained on pilot interactions and historical data.

- **Full Deployment:**
  - Integrate the refined chatbot into the main website and any other channels (e.g., mobile app, social media).
  - Ensure seamless integration with existing systems like CRM and course management platforms.
  - Develop comprehensive documentation and provide training for Customer Support teams to handle escalations.

- **Monitoring & Iteration:**
  - Set up dashboards using Mixpanel, Google Analytics, and BigQuery to track key metrics (conversion rates, student satisfaction, course match accuracy, and chatbot response times).
  - Establish a feedback loop for ongoing improvements and schedule periodic reviews (weekly/monthly) with all stakeholders.
  - Plan for future enhancements such as multilingual support or integration with additional data sources.

#### Success Metrics:
- Full deployment with consistent performance across channels.
- Achieving a sustained resolution rate (accurate grading) above 70%.
- Demonstrable improvements in new subscription conversion rates and a reduction in course mismatch incidents.
- Documented increases in student satisfaction scores and reduced onboarding time.
