# Quantum Machine Learning Workshop | ADC 2022

Repository for the materials for the exercises developed during the Quantum Machine Learning Workshop, Applaudo Studios' ADC 2022.

During this workshop we will be implementing the following Machine Learning algorithms:
* Linear Regression
* K-means

And train, validate and test these models harnessing a Quantum Computer.

## Quantum Computing and Machine Learning Theory and Concepts

In order to understand the implementations of these algorithms it is recommended (but not mandatory) to know a little bit of each of these and the basics of Quantum Computing to understand what is happening behind the scenes. If you don't know these concepts as of yet do not worry, you can totally carry out the workshop without them, but I do suggest to do some further reading to understand what has been implemented. I will try to explain them in a simple manner so that we may begin the implementations.

1. **Machine Learning**: branch of AI whose purpose is to develop methods to enable machines to learn on their own. OK, cool Rodrigo, but what are *methods*? Well, since this is an introduction and we are speed running theory, it is beyond the scope of the workshop to explain in detail these methods, I'll leave some links in the refereces sections for further reading. Nonetheless, know that in essence these employ 2 fundamental elements: large volumes of data and algorithms that mimic how human beings learn, thus, graudally improving the results. at the end of the day, Machine Learning produces "trained" algorithms called models. 
2. **Model Training**: "What is this *training* process?" you may ask. It is fairly simple, let's recall our algebra I classes. We had a function $y = mx + b$. This is the basis of all ML models, an equation that tries to predict the value of variable $(y)$ given variable $x$ and a bias $b$. So, the model learns the optimal value of $m$ by plotting the euqtion through a bunch of data points (training dataset). In reality, models are much more complicated than this univariable linear function, as you may have more than one input variable $X_{0}$, $X_{1}$, $X_{2}$... thus, having to learn multiple weights for each for each of these input params.
3. **Quantum Computing**: Thinking of atoms and Ant Man. You got the right idea. QC is a type of computing that harnesses the properties of Quantum Mechanics (also known as Quantum Physics) to accelerate computational tasks, particularly useful when it comes to complex calculations. So, to be perfectly clear, quantum computers are very cool, but they are not meant to browse Twitter.
4. **Quantum Machine Learning**: Nothing else than the classical ML we alerady know, but powered by a quantum computer. QML lies at the intersection between ML and QC, and the idea is to speed up ML with QC. It is in all honesty, more of a research area than a technology in production. To be specific, Quantum ML harnesses properties of QC such as Quantum Tunneling to perform tasks like finding optimal values in a loss function. This operation is usually very expensive for a classical computer since the whole domain of the function must be searched, but through Quantum Tunneling searching the domain of the loss function is much faster.

Having established these broad concepts let's dive into the algorithms we will be implemeting:

### Linear Regression

### K-means

### Quantum Regression and Variational Quantum Regression

### Quantum Classification
