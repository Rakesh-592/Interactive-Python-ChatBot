import re #for regex 
import long_responses as long 

def message_probability(user_message,recognised_words,single_response = False,required_words=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognised_words:
            message_certainty += 1 
    #calculating % of recognised in user msg
    percentage = float(message_certainty) / float(len(recognised_words))

    #checks if the required words in string or not
    for word in required_words:
        if word not in user_message:
            has_required_words = False
            break 
    #must have req words or be a single response
    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0 #if nothing really match

def check_all_messages(message):
    highest_prob_list = {}

    #simplifies response creation/ adds it to the dict
    def response(bot_response,list_of_words,single_response = False,required_words=[]):
        nonlocal highest_prob_list 
        highest_prob_list[bot_response] = message_probability(message,list_of_words,single_response,required_words)

    #Responses ------------------------
    #list contains lower case as it's case sensitive
    response("Hello!",["hello", "hola!",  "hi", "hey", "wassup!"],single_response=True)
    response("I\'m doing fine, and you?",["how","are","you","doing"],required_words=["how"])
    response("Thank you!:",["i","love","coding"],required_words=["code","love"])

    #longer responses
    response(long.R_EATING,["what","you","eat"],required_words=["you","eat"])
    
    best_match = max(highest_prob_list,key=highest_prob_list.get)
    #print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match

def get_response(user_input):
    #this helps to remove all the symbols from msgs
    #and allows us just to have clean words just to
    #recognize
    split_message = re.split(r'\s+|[,;?!.-]\s*',user_input.lower())
    response = check_all_messages(split_message)
    return response 
    #using lower as it is case sensitive
#an infinite while loop to always get
#new responses

#testing the response system
while True:
    print("Bot: "+get_response(input("You: "))) 