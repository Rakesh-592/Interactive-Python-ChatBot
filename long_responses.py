import random

R_EATING = "I don't like eating anything because I am a bot obviously!"
def unknown():
    response = ["Could you please re-phrase that?",
                "....",
                "Sounds about right",
                "what does that mean?"][random.randrange(4)]
                #as there are 4 responses
    
    return response 