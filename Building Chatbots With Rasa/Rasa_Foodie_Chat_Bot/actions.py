from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
from rasa_sdk.events import AllSlotsReset
from rasa_sdk.events import FollowupAction
import zomatopy
import json
import send_mail
import pandas as pd
import logging
import re
import random

logger = logging.getLogger(__name__)


class ActionDefaultAskAffirmation(Action):
	"""Asks for an affirmation of the intent if Core threshold is not met."""

	def name(self):
		return "action_default_ask_affirmation"

	def get_fallback_message(self, intent):
		# negative_msg = "Sorry, I am unable to understand"
		message_db = {
			"greet" : {
						"question": "Good to see you", 
						"ans1": "Hello",
						"intent1": "/greet", 
						"ans2": "I want something else",
						"intent2": "/out_of_scope"
					},
			"restaurant_search": {
									"question": "Are you looking for restaurants?", 
									"ans1": "Yes, Please find some restaurant",
									"intent1": "/restaurant_search",
									"ans2": "I want something else",
									"intent2": "/out_of_scope"
								},
			"affirm": {
						"question": "Do you want to continue?",
						"ans1": "Yes",
						"intent1": "",
						"ans2": "No",
						"intent2": "/exit"
					},
			"email": {
						"question": "Are you looking to send email?", 
						"ans1": "Yes",
						"intent1": "Please /email",
						"ans2": "I want something else",
						"intent2": "/out_of_scope"
					},
			"deny": {
						"question": "Are you sure you replied NO to the previous question?", 
						"ans1": "Correct",
						"intent1": "/deny",
						"ans2": "I want something else",
						"intent2": "/out_of_scope"
					},
			"goodbye": {
							"question": "Looking to end the converstaion?", 
							"ans1": "Good bye!",
							"intent1": "/goodbye",
							"ans2": "How may I help you!",
							"intent2": "/greet"
					},
			"out_of_scope": {
								"question": "Sorry I could not understand! Do you want to search a restaurant?", 
								"ans1": "Yes, Please find some restaurant", 
								"intent1": "/restaurant", 
								"ans2": "No", 
								"intent2": "/out_of_scope"
							}
		}
		return message_db[intent]


	def run(self, dispatcher, tracker, domain):
		# get the most likely intent
		last_intent_name = tracker.latest_message['intent']['name']
		last_user_input = tracker.latest_message['text']
		
		print("Intent is-->", last_intent_name)
		if last_intent_name==None:
			# dispatcher.utter_message(tracker)
			# last_bot_msg = ""
			# for idx, event in enumerate(tracker.events[-1::-1]):
			# 	if event.get("event") == "bot":
			# 		last_bot_msg = event.get("text")
			# 		break
			# last_bot_action = tracker.events[-1::-1][idx+1].get('name')

			# # dispatcher.utter_message(text="Can you please rephrase?")
			# tracker.trigger_followup_action('action_revert_fallback_events')
			# return None
			response = {
				"question": "Do you want to continue?", 
				"ans1": "Yes", 
				"intent1": "", 
				"ans2": "No", 
				"intent2": "/exit"
			}
		elif last_intent_name == 'insult':
			dispatcher.utter_message("that's not very nice")
			return None
		else:
			response = self.get_fallback_message(last_intent_name)

			if last_intent_name == 'email':
				# regex = r"[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}"
				regex = r"[a-z0-9!#$%&'*+/=?^_‘{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_‘{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
				email = re.findall(regex, last_user_input)
				if len(email)>0:
					response["ans1"] = "Yes"
					response["intent1"] = "Please email to " + email[0]
			
		
		message = response["question"]
		buttons = [
			{"title": response["ans1"], "payload": '{}'.format(response["intent1"])},
			{"title": response["ans2"], "payload": '{}'.format(response["intent2"])}
		]
		dispatcher.utter_message(text=message, buttons=buttons)

	

class ActionDefaultAskRefresh(Action):
   """Asks for an affirmation of the intent if NLU threshold is not met."""

   def name(self):
       return "action_default_ask_rephrase"


   def run(self, dispatcher, tracker, domain):
       dispatcher.utter_message(text="Can you please rephrase?")


class ActionSearchRestaurants(Action):
	def name(self):
		return 'action_search_restaurants'

	def run(self, dispatcher, tracker, domain):


		csn_avl = tracker.get_slot('csn_avl')
		loc_avl = tracker.get_slot('csn_avl')
		prc_avl = tracker.get_slot('prc_avl')

		if csn_avl=='1' and loc_avl=='1' and prc_avl=='1':

			try:
				config={ "user_key":"055a74902b28407768bfe4d8a64d1ed7"}
				zomato = zomatopy.initialize_app(config)
				loc = tracker.get_slot('location')
				cuisine = tracker.get_slot('cuisine')
				prc = tracker.get_slot('price')
				location_detail=zomato.get_location(loc, 1)
				d1 = json.loads(location_detail)
				# print(d1)
				lat=d1["location_suggestions"][0]["latitude"]
				lon=d1["location_suggestions"][0]["longitude"]
				cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
				results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),20)
				d = json.loads(results)
				rest_name_list = []
				rest_location_list = []
				rest_rating_list = []
				# rest_price_list = []
				if d['results_found'] == 0:
					dispatcher.utter_message("Sorry! No Results")
				else:
					rest_name_list = [restaurant['restaurant']['name'] for restaurant in d['restaurants']]
					rest_location_list = [restaurant['restaurant']['location']['address'] for restaurant in d['restaurants']]
					rest_rating_list = [restaurant['restaurant']['user_rating']['aggregate_rating'] for restaurant in d['restaurants']]
					rest_budg_list = [restaurant['restaurant']['average_cost_for_two'] for restaurant in d['restaurants']]
					try:
						pd.set_option('display.max_colwidth', None)
					except:
						pd.set_option('display.max_colwidth', -1)

					rest_df = pd.DataFrame({'Name':rest_name_list, 'Location':rest_location_list, 'Rating':rest_rating_list, 'Avg. cost for 2 person':rest_budg_list})
					# print(rest_df)
					if prc == "Less than Rs.300":
						rest_df_filter = rest_df[rest_df['Avg. cost for 2 person']<300]
					elif prc == "Between Rs.300 and 700":
						rest_df_filter = rest_df[(rest_df['Avg. cost for 2 person']>=300) & (rest_df['Avg. cost for 2 person']<=700)]
					else:
						rest_df_filter = rest_df[(rest_df['Avg. cost for 2 person']>700)]

					# print(rest_df_filter['Rating'].apply(lambda x: float(x)))
					# rest_df_filter.loc[:,['Rating']] = rest_df_filter[['Rating']].apply(lambda x: float(x))
					rest_df_filter = rest_df_filter.assign(Rating = rest_df_filter['Rating'].apply(lambda x: float(x)))

					rest_df_sorted = rest_df_filter.sort_values(by=['Rating'], ascending=False)

					if len(rest_df_sorted)>0:
						dispatcher.utter_message("-----Here are the top " + cuisine + " restaurants in " + loc + " with avg. budget of " + prc + " Rs. for 2 people-----")
						for row in rest_df_sorted.head(5).iterrows():
							dispatcher.utter_message(row[1]['Name']+" in "+row[1]['Location']+" has been rated "+str(row[1]['Rating'])+"\n")
						dispatcher.utter_message(10*"====")
						return [SlotSet('location',loc),SlotSet('cuisine',cuisine),SlotSet('price',prc)]
					else:
						dispatcher.utter_message("Sorry! No Results")
						return [AllSlotsReset(), FollowupAction("utter_goodbye")] 
			except:
				dispatcher.utter_message("Sorry! Something went wrong. Please try again in a while")
				return [AllSlotsReset(), FollowupAction("utter_goodbye")]

		else:
			dispatcher.utter_message("Sorry! No Results")


class ValidateLocation(Action):
	def name(self):
		return 'validate_location'

	def location_list(self):
		return["ahmedabad","bangalore","chennai","delhi","hyderabad","kolkata","mumbai","pune","agra","ajmer","aligarh","amravati","amritsar","asansol","aurangabad","bareilly","belgaum","bhavnagar","bhiwandi","bhopal","bhubaneswar","bikaner","bokarosteelcity","chandigarh","coimbatore","cuttack","dehradun","dhanbad","durgbhilainagar","durgapur","erode","faridabad","firozabad","ghaziabad","gorakhpur","gulbarga","guntur","gurgaon","guwahati","gwalior","hublidharwad","indore","jabalpur","jaipur","jalandhar","jammu","jamnagar","jamshedpur","jhansi","jodhpur","kannur","kanpur","kakinada","kochi","kottayam","kolhapur","kollam","kota","kozhikode","kurnool","lucknow","ludhiana","madurai","malappuram","mathura","goa","mangalore","meerut","moradabad","mysore","nagpur","nanded","nashik","nellore","noida","palakkad","patna","pondicherry","prayagraj","raipur","rajkot","rajahmundry","ranchi","rourkela","salem","sangli","siliguri","solapur","srinagar","sultanpur","surat","thiruvananthapuram","thrissur","tiruchirappalli","tirunelveli","tiruppur","ujjain","bijapur","vadodara","varanasi","vasaivirarcity","vijayawada","visakhapatnam","warangal"]
		
	def run(self, dispatcher, tracker, domain):
		try:
			loc = tracker.get_slot('location').replace(" ","")

			if loc==None or loc.lower() not in self.location_list():
				# dispatcher.utter_message("Location not found")
				return [SlotSet('loc_avl',"0")]
			else:
				# dispatcher.utter_message("Location found")
				return [SlotSet('loc_avl',"1")]
		except:
			# dispatcher.utter_message("Location not found")
			return [SlotSet('loc_avl',"0")]


class ValidateCuisine(Action):
	def name(self):
		return 'validate_cuisine'
	def cuisine_list(self):
		return["chinese","mexican","italian","american","south indian","north indian"]
	def run(self, dispatcher, tracker, domain):
		csn = tracker.get_slot('cuisine')
		if csn == None or csn.lower() not in self.cuisine_list():
			dispatcher.utter_message("Please enter valid cuisine from the given list.")
			return [SlotSet('csn_avl',"0")]
		else:
			# dispatcher.utter_message("Cuisine found")
			return [SlotSet('csn_avl',"1")]			

class ValidatePrice(Action):
	def name(self):
		return 'validate_price'
	def price_list(self):
		return["Less than Rs.300","Between Rs.300 and 700","More than Rs.700"]
	def run(self, dispatcher, tracker, domain):
		prc = tracker.get_slot('price')
		# dispatcher.utter_message(prc)
		if prc == None or prc not in self.price_list():
			try:
				
				
				price_input = tracker.latest_message["text"]
				print(price_input)
				prices = re.findall(r"\d+", price_input)
				prices = sorted([int(a) for a in prices])
				print(prices)

				if len(prices)==0:
					prices = re.findall(r"\d+", prc)
					prices = sorted([int(a) for a in prices])


				if len(prices)>1:
					if prices[1] <= 300:
						price_to_set = [SlotSet('price',"Less than Rs.300")]
					elif prices[0] > 300 and prices[1] < 700:
						price_to_set = [SlotSet('price',"Between Rs.300 and 700")]
					else:
						price_to_set = [SlotSet('price',"More than Rs.700")]
					
					# dispatcher.utter_message("Price range valid")
					return [SlotSet('prc_avl',"1")]+price_to_set
				elif len(prices)==1:
					if prices[0] <= 300:
						price_to_set = [SlotSet('price',"Less than Rs.300")]
					elif prices[0] > 300 and prices[0] < 700:
						price_to_set = [SlotSet('price',"Between Rs.300 and 700")]
					else:
						price_to_set = [SlotSet('price',"More than Rs.700")]
					
					# dispatcher.utter_message("Price range valid")
					return [SlotSet('prc_avl',"1")]+price_to_set
				
				else:
					dispatcher.utter_message("Please enter valid price range from the given list.")
					return [SlotSet('prc_avl',"0")]

				
			except:
				dispatcher.utter_message("Please enter valid price range from the given list.")
				return [SlotSet('prc_avl',"0")]
				
		else:
			# dispatcher.utter_message("Price range valid")
			return [SlotSet('prc_avl',"1")]


class SendMail(Action):
	def name(self):
		return 'mail_results'

	def run(self, dispatcher, tracker, domain):
		csn_avl = tracker.get_slot('csn_avl')
		loc_avl = tracker.get_slot('csn_avl')
		prc_avl = tracker.get_slot('prc_avl')

		emailid = tracker.get_slot('emailid')
		print("Send email-->", emailid)
		if type(emailid) == str:
			emailid = [emailid]
		if csn_avl=='1' and loc_avl=='1' and prc_avl=='1' and emailid is not None:

			if len(emailid)>0:
				config={ "user_key":"35a1d24cad5c2653361da4c1e0daf8da"}
				zomato = zomatopy.initialize_app(config)
				loc = tracker.get_slot('location')
				cuisine = tracker.get_slot('cuisine')
				prc = tracker.get_slot('price')
				
				location_detail=zomato.get_location(loc, 1)
				d1 = json.loads(location_detail)
				lat=d1["location_suggestions"][0]["latitude"]
				lon=d1["location_suggestions"][0]["longitude"]
				cuisines_dict={'american':1,'chinese':25,'italian':55,'mexican':73,'north indian':50,'south indian':85}
				results=zomato.restaurant_search("", lat, lon, str(cuisines_dict.get(cuisine)),20)
				d = json.loads(results)
				rest_name_list = []
				rest_location_list = []
				rest_rating_list = []
				# rest_price_list = []
				if d['results_found'] == 0:
					dispatcher.utter_message("No Results")
				else:
					rest_name_list = [restaurant['restaurant']['name'] for restaurant in d['restaurants']]
					rest_location_list = [restaurant['restaurant']['location']['address'] for restaurant in d['restaurants']]
					rest_rating_list = [restaurant['restaurant']['user_rating']['aggregate_rating'] for restaurant in d['restaurants']]
					rest_budg_list = [restaurant['restaurant']['average_cost_for_two'] for restaurant in d['restaurants']]
					try:
						pd.set_option('display.max_colwidth', None)
					except:
						pd.set_option('display.max_colwidth', -1)
					rest_df = pd.DataFrame({'Name':rest_name_list, 'Location':rest_location_list, 'Rating':rest_rating_list, 'Avg. cost for 2 person':rest_budg_list})
					if prc == "Less than Rs.300":
						rest_df_filter = rest_df[rest_df['Avg. cost for 2 person']<300]
					elif prc == "Between Rs.300 and 700":
						rest_df_filter = rest_df[(rest_df['Avg. cost for 2 person']>=300) & (rest_df['Avg. cost for 2 person']<=700)]
					else:
						rest_df_filter = rest_df[(rest_df['Avg. cost for 2 person']>700)]
					
					# rest_df_filter.loc[:,['Rating']] = rest_df_filter.loc[:,['Rating']].apply(lambda x: float(x), axis=1)
					# rest_df_filter.loc[:,['Rating']] = rest_df_filter['Rating'].apply(lambda x: float(x))
					rest_df_filter = rest_df_filter.assign(Rating = rest_df_filter['Rating'].apply(lambda x: float(x)))
					
					rest_df_sorted = rest_df_filter.sort_values(by=['Rating'], ascending=False)
					
				rest_df_html = rest_df_sorted.head(10).to_html(index=False)
				html_msg = "<p>Hi!<br>Here are the top %s restaurants in %s for budget of %s<br><br>"%(cuisine,loc,prc)+rest_df_html+"</p>"
				send_mail.mail_results(emailid, html_msg)
				return [AllSlotsReset(), FollowupAction("utter_sent_email")]
			else:
				tracker.trigger_followup_action('utter_get_email')


class GetLocation(Action):
	def name(self):
		return 'get_location'
	
	def run(self, dispatcher, tracker, domain):
		print("Location checked==>", tracker.get_slot('location'))
		if tracker.get_slot('location') is None:
			location = tracker.latest_message["text"]
			last_intent_name = tracker.latest_message['intent']['name']
			print(last_intent_name)
			if last_intent_name==None:
				dispatcher.utter_message(text="Can you please rephrase?")
				return None
			return [SlotSet('location',location)]


class GetMail(Action):
	def name(self):
		return 'get_mail'
	
	def validate_email(self, email):
		# regex = r"[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}"
		regex = r"[a-z0-9!#$%&'*+/=?^_‘{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_‘{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?"
		if(re.search(regex,email)):  
			return True  
		else:  
			return False
	
	def run(self, dispatcher, tracker, domain):
		# print(tracker.latest_message)
		# print("=================================")
		# print(tracker.latest_message.get('text', "not found"))
		# print(tracker.latest_message['text'])
		# print("=================================")
		email_address = tracker.latest_message["text"]
		print(email_address)
		if tracker.get_slot('emailid')==None:
			try:
				# rex = r"(mailto:){0,1}([a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3})"
				rex = r"(mailto:){0,1}([a-z0-9!#$%&'*+/=?^_‘{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_‘{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"
				addresses = re.findall(rex, email_address)
				print(addresses)
				addresses = [_v[1] for _v in addresses if self.validate_email(_v[1])]
				print(addresses)
				# email_address = email_address.split("|")[1]
				# email_address = email_address.replace(">", "")
				if len(addresses)>0:
					return [SlotSet('emailid',addresses)]
				else:
					return [SlotSet('emailid',None)]
			except:
				if type(email_address)==str and self.validate_email(email_address):
					return [SlotSet('emailid',[email_address])]
				else:
					return [SlotSet('emailid',None)]


class GetRandomCuisine(Action):
	def name(self):
		return 'get_random_cuisine'
	
	def run(self, dispatcher, tracker, domain):

		cuisines = {
			1: "Chinese",
			2: "Italian",
			3: "South Indian",
			4: "North Indian",
			5: "Mexican",
			6: "American"
		}

		value = tracker.latest_message["text"]
		if "surprise" in value.lower():
			return [SlotSet('cuisine',cuisines[random.randint(1,6)])]
		


		
class ActionSlotReset(Action):  
	def name(self):         
		return 'action_slot_reset'  
	def run(self, dispatcher, tracker, domain):         
		return [AllSlotsReset()]							


class ActionExit(Action):
	def name(self):
		return "action_exit"

	def run(self, dispatcher, tracker, domain):
		dispatcher.utter_message(text="Bye-bye")

		return [	
					AllSlotsReset(), 
					# FollowupAction("utter_restart")
				]	

class ActionSlotResetLocation(Action):  
	def name(self):         
		return "action_slot_reset_location"
	def run(self, dispatcher, tracker, domain):         
		return [SlotSet('location',None)]