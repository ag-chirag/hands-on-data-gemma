RAG_IN_CONTEXT_PROMPT = """
Given a QUERY below, your task is to come up with a maximum of 25
STATISTICAL QUESTIONS that help in answering QUERY.

Here are the only forms of STATISTICAL QUESTIONS you can generate:

1. "What is $METRIC in $PLACE?"
2. "What is $METRIC in $PLACE $PLACE_TYPE?"
3. "How has $METRIC changed over time in $PLACE $PLACE_TYPE?"

where:
- $METRIC should a publicly accessible metric on societal topics around
  demographics, economy, health, education, environment, etc.  Examples are
  unemployment rate, life expectancy, etc.
- $PLACE is the name of a place like California, World, Chennai, etc.
- $PLACE_TYPE is an immediate child type within $PLACE, like counties, states,
  districts, etc.

Your response should only include the questions, one per line without any
numbering or bullet!  If you cannot come up with statistical questions to ask,
return an empty response.

NOTE:  Do not repeat questions.  Limit the number of questions to 25.

If QUERY asks about  multiple concepts (e.g., income and diseases), make sure
the questions cover all the concepts.

[Start of Examples]

QUERY: Which grades in the middle school have the lowest enrollment in Palo Alto?
STATISTICAL QUESTIONS:
What is the number of students enrolled in Grade 6 in Palo Alto schools?
What is the number of students enrolled in Grade 7 in Palo Alto schools?
What is the number of students enrolled in Grade 8 in Palo Alto schools?

QUERY: Which industries have grown the most in California?
STATISTICAL QUESTIONS:
How have jobs in agriculture changed over time in California?
How has GDP of agriculture sector changed over time in California?
How have jobs in information and technology changed over time in California?
How has GDP of information and technology sector changed over time in California?
How have jobs in the government changed over time in California?
How has GDP of the government sector changed over time in California?
How have jobs in healthcare changed over time in California?
How has GDP of healthcare sector changed over time in California?
How have jobs in entertainment changed over time in California?
How has GDP of entertainment sector changed over time in California?
How have jobs in retail trade changed over time in California?
How has GDP of retail trade sector changed over time in California?
How have jobs in manufacturing changed over time in California?
How has GDP of manufacturing sector changed over time in California?
How have jobs in education services changed over time in California?
How has GDP of education services sector changed over time in California?

QUERY: Which state in the US has the most asian population?
STATISTICAL QUESTIONS:
What is the number of asian people in US states?

QUERY: Do specific health conditions affect the richer California counties?
STATISTICAL QUESTIONS:
What is the median income among California counties?
What is the median house price among California counties?
What is the prevalence of obesity in California counties?
What is the prevalence of diabetes in California counties?
What is the prevalence of heart disease in California counties?
What is the prevalence of arthritis in California counties?
What is the prevalence of asthma in California counties?
What is the prevalence of chronic kidney disease in California counties?
What is the prevalence of chronic obstructive pulmonary disease in California counties?
What is the prevalence of coronary heart disease in California counties?
What is the prevalence of high blood pressure in California counties?
What is the prevalence of high cholesterol in California counties?
What is the prevalence of stroke in California counties?
What is the prevalence of poor mental health in California counties?
What is the prevalence of poor physical health in California counties?


[End of Examples]

QUERY: {question}
STATISTICAL QUESTIONS:
"""