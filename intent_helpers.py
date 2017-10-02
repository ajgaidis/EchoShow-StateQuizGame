from state_data import data, get_random_state, search_for_dict_entry
from build_response import *
import random


def get_welcome_response():
    """ Welcome response for when you enter the skill """
    session_attributes = {}
    card_title = "Welcome"
    speech_output = ("Welcome to the ultimate United States quiz game." +
                     " Ask me to start a quiz!")
    should_end_session = False
    reprompt_text = ("Hello? Anyone there? Ask me to start a quiz or for" +
                     " information about a state!")
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text,
        build_display_response('https://i.imgur.com/WTHzM1y.png'),
        should_end_session))

def initialize_quiz_data(num_quiz_items):
    """ Returns a list of length num_quiz_item which contains quiz items """
    quiz_items = []
    for i in range(num_quiz_items + 1):
        state_dict = get_random_state()
        while (state_dict in quiz_items):
            state_dict = get_random_state()
        quiz_items.append(state_dict)
    return quiz_items


positive_speechCons = ["bam", "bazinga", "bingo", "boom", "booya", "bravo",
                       "cha ching", "cowabunga", "dynomite", "hurray",
                       "kaching", "mazel tov", "righto", "wahoo", "well done"]
negative_speechCons = ["argh", "blah", "blarg", "boo", "bummer", "d'oh", "eek",
                       "good grief", "jeepers creepers", "le sigh", "mamma mia",
                       "oh boy", "oh brother", "oh dear", "oy", "ruh roh",
                       "wah wah", "uh oh", "yikes", "yuck"]
def speechCon(is_response_correct):
    """ Returns a positive or negative speechCon for colorful interaction """
    if is_response_correct:
        return ("<say-as interpret-as='interjection'>" +
                random.choice(positive_speechCons) + "</say-as>")
    else:
        return ("<say-as interpret-as='interjection'>" +
                random.choice(negative_speechCons) + "</say-as>")

def start_quiz():
    """ Corresponds to the StartQuiz intent which initializes a quiz """
    total_questions = 9 # 10 questions total since zero-index
    quiz_data = initialize_quiz_data(total_questions)
    session_attributes = {"quizData": quiz_data,
                          "numQuestions": total_questions,
                          "questionsAsked": 0,
                          "numQuestionsCorrect": 0}
    card_title = "Start Quiz"
    speech_output = ("Alrighty! I will ask you the capitals of ten states. " +
        "Get seven out of ten right and I will sing for you! Here we go. What" +
        " is the capital of " + quiz_data[0]["StateName"] + "?")
    should_end_session = False
    reprompt_text = ""
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text,
        build_display_response(quiz_data[0]["image"]), should_end_session))

def answer(slots, attributes):
    """ Handles judging quiz answers and prompting for the next question """
    quiz_data = attributes["quizData"]
    total_questions = attributes["numQuestions"]
    questions_asked = attributes["questionsAsked"]
    questionsCorrect = attributes["numQuestionsCorrect"]

    if questions_asked == total_questions: # all ten questions asked
        session_attributes = {}
        speech_output = ("Wow! Not too shabby! You got %d out of %d correct." %
                         (questionsCorrect, total_questions + 1))
        card_title = "Answer"
        should_end_session = True
        reprompt_text = ""
        return build_response(session_attributes, build_speechlet_response(
            card_title, speech_output, reprompt_text,
            build_display_response('https://i.imgur.com/WTHzM1y.png'),
            should_end_session))
    else:
        if quiz_data[questions_asked]["capital"] == slots["capital"]["value"]:
            session_attributes = {"quizData": quiz_data,
                                  "numQuestions": total_questions,
                                  "questionsAsked": (questions_asked + 1),
                                  "numQuestionsCorrect": (questionsCorrect + 1)}
            speech_output = ("Correct! What is the capital of " +
                             quiz_data[questions_asked + 1]["StateName"] + "?")
            card_title = "Answer"
            should_end_session = False
            reprompt_text = ("What is the capital of " +
                            quiz_data[questions_asked + 1]["StateName"] + "?")
            return build_response(session_attributes, build_speechlet_response(
                card_title, speech_output, reprompt_text,
                build_display_response(quiz_data[questions_asked + 1]["image"]),
                should_end_session))
        else:
            session_attributes = {"quizData": quiz_data,
                                  "numQuestions": total_questions,
                                  "questionsAsked": (questions_asked + 1),
                                  "numQuestionsCorrect": questionsCorrect}
            speech_output = ("Incorrect! The capital was " +
                             quiz_data[questions_asked]["capital"] +
                             ". What is the capital of " +
                             quiz_data[questions_asked + 1]["StateName"] + "?")
            card_title = "Answer"
            should_end_session = False
            reprompt_text = ("What is the capital of " +
                            quiz_data[questions_asked + 1]["StateName"] + "?")
            return build_response(session_attributes, build_speechlet_response(
                card_title, speech_output, reprompt_text,
                build_display_response(quiz_data[questions_asked + 1]["image"]),
                should_end_session))

def stop():
    """ For the stop intent, ends the session after one last output """
    session_attributes = {}
    card_title = "Stop"
    speech_output = "I understand that you must go. Farewell, my friend."
    should_end_session = True
    reprompt_text = ""
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text,
        build_display_response('https://i.imgur.com/WTHzM1y.png'),
        should_end_session))

def cancel():
    """ For the cancel intent, ends the session after one last output """
    session_attributes = {}
    card_title = "Cancel"
    speech_output = "I will cancel the current skill. See you next time!"
    should_end_session = True
    reprompt_text = ""
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text,
        build_display_response('https://i.imgur.com/WTHzM1y.png'),
        should_end_session))

def not_implemented_error():
    """ A generic response for when an intent is not implemented """
    session_attributes = {}
    card_title = "Not Implemented"
    speech_output = "Sorry bud, all powerful Alex didn't give me that feature."
    should_end_session = False
    reprompt_text = ""
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text,
        build_display_response('https://i.imgur.com/WTHzM1y.png'),
        should_end_session))
