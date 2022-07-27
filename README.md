# Quantum Machine Learning Workshop | ADC 2022

Repository for the materials for the exercises developed during the Quantum Machine Learning Workshop, Applaudo Studios' ADC 2022.

During this workshop we will be implementing the following Machine Learning algorithms:
* Linear Regression
* K-means

And train, validate and test these models harnessing a Quantum Computer.

## Quantum Comuting and Machine Learning Theory and Concepts

In order to understand the implementations of these algorithms it is recommended (but not mandatory) to know a little bit of each of these and the basics of Quantum Computing to understand what is happening behind the scenes. If you don't know these concepts as of yet do not worry, you can totally carry out the workshop without them, but I do suggest to do some further reading to understand what has been implemented. I will try to explain them in a simple manner so that we may begin the implementations.

1. **Machine Learning**: branch of AI whose purpose is to develop methods to enable machines to learn on their own. OK, cool Rodrigo, but what are *methods*? Well, since this is an introduction and we are speed running theory, it is beyond the scope of the workshop to explain in detail these methods, I'll leave some links in the refereces sections for further reading. Nonetheless, know that in essence these employ 2 fundamental elements: large volumes of data and algorithms that mimic how human beings learn, thus, graudally improving the results. at the end of the day, Machine Learning produces "trained" algorithms called models. "What is this *training* process?" you may ask. It is fairly simple, let's recall our algebra I classes. We had a function $y = mx + b$. This is the basis of all ML models, an equation that tries to predict the value of variable $(y)$ given variable $x$ and a bias $b$. So the model learns the optimal value of $m$ through a bunch of data points.
