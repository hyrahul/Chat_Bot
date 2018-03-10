EchoBot I
Hello, World!
Write a function called respond() with a single parameter message which returns the bot's response. To do this, concatenate the strings "I can hear you! You said: " and message.
Store the concatenated strings in bot_message, and return this result.


bot_template = "BOT : {0}"bot_template = "BOT : {0}"
user_template = "USER : {0}"

# Define a function that responds to a user's message: respond
def respond(message):
    # Concatenate the user's message to the end of a standard bot respone
    bot_message = "I can hear you! You said: " + message
    # Return the result
    return bot_message


EchoBot II
Having written your respond() function, you'll now define a function called send_message() with a single parameter message which logs the message and the bot's response.

# Define a function that sends a message to the bot: send_message
def send_message(message):
    # Print user_template including the user_message
    print(user_template.format(message))
    # Get the bot's response to the message
    response = respond(message)
    # Print the bot template including the bot's response.
    print(bot_template.format(response))

# Send a message to the bot
send_message("hello")


Chitchat
Now you're going to leave simple EchoBot behind and create a bot which can answer simple questions such as "What's your name?" and "What's today's weather?"

You'll use a dictionary with these questions as keys, and the correct responses as values.

This means the bot will only respond correctly if the message matches exactly, which is a big limitation. In later exercises you will create much more robust solutions.

The send_message function has already been defined for you, as well as the bot_template and user_template variables.

# Define variables
name = "Greg"
weather = "cloudy"

# Define a dictionary with the predefined responses
responses = {
  "what's your name?": "my name is {0}".format(name),
  "what's today's weather?": "the weather is {0}".format(weather),
  "default": "default message"
}

# Return the matching response if there is one, default otherwise
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return the matching message
        bot_message = responses[message]
    else:
        # Return the "default" message
        bot_message = responses["default"]
    return bot_message
	
	
	
Adding variety
It can get a little boring hearing the same old answers over and over. In this exercise, you'll add some variation. If you ask your bot how it's feeling, it may equally well respond with "oh I'm great!" as with "I'm very sad today".

Here, you'll use the random module - specifically random.choice(ls) - which randomly selects an element from a list ls.

A dictionary called responses, which maps each message to a list of possible responses, has been defined for you.

# Import the random module
import random

name = "Greg"
weather = "cloudy"

# Define a dictionary containing a list of responses for each message
responses = {
  "what's your name?": [
      "my name is {0}".format(name),
      "they call me {0}".format(name),
      "I go by {0}".format(name)
   ],
  "what's today's weather?": [
      "the weather is {0}".format(weather),
      "it's {0} today".format(weather)
    ],
  "default": ["default message"]
}

# Use random.choice() to choose a matching response
def respond(message):
    # Check if the message is in the responses
    if message in responses:
        # Return a random matching response
        bot_message = random.choice(responses[message])
    else:
        # Return a random "default" response
        bot_message = random.choice(responses["default"])
    return bot_message
	
	
	
	
ELIZA I: asking questions
Asking questions is a great way to create an engaging conversation. Here, you'll create the very first hint of ELIZA's famous personality, by responding to statements with a question and responding to questions with answers.

A dictionary of responses with "question" and "statement" as keys, and lists of appropriate responses as values has already been defined for you. Explore this in the Shell with responses.keys() and responses["question"].

import random

def respond(message):
    # Check for a question mark
    if message.endswith("?"):
        # Return a random question
        return random.choice(responses["question"])
    # Return a random statement
    return random.choice(responses["statement"])


# Send messages ending in a question mark
send_message("what's today's weather?")
send_message("what's today's weather?")

# Send messages which don't end with a question mark
send_message("I love building chatbots")
send_message("I love building chatbots")





ELIZA II: Extracting key phrases
The really clever thing about ELIZA is the way the program appears to understand what you told it, by occasionally including phrases uttered by the user in its responses.

In this exercise, you will match messages against some common patterns and extract phrases using re.search(). A dictionary called rules has already been defined, which matches the following patterns:

"do you think (.*)"
"do you remember (.*)"
"I want (.*)"
"if (.*)"
Inspect this dictionary in the Shell before starting the exercise.



# Define match_rule()
def match_rule(rules, message):
    response, phrase = "default", None
    
    # Iterate over the rules dictionary
    for pattern, responses in rules.items():
        # Create a match object
        match = re.search(pattern, message)
        if match is not None:
            # Choose a random response
            response = random.choice(responses)
            if '{0}' in response:
                phrase = match.group(1)
    # Return the response and phrase
    return response, phrase

# Test match_rule
print(match_rule(rules, "do you remember your last birthday"))


ELIZA III: Pronouns
To make responses grammatically coherent, you'll want to transform the extracted phrases from first to second person and vice versa. In English, conjugating verbs is easy, and simply swapping "I" and 'you', "my" and "your" works in most cases.

In this exercise, you'll define a function called replace_pronouns() which uses re.sub() to map "me" and "my" to "you" and "your" (and vice versa) in a string.


# Define replace_pronouns()
def replace_pronouns(message):

    message = message.lower()
    if 'me' in message:
        # Replace 'me' with 'you'
        return re.sub('me','you',message)
    if 'my' in message:
        # Replace 'my' with 'your'
        return re.sub('my','your',message)
    if 'your' in message:
        # Replace 'your' with 'my'
        return re.sub('your','my',message)
    if 'you' in message:
        # Replace 'you' with 'me'
        return re.sub('you','me',message)

    return message

print(replace_pronouns("my last birthday"))
print(replace_pronouns("when you went to Florida"))
print(replace_pronouns("I had my own castle"))


ELIZA IV: Putting it all together
Now you're going to put it all together and experience the magic! The match_rule(), send_message(), and replace_pronouns() functions have already been defined, and the rules dictionary is available in your workspace.

Your job here is to write a function called respond() with a single argument message which creates an appropriate response to be handled by send_message.


# Define respond()
def respond(message):
    # Call match_rule
    response, phrase = match_rule(rules,message)
    if '{0}' in response:
        # Replace the pronouns in the phrase
        phrase = replace_pronouns(phrase)
        # Include the phrase in the response
        response = response.format(phrase)
    return response

# Send the messages
send_message("do you remember your last birthday")
send_message("do you think humans should be worried about AI")
send_message("I want a robot friend")
send_message("what if you could be anything you wanted")



