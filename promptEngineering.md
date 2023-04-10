# Prompt Engineering

AI can be used for different parts of education. 
1. Teachers - preparing material (green)
2. Teachers - providing summaries of classroom activities to parents and the ministry. (orange)
3. Students - as a tutor (green)
4. Students - to start the creative process (orange)

## General prompt advice

1. prompts are critical. The model has a working memory. You need to add enough context to the working memory for it to perform better. Give it examples of the type of text you want it to produce. Fill up parts of the context with a role it is playing and an audience.

2. Get it to review its answers. In BingChat, when it gives you an answer you can say “some of the statements you just made might be incorrect. Can you find evidence to support each of the statements and give an estimate of how likely it is to be incorrect?” This self-reflection improves answers significantly

3. Get it to do its own structure. Ask it to give an overview of a task and then ask it to fill in the details of each section. This gives it much better output as it has a goal included in the prompt, a goal that is internally clear.

4. Iterate, iterate, iterate. You need to work with it over multiple prompts to get interesting answers. Do not expect a blank model to give you good responses.

5. LLMs are best at translation and creation, not search. Do not ask it questions about reality, that is what google is for. Ask it to turn bullet points into sentences, or paragraphs into bullet points. Ask it to pretend to be a student and explain a concept to it and see if it understands. This roleplaying is the thing that it is very good at.


## Example prompts

1. Teach me about [topic], using principles, terminology and concepts from [scaffold topic] which I know a lot about. [Integration Example](examples/integrationrugby.md)
