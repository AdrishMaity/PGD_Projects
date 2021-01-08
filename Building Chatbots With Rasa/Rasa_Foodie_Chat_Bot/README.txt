Foodie : A Zomato Chat Bot
================================

The bot is build using RASA Open Source. It searches restaurants across Tier 1 and Tier 2 cities in India using Zomato API. 
Once a search is complete it displays top 5 resturants from Zomato in descending order of Ratings and asks for user confirmation of sending the information via email. 
If user provides email address to the bot it sends top 10 restaurants with price and ratings in tabular format to the address.

Python modules:
-----------------
All the required python packages are listed inside requirements.txt file. Python version 3.7.6 is used for this project.

Configuration of RASA Bot: the config.yml file
==============================================
pipeline:
---------
--> SpacyNLP (case_sensitive: False) : When retrieving word vectors, this will decide if the casing of the word is relevant. E.g. hello and Hello will retrieve the same vector.
--> SpacyTokenizer: Creates tokens using the spaCy tokenizer.
--> SpacyFeaturizer: Creates features for entity extraction, intent classification, and response classification using the spaCy featurizer.
--> RegexFeaturizer: Creates a vector representation of user message using regular expressions.
--> CRFEntityExtractor: Learn custom entities in any language, given some training data.
--> EntitySynonymMapper: Maps synonymous entity values to the same value.
--> SklearnIntentClassifier: The sklearn intent classifier trains a linear SVM which gets optimized using a grid search.

policies:
---------
--> TwoStageFallbackPolicy: handles low NLU confidence in multiple stages by trying to disambiguate the user input. (nlu_thresholds: 0.5, core_threshold: 0.4)
--> AugmentedMemoizationPolicy (max_history: 10): It works the same way as the MemoizationPolicy, but if no exact match is found it additionally has a mechanism that forgets a certain amount of steps in the conversation history to find a match in stories.
--> TEDPolicy: The Transformer Embedding Dialogue (TED) Policy. (epochs: 50, hidden_layers_sizes: [16,8], max_history: 10, batch_size: [4,8])
--> MappingPolicy: The MappingPolicy can be used to directly map intents to actions.

Email Configuration: The email is configured with gmail credentials which can be generated from https://myaccount.google.com/apppasswords
=====================

Slack configuration in credentials.yml: slack_token has been generated from https://api.slack.com/ by creating new app.
=======================================

Training Instruction
======================

Train RASA NLU only --> rasa train nlu

Train RASA CORE only --> rasa train core

Train both nlu and core --> rasa train --data data -d domain.yml --force -vv

Executing the Chat Bot
=======================
Start RASA Action Server --> rasa run actions -vv --debug

Start RASA Shell --> rasa shell -m models/<< model_file >>.tar.gz

Start RASA NLU --> rasa run nlu

======================================
Authors: Adrish Maity, Sachin Malusare
======================================

