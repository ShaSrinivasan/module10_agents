# Week 11 answers

## Exercise 1
1. The message the customer never saw: The system message
2. How many times the customer has spoken: Twice
3. Can the model tell that the last reply came from the order tool? Why does that matter? : No they cannot, In the history every reply has the role assistant, whether a rule, a tool, or the model wrote it. The model reads the whole history, so it can copy the pattern of an earlier tool answer and state something the tool never said.
4. The customer now types "thanks". How many messages are sent on the next call?:  Six 



Exercise 4: Sunny: The store now closes at 11 pm.

A reply like this could be detrimental to customer satisfaction, and false answers like this could also allow users to create more problems. Facts that should never come from the model should include prices, refunds and anything to do with money. They could have major consequences on a business if not controlled.