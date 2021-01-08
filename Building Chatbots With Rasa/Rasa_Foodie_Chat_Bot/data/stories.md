## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search
    - validate_price
    - action_search_restaurants
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "adrish.maity@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "adrish.maity@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai", "price": "More than Rs.700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - slot{"price": "More than Rs.700"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "adrish.maity@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "adrish.maity@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Lucknow"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_6
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_7
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai", "price": "More than Rs.700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - slot{"price": "More than Rs.700"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_8
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_9
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mirzapur"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mirzapur"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_10
* greet
    - utter_greet
* restaurant_search{"location": "wasseypur"}
    - slot{"location": "wasseypur"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_11
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "wasseypur"}
    - slot{"location": "wasseypur"}
    - get_location
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_12
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search
    - validate_cuisine
    - slot{"csn_avl": "0"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"cuisine": "italian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "adrish.maity@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_13
* greet
    - utter_greet
* restaurant_search{"cuisine": "moroccan", "location": "Mumbai"}
    - slot{"cuisine": "moroccan"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "0"}
    - utter_ask_cuisine
* email{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_14
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search
    - validate_cuisine
    - slot{"csn_avl": "0"}	
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "adrish.maity@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_15
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Kochi", "price": "200 to 600"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kochi"}
    - slot{"price": "200 to 600"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "0"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kochi"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "adrish.maity@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_16
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "less than 500"}
    - slot{"price": "less than 500"}
    - validate_price
    - slot{"prc_avl": "0"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_17
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "less than 500"}
    - slot{"price": "less than 500"}
    - validate_price
    - slot{"prc_avl": "0"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "adrish.maity@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_18
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "adrish.maity@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_19
* greet
    - utter_greet
* restaurant_search{"cuisine": "egyptian"}
    - slot{"cuisine": "egyptian"}
    - validate_cuisine
    - slot{"csn_avl": "0"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_20
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "adrish.maity@outlook.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_21
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_22
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet
    - utter_greet
* restaurant_search{"cuisine": "south indian", "location": "Delhi"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_23
* greet
    - utter_greet
* restaurant_search{"location": "Gurgaon"}
    - slot{"location": "Gurgaon"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Gurgaon"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_24
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_25
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Trivandram"}
    - slot{"location": "Trivandram"}
    - get_location
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_26
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Thiruvananthapuram"}
    - slot{"location": "Thiruvananthapuram"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Thiruvananthapuram"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_27
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Delhi", "price": "Less than Rs.300"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Delhi"}
    - slot{"price": "Less than Rs.300"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet
    - utter_greet
* restaurant_search{"location": "Uluberia"}
    - slot{"location": "Uluberia"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_28
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata", "price": "Between Rs.300 and 700"}
    - slot{"location": "Kolkata"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "0"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_29
* greet
    - utter_greet
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Patna"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_30
* greet
    - utter_greet
* restaurant_search{"location": "CHennai"}
    - slot{"location": "CHennai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "CHennai"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_31
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_32
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Uluberia"}
    - slot{"location": "Uluberia"}
    - get_location
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_33
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kota"}
    - slot{"location": "kota"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "kota"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_34
* email
    - get_mail
    - slot{"emailid": "a.a@a.a"}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "italian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - slot{"emailid": "adrish.maity@outlook.com"}
    - mail_results
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_35
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Lucknow"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - slot{"emailid": "adrish.maity@outlook.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_36
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_37
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - slot{"emailid": "adrish.maity@outlook.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_38
* greet
    - utter_greet
* restaurant_search{"cuisine": "Mexican", "location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - slot{"emailid": "adrish.maity@outlook.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_39
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 900"}
    - slot{"price": "more than 900"}
    - validate_price
    - slot{"prc_avl": "0"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "aniket.maity1@gmail.com"}
    - slot{"emailid": "aniket.maity1@gmail.com"}
    - get_mail
    - slot{"emailid": "adrish.maity@outlook.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_40
* greet
    - utter_greet
* restaurant_search{"location": "Guwahati"}
    - slot{"location": "Guwahati"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Guwahati"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - slot{"emailid": "adrish.maity@outlook.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_41
* greet
    - utter_greet
* restaurant_search{"location": "Meerut"}
    - slot{"location": "Meerut"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Meerut"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_42
* greet
    - utter_greet
* restaurant_search{"location": "Guwahati"}
    - slot{"location": "Guwahati"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Guwahati"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - slot{"emailid": "adrish.maity@outlook.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_43
* greet
    - utter_greet
* restaurant_search{"cuisine": "South Indian", "location": "Madurai"}
    - slot{"cuisine": "South Indian"}
    - slot{"location": "Madurai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Madurai"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_44
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - slot{"emailid": "adrish.maity@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_45
* greet
    - utter_greet
* restaurant_search{"cuisine": "American", "location": "Mumbai"}
    - slot{"cuisine": "American"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "American"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - slot{"emailid": "adrish.maity@outlook.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_46
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kona"}
    - slot{"location": "Kona"}
    - get_location
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_48
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Jabbalpur"}
    - slot{"location": "Jabbalpur"}
    - get_location
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_49
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kanpur"}
    - slot{"location": "Kanpur"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"location": "North Indian"}
    - slot{"location": "North Indian"}
    - validate_location
    - slot{"loc_avl": "0"}

## interactive_story_50
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kanpur"}
    - slot{"location": "Kanpur"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 400"}
    - slot{"price": "more than 400"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kanpur"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "more than 400"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_51
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kanpur"}
    - slot{"location": "Kanpur"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kanpur"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_52
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 900"}
    - slot{"price": "more than 900"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "more than 900"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - slot{"emailid": "adrish.maity@gmail.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_53
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese", "location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Kolkata"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - slot{"emailid": "adrish.maity@gmail.com"}
    - mail_results
    - utter_goodbye
    - action_slot_reset
    - reset_slots

## interactive_story_54
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese", "location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Kolkata"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "400"}
    - slot{"price": "400"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "400"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* restaurant_search{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - slot{"emailid": "adrish.maity@outlook.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_55
* greet
    - utter_greet
* restaurant_search{"location": "Varanasi"}
    - slot{"location": "Varanasi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Varanasi"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": "adrish.maity@gmail.com; adrish.maity@outlook.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_56
* greet
    - utter_greet
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email
    - get_mail
    - slot{"emailid": ["adrish.maity@outlook.com", "adrish.maity@gmail.com"]}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_57
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Kolkata", "price": "less than 500"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kolkata"}
    - slot{"price": "less than 500"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "less than 500"}
    - utter_ask_sendmail
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - slot{"emailid": ["adrish.maity@outlook.com"]}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_58
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata", "price": "under 600"}
    - slot{"location": "Kolkata"}
    - slot{"price": "under 600"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "0"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "0"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* email{"email": "adrish.maity@gmail.com", "emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - slot{"emailid": ["adrish.maity@gmail.com", "adrish.maity@outlook.com"]}
    - mail_results
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_59
* greet
    - utter_greet
* restaurant_search{"location": "Kolhapur", "price": "less than 500"}
    - slot{"location": "Kolhapur"}
    - slot{"price": "less than 500"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "0"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolhapur"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "less than 500"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - slot{"emailid": ["adrish.maity@outlook.com"]}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_60
* greet
    - utter_greet
* restaurant_search{"price": "less than 500"}
    - slot{"price": "less than 500"}
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - utter_ask_cuisine
* restaurant_search
    - get_random_cuisine
    - slot{"cuisine": "American"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "American"}
    - slot{"price": "less than 500"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - slot{"emailid": "adrish.maity@outlook.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_61
* restaurant_search{"price": "less than 500"}
    - slot{"price": "less than 500"}
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search
    - get_random_cuisine
    - slot{"cuisine": "American"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "American"}
    - slot{"price": "less than 500"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - slot{"emailid": "adrish.maity@outlook.com"}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_62
* greet
    - utter_greet
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_location
* affirm{"location": "Bhubaneswar"}
    - slot{"location": "Bhubaneswar"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search
    - get_random_cuisine
    - slot{"cuisine": "Mexican"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Bhubaneswar"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - slot{"emailid": ["adrish.maity@outlook.com"]}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_63
* greet
    - utter_greet
* restaurant_search{"location": "Shimla"}
    - slot{"location": "Shimla"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_64 
* greet
    - utter_greet
* restaurant_search{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - slot{"cuisine": "American"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - slot{"emailid": ["adrish.maity@gmail.com"]}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_65
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "< 600"}
    - slot{"price": "< 600"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "bangalore"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "< 600"}
    - utter_ask_sendmail
* affirm{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_66
* greet
    - utter_greet
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "< 600"}
    - slot{"price": "< 600"}
    - validate_price
    - slot{"prc_avl": "1"}
    - slot{"price": "Between Rs.300 and 700"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - slot{"emailid": ["adrish.maity@outlook.com"]}
    - mail_results
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_67
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - slot{"emailid": ["adrish.maity@gmail.com"]}
    - mail_results
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_68
* greet
    - utter_greet
* restaurant_search{"location": "Jabbalpur"}
    - slot{"location": "Jabbalpur"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_69
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - get_location
    - slot{"location": "mumba"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_70
* greet
    - utter_greet
* insult
    - utter_respond_insult
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - slot{"emailid": ["adrish.maity@outlook.com"]}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_71
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Jalandhar"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_72
* greet
    - utter_greet
* insult
    - utter_respond_insult
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Jodhpur"}
    - slot{"location": "Jodhpur"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Jodhpur"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - slot{"emailid": ["adrish.maity@gmail.com"]}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_73
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - get_location
    - slot{"location": "Howrah"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_74
* greet
    - utter_greet
* restaurant_search{"location": "Guwahati"}
    - slot{"location": "Guwahati"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Guwahati"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - slot{"emailid": ["adrish.maity@outlook.com"]}
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_75
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - get_location
    - slot{"location": "Vellor"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_76

* greet
    - utter_greet
* restaurant_search{"location":"Kolkata"}
    - slot{"location":"Kolkata"}
    - slot{"location":"Kolkata"}
    - validate_location
    - slot{"loc_avl":"1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"Mexican"}
    - slot{"cuisine":"Mexican"}
    - slot{"cuisine":"Mexican"}
    - validate_cuisine
    - slot{"csn_avl":"1"}
    - utter_ask_budget
* restaurant_search{"price":"Between Rs.300 and 700"}
    - slot{"price":"Between Rs.300 and 700"}
    - slot{"price":"Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl":"1"}
    - action_search_restaurants
    - slot{"location":"Kolkata"}
    - slot{"cuisine":"Mexican"}
    - slot{"price":"Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid":"adrish.maity@outlook.com"}
    - slot{"emailid":"adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - utter_restart

## interactive_story_77

* greet
    - utter_greet
* restaurant_search{"location":"Kolkata"}
    - slot{"location":"Kolkata"}
    - validate_location
    - slot{"loc_avl":"1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"North Indian"}
    - slot{"cuisine":"North Indian"}
    - validate_cuisine
    - slot{"csn_avl":"1"}
    - utter_ask_budget
* restaurant_search{"price":"More than Rs.700"}
    - slot{"price":"More than Rs.700"}
    - validate_price
    - slot{"prc_avl":"1"}
    - action_search_restaurants
    - slot{"location":"Kolkata"}
    - slot{"cuisine":"North Indian"}
    - slot{"price":"More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid":"adrish.maity@gmail.com"}
    - slot{"emailid":"adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - utter_restart

## interactive_story_78

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location":"Mumbai"}
    - slot{"location":"Mumbai"}
    - get_location
    - validate_location
    - slot{"loc_avl":"1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"Chinese"}
    - slot{"cuisine":"Chinese"}
    - validate_cuisine
    - slot{"csn_avl":"1"}
    - utter_ask_budget
* restaurant_search{"price":"more than 2000"}
    - slot{"price":"more than 2000"}
    - validate_price
    - slot{"prc_avl":"1"}
    - slot{"price":"More than Rs.700"}
    - action_search_restaurants
    - slot{"location":"Mumbai"}
    - slot{"cuisine":"Chinese"}
    - slot{"price":"More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - utter_restart

## interactive_story_79

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - get_location
    - slot{"location":"Darjeeling"}
    - validate_location
    - slot{"loc_avl":"0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_80

* greet
    - utter_greet
* restaurant_search{"location":"Dimapur"}
    - slot{"location":"Dimapur"}
    - validate_location
    - slot{"loc_avl":"0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_81

* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location":"Kolkata"}
    - slot{"location":"Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl":"1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"North Indian"}
    - slot{"cuisine":"North Indian"}
    - validate_cuisine
    - slot{"csn_avl":"1"}
    - utter_ask_budget
* restaurant_search{"price":"Between Rs.300 and 700"}
    - slot{"price":"Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl":"1"}
    - action_search_restaurants
    - slot{"location":"Kolkata"}
    - slot{"cuisine":"North Indian"}
    - slot{"price":"Between Rs.300 and 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - utter_restart

## interactive_story_82
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_83
* greet
    - utter_greet
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search
    - validate_cuisine
    - slot{"csn_avl": "0"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_84
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Delhi", "price": "More than Rs.700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - slot{"price": "More than Rs.700"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore", "price": "less than 700"}
    - slot{"location": "Bangalore"}
    - slot{"price": "less than 700"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - slot{"price": "More than Rs.700"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* restaurant_search{"location": "Mumbai", "price": "less than 500"}
    - slot{"location": "Mumbai"}
    - slot{"price": "less than 500"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - slot{"price": "Between Rs.300 and 700"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_85
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Ranchi"}
    - slot{"location": "Ranchi"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Ranchi"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_86
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_87
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_88
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_89
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "Chennai", "price": "above 800"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Chennai"}
    - slot{"price": "above 800"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - slot{"price": "More than Rs.700"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_90
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - reset_slots
    - followup{"name": "utter_goodbye"}
    - utter_goodbye
    - action_slot_reset
    - reset_slots

## interactive_story_91
* greet
    - utter_greet
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - reset_slots
    - followup{"name": "utter_goodbye"}
    - utter_goodbye
    - action_slot_reset
    - reset_slots

## interactive_story_92
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - get_location
    - slot{"location": "France"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_93
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_94
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_95
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "American"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_96
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbaim"}
    - slot{"location": "mumbaim"}
    - get_location
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_97
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_98
* insult
    - utter_respond_insult

## interactive_story_99
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "thai"}
    - slot{"cuisine": "thai"}
    - validate_cuisine
    - slot{"csn_avl": "0"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "more than 800"}
    - slot{"price": "more than 800"}
    - validate_price
    - slot{"prc_avl": "1"}
    - slot{"price": "More than Rs.700"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"cuisine": "American"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_100    
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_101
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_sachin_10Jul2020
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - reset_slots
    - followup{"name": "utter_goodbye"}
    - utter_goodbye
    - action_slot_reset
    - reset_slots

## interactive_story_sachin_10Jul2020
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "sachinmidesign@gmail.com"}
    - slot{"emailid": "sachinmidesign@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_sachin_10Jul2020
* greet
    - utter_greet
* restaurant_search{"location": "Rishikesh"}
    - slot{"location": "Rishikesh"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Allahabd"}
    - slot{"location": "Allahabd"}
    - get_location
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Noida"}
    - slot{"location": "Noida"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Noida"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "sachinmidesign@gmail.com"}
    - slot{"emailid": "sachinmidesign@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_sachin_10Jul2020
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "American"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "sachinmidesign@gmail.com"}
    - slot{"emailid": "sachinmidesign@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_sachin_10Jul2020
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - get_location
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "American"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "sachinmidesign@gmail.com"}
    - slot{"emailid": "sachinmidesign@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_sachin_10Jul2020
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "sachinmidesign@gmail.com"}
    - slot{"emailid": "sachinmidesign@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_4
* greet
    - utter_greet
* restaurant_search{"location": "patiala"}
    - slot{"location": "patiala"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Salem"}
    - slot{"location": "Salem"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Salem"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet
    - utter_greet
* restaurant_search{"location": "Nellore"}
    - slot{"location": "Nellore"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Nellore"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* restaurant_search{"cuisine": "Italian", "location": "baniban"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "baniban"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Uluberia"}
    - slot{"location": "Uluberia"}
    - get_location
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Hajipur"}
    - slot{"location": "Hajipur"}
    - get_location
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Bhubaneswar"}
    - slot{"location": "Bhubaneswar"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - reset_slots
    - followup{"name": "utter_goodbye"}
    - utter_goodbye
    - action_slot_reset
    - reset_slots

## interactive_story_2
* restaurant_search{"location": "uluberia"}
    - slot{"location": "uluberia"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Nona"}
    - slot{"location": "Nona"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_1
* restaurant_search{"location": "google"}
    - slot{"location": "google"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search
    - get_location
    - slot{"location": "yahoo"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search
    - get_location
    - slot{"location": "facebook"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "bellow 500"}
    - slot{"price": "bellow 500"}
    - validate_price
    - slot{"prc_avl": "1"}
    - slot{"price": "Between Rs.300 and 700"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Howrah"}
    - slot{"location": "Howrah"}
    - get_location
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search
    - get_location
    - slot{"location": "Fuleswar"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Mathura"}
    - slot{"location": "Mathura"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mathura"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet
    - utter_greet
* restaurant_search{"cuisine": "Chinese", "location": "Kollam"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "Kollam"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kollam"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* restaurant_search{"location": "Lucknow", "cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - slot{"location": "Lucknow"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Lucknow"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* restaurant_search{"location": "Bareilly"}
    - slot{"location": "Bareilly"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - action_search_restaurants
    - reset_slots
    - followup{"name": "utter_goodbye"}
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata", "cuisine": "chinese", "price": "250"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kolkata"}
    - slot{"price": "250"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - slot{"price": "Less than Rs.300"}
    - action_search_restaurants
    - reset_slots
    - followup{"name": "utter_goodbye"}
    - utter_goodbye
    - action_slot_reset
    - reset_slots
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata", "cuisine": "Mexican", "price": "600"}
    - slot{"cuisine": "Mexican"}
    - slot{"location": "Kolkata"}
    - slot{"price": "600"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - slot{"price": "Between Rs.300 and 700"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata", "cuisine": "chinese", "price": "400"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kolkata"}
    - slot{"price": "400"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - slot{"price": "Between Rs.300 and 700"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet
    - utter_greet
* restaurant_search{"location": "howrah", "cuisine": "Chinese", "price": "500"}
    - slot{"cuisine": "Chinese"}
    - slot{"location": "howrah"}
    - slot{"price": "500"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - slot{"price": "Between Rs.300 and 700"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"cuisine": "Chinese"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* email{"emailid": "aniket.maity1@gmail.com"}
    - slot{"emailid": "aniket.maity1@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search
    - get_location
    - slot{"location": "bagnan"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "kanpur"}
    - slot{"location": "kanpur"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - reset_slots
    - followup{"name": "utter_goodbye"}
    - utter_goodbye
    - action_slot_reset
    - reset_slots
* greet
    - utter_greet
* restaurant_search{"location": "Kolhapur"}
    - slot{"location": "Kolhapur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolhapur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "aniket.maity1@gmail.com"}
    - slot{"emailid": "aniket.maity1@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_1
* restaurant_search{"cuisine": "chinese", "price": "500", "location": "Kolkata"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Kolkata"}
    - slot{"price": "500"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - slot{"price": "Between Rs.300 and 700"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "chinese"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "price": "Less than Rs.300", "location": "Delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "Delhi"}
    - slot{"price": "Less than Rs.300"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - reset_slots
    - followup{"name": "utter_goodbye"}
    - utter_goodbye
    - action_slot_reset
    - reset_slots
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "pune"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "American"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet
    - utter_greet
* restaurant_search{"location": "Allahabd"}
    - slot{"location": "Allahabd"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Amritsar"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet
    - utter_greet
* restaurant_search{"location": "Indore"}
    - slot{"location": "Indore"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Indore"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Jamshedpur"}
    - slot{"location": "Jamshedpur"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Jamshedpur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "aniket.maity1@gmail.com"}
    - slot{"emailid": "aniket.maity1@gmail.com"}
    - get_mail
    - mail_results
    - reset_slots
    - followup{"name": "utter_sent_email"}
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## Story from conversation with 83a2afa48cd34f998ec08d5b0b7f8c9f on July 13th 2020

* greet
    - utter_greet
* restaurant_search{"location":"Kolkata"}
    - slot{"location":"Kolkata"}
    - slot{"location":"Kolkata"}
    - validate_location
    - slot{"loc_avl":"1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - slot{"cuisine":"South Indian"}
    - validate_cuisine
    - slot{"csn_avl":"1"}
    - utter_ask_budget
* restaurant_search{"price":"More than Rs.700"}
    - slot{"price":"More than Rs.700"}
    - slot{"price":"More than Rs.700"}
    - validate_price
    - slot{"prc_avl":"1"}
    - action_search_restaurants
    - slot{"location":"Kolkata"}
    - slot{"cuisine":"South Indian"}
    - slot{"price":"More than Rs.700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - utter_restart
* restaurant_search{"location":"Jamshedpur"}
    - slot{"location":"Jamshedpur"}
    - slot{"location":"Jamshedpur"}
    - validate_location
    - slot{"loc_avl":"1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine":"Chinese"}
    - slot{"cuisine":"Chinese"}
    - slot{"cuisine":"Chinese"}
    - validate_cuisine
    - slot{"csn_avl":"1"}
    - utter_ask_budget
* restaurant_search{"price":"Between Rs.300 and 700"}
    - slot{"price":"Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl":"1"}
    - action_search_restaurants
    - slot{"location":"Jamshedpur"}
    - slot{"cuisine":"Chinese"}
    - slot{"price":"Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid":"adrish.maity@outlook.com"}
    - slot{"emailid":"adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - utter_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* greet
    - utter_greet
* restaurant_search{"location": "Vasai-Virar City"}
    - slot{"location": "Vasai-Virar City"}
    - validate_location
    - slot{"loc_avl": "0"}
    - utter_do_not_operate
    - action_slot_reset_location
    - slot{"location": null}
* restaurant_search{"location": "Ujjain"}
    - slot{"location": "Ujjain"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Ujjain"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
* restaurant_search{"location": "Tiruppur"}
    - slot{"location": "Tiruppur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Italian"}
    - slot{"cuisine": "Italian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "More than Rs.700"}
    - slot{"price": "More than Rs.700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - reset_slots
    - followup{"name": "utter_goodbye"}
    - utter_goodbye
    - action_slot_reset
    - reset_slots
* greet
    - utter_greet
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Nashik"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "More than Rs.700"}
    - utter_ask_sendmail
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - reset_slots
    - followup{"name": "utter_sent_email"}
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_0
* greet
    - utter_greet
* restaurant_search{"location": "Kolhapur"}
    - slot{"location": "Kolhapur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolhapur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_Ahmedabad_100
* greet
    - utter_greet
* restaurant_search{"location": "Ahmedabad"}
    - slot{"location": "Ahmedabad"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Ahmedabad"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Bangalore_101
* greet
    - utter_greet
* restaurant_search{"location": "Bangalore"}
    - slot{"location": "Bangalore"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Bangalore"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Chennai_102
* greet
    - utter_greet
* restaurant_search{"location": "Chennai"}
    - slot{"location": "Chennai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Chennai"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Delhi_103
* greet
    - utter_greet
* restaurant_search{"location": "Delhi"}
    - slot{"location": "Delhi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Delhi"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Hyderabad_104
* greet
    - utter_greet
* restaurant_search{"location": "Hyderabad"}
    - slot{"location": "Hyderabad"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Hyderabad"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Kolkata_105
* greet
    - utter_greet
* restaurant_search{"location": "Kolkata"}
    - slot{"location": "Kolkata"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolkata"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Mumbai_106
* greet
    - utter_greet
* restaurant_search{"location": "Mumbai"}
    - slot{"location": "Mumbai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mumbai"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Pune_107
* greet
    - utter_greet
* restaurant_search{"location": "Pune"}
    - slot{"location": "Pune"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Pune"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Agra_108
* greet
    - utter_greet
* restaurant_search{"location": "Agra"}
    - slot{"location": "Agra"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Agra"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Ajmer_109
* greet
    - utter_greet
* restaurant_search{"location": "Ajmer"}
    - slot{"location": "Ajmer"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Ajmer"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Aligarh_110
* greet
    - utter_greet
* restaurant_search{"location": "Aligarh"}
    - slot{"location": "Aligarh"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Aligarh"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Amravati_111
* greet
    - utter_greet
* restaurant_search{"location": "Amravati"}
    - slot{"location": "Amravati"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Amravati"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Amritsar_112
* greet
    - utter_greet
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Amritsar"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 

## interactive_story_Amritsar_100
* greet
    - utter_greet
* restaurant_search{"location": "Amritsar"}
    - slot{"location": "Amritsar"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Amritsar"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Asansol_101
* greet
    - utter_greet
* restaurant_search{"location": "Asansol"}
    - slot{"location": "Asansol"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Asansol"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Aurangabad_102
* greet
    - utter_greet
* restaurant_search{"location": "Aurangabad"}
    - slot{"location": "Aurangabad"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Aurangabad"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Bareilly_103
* greet
    - utter_greet
* restaurant_search{"location": "Bareilly"}
    - slot{"location": "Bareilly"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Bareilly"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Belgaum_104
* greet
    - utter_greet
* restaurant_search{"location": "Belgaum"}
    - slot{"location": "Belgaum"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Belgaum"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Bhavnagar_105
* greet
    - utter_greet
* restaurant_search{"location": "Bhavnagar"}
    - slot{"location": "Bhavnagar"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Bhavnagar"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Bhiwandi_106
* greet
    - utter_greet
* restaurant_search{"location": "Bhiwandi"}
    - slot{"location": "Bhiwandi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Bhiwandi"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Bhopal_107
* greet
    - utter_greet
* restaurant_search{"location": "Bhopal"}
    - slot{"location": "Bhopal"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Bhopal"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Bhubaneswar_108
* greet
    - utter_greet
* restaurant_search{"location": "Bhubaneswar"}
    - slot{"location": "Bhubaneswar"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Bhubaneswar"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Bikaner_109
* greet
    - utter_greet
* restaurant_search{"location": "Bikaner"}
    - slot{"location": "Bikaner"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Bikaner"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Bokaro Steel City_110
* greet
    - utter_greet
* restaurant_search{"location": "Bokaro Steel City"}
    - slot{"location": "Bokaro Steel City"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Bokaro Steel City"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Chandigarh_111
* greet
    - utter_greet
* restaurant_search{"location": "Chandigarh"}
    - slot{"location": "Chandigarh"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Chandigarh"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Coimbatore_112
* greet
    - utter_greet
* restaurant_search{"location": "Coimbatore"}
    - slot{"location": "Coimbatore"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Coimbatore"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Cuttack_113
* greet
    - utter_greet
* restaurant_search{"location": "Cuttack"}
    - slot{"location": "Cuttack"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Cuttack"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Dehradun_114
* greet
    - utter_greet
* restaurant_search{"location": "Dehradun"}
    - slot{"location": "Dehradun"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Dehradun"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Dhanbad_115
* greet
    - utter_greet
* restaurant_search{"location": "Dhanbad"}
    - slot{"location": "Dhanbad"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Dhanbad"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Durg Bhilai Nagar_116
* greet
    - utter_greet
* restaurant_search{"location": "Durg Bhilai Nagar"}
    - slot{"location": "Durg Bhilai Nagar"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Durg Bhilai Nagar"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Durgapur_117
* greet
    - utter_greet
* restaurant_search{"location": "Durgapur"}
    - slot{"location": "Durgapur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Durgapur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Erode_118
* greet
    - utter_greet
* restaurant_search{"location": "Erode"}
    - slot{"location": "Erode"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Erode"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Faridabad_119
* greet
    - utter_greet
* restaurant_search{"location": "Faridabad"}
    - slot{"location": "Faridabad"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Faridabad"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Firozabad_120
* greet
    - utter_greet
* restaurant_search{"location": "Firozabad"}
    - slot{"location": "Firozabad"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Firozabad"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Ghaziabad_121
* greet
    - utter_greet
* restaurant_search{"location": "Ghaziabad"}
    - slot{"location": "Ghaziabad"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Ghaziabad"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Gorakhpur_122
* greet
    - utter_greet
* restaurant_search{"location": "Gorakhpur"}
    - slot{"location": "Gorakhpur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Gorakhpur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Gulbarga_123
* greet
    - utter_greet
* restaurant_search{"location": "Gulbarga"}
    - slot{"location": "Gulbarga"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Gulbarga"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Guntur_124
* greet
    - utter_greet
* restaurant_search{"location": "Guntur"}
    - slot{"location": "Guntur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Guntur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Gurgaon_125
* greet
    - utter_greet
* restaurant_search{"location": "Gurgaon"}
    - slot{"location": "Gurgaon"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Gurgaon"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Guwahati_126
* greet
    - utter_greet
* restaurant_search{"location": "Guwahati"}
    - slot{"location": "Guwahati"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Guwahati"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Gwalior_127
* greet
    - utter_greet
* restaurant_search{"location": "Gwalior"}
    - slot{"location": "Gwalior"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Gwalior"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Hubli Dharwad_128
* greet
    - utter_greet
* restaurant_search{"location": "Hubli Dharwad"}
    - slot{"location": "Hubli Dharwad"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Hubli Dharwad"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Indore_129
* greet
    - utter_greet
* restaurant_search{"location": "Indore"}
    - slot{"location": "Indore"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Indore"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Jabalpur_130
* greet
    - utter_greet
* restaurant_search{"location": "Jabalpur"}
    - slot{"location": "Jabalpur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Jabalpur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Jaipur_131
* greet
    - utter_greet
* restaurant_search{"location": "Jaipur"}
    - slot{"location": "Jaipur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Jaipur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Jalandhar_132
* greet
    - utter_greet
* restaurant_search{"location": "Jalandhar"}
    - slot{"location": "Jalandhar"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Jalandhar"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Jammu_133
* greet
    - utter_greet
* restaurant_search{"location": "Jammu"}
    - slot{"location": "Jammu"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Jammu"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Jamnagar_134
* greet
    - utter_greet
* restaurant_search{"location": "Jamnagar"}
    - slot{"location": "Jamnagar"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Jamnagar"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Jamshedpur_135
* greet
    - utter_greet
* restaurant_search{"location": "Jamshedpur"}
    - slot{"location": "Jamshedpur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Jamshedpur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Jhansi_136
* greet
    - utter_greet
* restaurant_search{"location": "Jhansi"}
    - slot{"location": "Jhansi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Jhansi"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Jodhpur_137
* greet
    - utter_greet
* restaurant_search{"location": "Jodhpur"}
    - slot{"location": "Jodhpur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Jodhpur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Kannur_138
* greet
    - utter_greet
* restaurant_search{"location": "Kannur"}
    - slot{"location": "Kannur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kannur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Kanpur_139
* greet
    - utter_greet
* restaurant_search{"location": "Kanpur"}
    - slot{"location": "Kanpur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kanpur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Kakinada_140
* greet
    - utter_greet
* restaurant_search{"location": "Kakinada"}
    - slot{"location": "Kakinada"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kakinada"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Kochi_141
* greet
    - utter_greet
* restaurant_search{"location": "Kochi"}
    - slot{"location": "Kochi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kochi"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Kottayam_142
* greet
    - utter_greet
* restaurant_search{"location": "Kottayam"}
    - slot{"location": "Kottayam"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kottayam"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Kolhapur_143
* greet
    - utter_greet
* restaurant_search{"location": "Kolhapur"}
    - slot{"location": "Kolhapur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kolhapur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Kollam_144
* greet
    - utter_greet
* restaurant_search{"location": "Kollam"}
    - slot{"location": "Kollam"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kollam"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Kota_145
* greet
    - utter_greet
* restaurant_search{"location": "Kota"}
    - slot{"location": "Kota"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kota"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Kozhikode_146
* greet
    - utter_greet
* restaurant_search{"location": "Kozhikode"}
    - slot{"location": "Kozhikode"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kozhikode"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Kurnool_147
* greet
    - utter_greet
* restaurant_search{"location": "Kurnool"}
    - slot{"location": "Kurnool"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Kurnool"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Lucknow_148
* greet
    - utter_greet
* restaurant_search{"location": "Lucknow"}
    - slot{"location": "Lucknow"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Lucknow"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Ludhiana_149
* greet
    - utter_greet
* restaurant_search{"location": "Ludhiana"}
    - slot{"location": "Ludhiana"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Ludhiana"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Madurai_150
* greet
    - utter_greet
* restaurant_search{"location": "Madurai"}
    - slot{"location": "Madurai"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Madurai"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Malappuram_151
* greet
    - utter_greet
* restaurant_search{"location": "Malappuram"}
    - slot{"location": "Malappuram"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Malappuram"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Mathura_152
* greet
    - utter_greet
* restaurant_search{"location": "Mathura"}
    - slot{"location": "Mathura"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mathura"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Goa_153
* greet
    - utter_greet
* restaurant_search{"location": "Goa"}
    - slot{"location": "Goa"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Goa"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Mangalore_154
* greet
    - utter_greet
* restaurant_search{"location": "Mangalore"}
    - slot{"location": "Mangalore"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mangalore"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Meerut_155
* greet
    - utter_greet
* restaurant_search{"location": "Meerut"}
    - slot{"location": "Meerut"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Meerut"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Moradabad_156
* greet
    - utter_greet
* restaurant_search{"location": "Moradabad"}
    - slot{"location": "Moradabad"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Moradabad"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Mysore_157
* greet
    - utter_greet
* restaurant_search{"location": "Mysore"}
    - slot{"location": "Mysore"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Nagpur_158
* greet
    - utter_greet
* restaurant_search{"location": "Nagpur"}
    - slot{"location": "Nagpur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Nagpur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Nanded_159
* greet
    - utter_greet
* restaurant_search{"location": "Nanded"}
    - slot{"location": "Nanded"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Nanded"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Nashik_160
* greet
    - utter_greet
* restaurant_search{"location": "Nashik"}
    - slot{"location": "Nashik"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Nashik"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Nellore_161
* greet
    - utter_greet
* restaurant_search{"location": "Nellore"}
    - slot{"location": "Nellore"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Nellore"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Noida_162
* greet
    - utter_greet
* restaurant_search{"location": "Noida"}
    - slot{"location": "Noida"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Noida"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Palakkad_163
* greet
    - utter_greet
* restaurant_search{"location": "Palakkad"}
    - slot{"location": "Palakkad"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Palakkad"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Patna_164
* greet
    - utter_greet
* restaurant_search{"location": "Patna"}
    - slot{"location": "Patna"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Patna"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Pondicherry_165
* greet
    - utter_greet
* restaurant_search{"location": "Pondicherry"}
    - slot{"location": "Pondicherry"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Pondicherry"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Prayagraj_166
* greet
    - utter_greet
* restaurant_search{"location": "Prayagraj"}
    - slot{"location": "Prayagraj"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Prayagraj"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Raipur_167
* greet
    - utter_greet
* restaurant_search{"location": "Raipur"}
    - slot{"location": "Raipur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Raipur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Rajkot_168
* greet
    - utter_greet
* restaurant_search{"location": "Rajkot"}
    - slot{"location": "Rajkot"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Rajkot"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Rajahmundry_169
* greet
    - utter_greet
* restaurant_search{"location": "Rajahmundry"}
    - slot{"location": "Rajahmundry"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Rajahmundry"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Ranchi_170
* greet
    - utter_greet
* restaurant_search{"location": "Ranchi"}
    - slot{"location": "Ranchi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Ranchi"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Rourkela_171
* greet
    - utter_greet
* restaurant_search{"location": "Rourkela"}
    - slot{"location": "Rourkela"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Rourkela"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@gmail.com"}
    - slot{"emailid": "adrish.maity@gmail.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Salem_172
* greet
    - utter_greet
* restaurant_search{"location": "Salem"}
    - slot{"location": "Salem"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Salem"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Sangli_173
* greet
    - utter_greet
* restaurant_search{"location": "Sangli"}
    - slot{"location": "Sangli"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Sangli"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Siliguri_174
* greet
    - utter_greet
* restaurant_search{"location": "Siliguri"}
    - slot{"location": "Siliguri"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Siliguri"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Solapur_175
* greet
    - utter_greet
* restaurant_search{"location": "Solapur"}
    - slot{"location": "Solapur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Solapur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Srinagar_176
* greet
    - utter_greet
* restaurant_search{"location": "Srinagar"}
    - slot{"location": "Srinagar"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Srinagar"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Sultanpur_177
* greet
    - utter_greet
* restaurant_search{"location": "Sultanpur"}
    - slot{"location": "Sultanpur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Sultanpur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Surat_178
* greet
    - utter_greet
* restaurant_search{"location": "Surat"}
    - slot{"location": "Surat"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Surat"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Thiruvananthapuram_179
* greet
    - utter_greet
* restaurant_search{"location": "Thiruvananthapuram"}
    - slot{"location": "Thiruvananthapuram"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Thiruvananthapuram"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 

## interactive_story_Thiruvananthapuram_100
* greet
    - utter_greet
* restaurant_search{"location": "Thiruvananthapuram"}
    - slot{"location": "Thiruvananthapuram"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Thiruvananthapuram"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Thrissur_101
* greet
    - utter_greet
* restaurant_search{"location": "Thrissur"}
    - slot{"location": "Thrissur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Thrissur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Tiruchirappalli_102
* greet
    - utter_greet
* restaurant_search{"location": "Tiruchirappalli"}
    - slot{"location": "Tiruchirappalli"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Tiruchirappalli"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Tirunelveli_103
* greet
    - utter_greet
* restaurant_search{"location": "Tirunelveli"}
    - slot{"location": "Tirunelveli"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Tirunelveli"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Tiruppur_104
* greet
    - utter_greet
* restaurant_search{"location": "Tiruppur"}
    - slot{"location": "Tiruppur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Tiruppur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Ujjain_105
* greet
    - utter_greet
* restaurant_search{"location": "Ujjain"}
    - slot{"location": "Ujjain"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Ujjain"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Bijapur_106
* greet
    - utter_greet
* restaurant_search{"location": "Bijapur"}
    - slot{"location": "Bijapur"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Bijapur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Vadodara_107
* greet
    - utter_greet
* restaurant_search{"location": "Vadodara"}
    - slot{"location": "Vadodara"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Vadodara"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Varanasi_108
* greet
    - utter_greet
* restaurant_search{"location": "Varanasi"}
    - slot{"location": "Varanasi"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Varanasi"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Vasai Virar City_109
* greet
    - utter_greet
* restaurant_search{"location": "Vasai Virar City"}
    - slot{"location": "Vasai Virar City"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Vasai Virar City"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Vijayawada_110
* greet
    - utter_greet
* restaurant_search{"location": "Vijayawada"}
    - slot{"location": "Vijayawada"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Vijayawada"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Visakhapatnam_111
* greet
    - utter_greet
* restaurant_search{"location": "Visakhapatnam"}
    - slot{"location": "Visakhapatnam"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Visakhapatnam"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_Warangal_112
* greet
    - utter_greet
* restaurant_search{"location": "Warangal"}
    - slot{"location": "Warangal"}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Warangal"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story__113
* greet
    - utter_greet
* restaurant_search{"location": ""}
    - slot{"location": ""}
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - utter_ask_budget
* restaurant_search{"price": "Between Rs.300 and 700"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": ""}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* affirm
    - utter_get_email
* email{"emailid": "adrish.maity@outlook.com"}
    - slot{"emailid": "adrish.maity@outlook.com"}
    - get_mail
    - mail_results
    - utter_sent_email
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart
 
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "less than 500"}
    - slot{"price": "less than 500"}
    - utter_ask_location
* restaurant_search{"location": "Kannur"}
    - slot{"location": "Kannur"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - slot{"price": "Between Rs.300 and 700"}
    - action_search_restaurants
    - slot{"location": "Kannur"}
    - slot{"cuisine": "North Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_1    
* greet
    - utter_greet
* restaurant_search{"price": "Between Rs.300 and 700", "cuisine": "Italian", "location": "Mysore"}
    - slot{"cuisine": "Italian"}
    - slot{"location": "Mysore"}
    - slot{"price": "Between Rs.300 and 700"}
    - validate_location
    - slot{"loc_avl": "1"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Mysore"}
    - slot{"cuisine": "Italian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "Less than Rs.300"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_location
* restaurant_search{"location": "Warangal"}
    - slot{"location": "Warangal"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - action_search_restaurants
    - slot{"location": "Warangal"}
    - slot{"cuisine": "Mexican"}
    - slot{"price": "Less than Rs.300"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price": "under 600"}
    - slot{"price": "under 600"}
    - utter_ask_location
* restaurant_search{"location": "Bijapur"}
    - slot{"location": "Bijapur"}
    - get_location
    - validate_location
    - slot{"loc_avl": "1"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - validate_cuisine
    - slot{"csn_avl": "1"}
    - validate_price
    - slot{"prc_avl": "1"}
    - slot{"price": "Between Rs.300 and 700"}
    - action_search_restaurants
    - slot{"location": "Bijapur"}
    - slot{"cuisine": "South Indian"}
    - slot{"price": "Between Rs.300 and 700"}
    - utter_ask_sendmail
* deny
    - utter_goodbye
    - action_slot_reset
    - reset_slots
    - utter_restart

## interactive_story_1
* greet
    - utter_greet
* goodbye
    - utter_goodbye
