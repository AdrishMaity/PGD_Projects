Problem Statement
With the evolution of Deep learning in Natural Language, many of the complicated tasks have now become way simpler. The traditional models using RNN(Recurrent Neural network) were not good enough to handle difficult tasks in Language modelling. One of such difficult tasks in NLP is reading comprehension. 

 

Imagine, for any given passage or comprehension, you can ask different questions related to it.  The language model will present you with correct answers through a short extract from the passage. Let’s say if we provide this paragraph to the model and ask “what is the most difficult task in NLP “. In reply to this the model will provide “reading comprehension” as the answer

Your task in this capstone is to create a transformer based model which can give answers to any question asked for the given passage. This problem statement is an application of Deep learning with NLP through the state of art model - Transformers. For this application you will be using a pre-trained model BERT(Bidirectional Encoder Representations from Transformers) for language generation. 

 

In this capstone you will look at the particular type of extractive QA that involves answering a question about a passage by highlighting the segment of the passage that answers the question.

 

Problem statement: To fine-tune a BERT model which predicts a start position and an end position in the passage in context to a aksed question.

We will use the Stanford Question Answering Dataset (SQuAD) 2.0 for this task.

 


At the end of this capstone, you will also deploy the project using Heroku to visualize the result of your model.

 

 

Project Pipeline
The project pipeline can be briefly summarized in the following four steps:

Data Understanding: Here, you need to load the data and convert it into parallel lists of contexts, questions, and answers.
Data processing: In this step, you will extract token positions where answers begins & ends for train & validation data. Once done you need to tokenize the context/question pairs along with converting each character start/end positions to token start/end positions.
Train/Test Split: Now your data will be ready. Under this step you need to create Train & Test datasets using Tensorflow Data api. 
Model-Building & training: Here you  need to import the pre-trained model - DistilBERT and define loss & optimiser functions for training the model.