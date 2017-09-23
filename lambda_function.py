from __future__ import print_function
from intent_helpers import *


def lambda_handler(event, context):
    print("Python START -------------------------------")
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])

def on_session_started(session_started_request, session):
    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])

def on_launch(launch_request, session):
    """ Called when user launches skill without specifying what they want """
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return get_welcome_response()

def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """
    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    attributes = {}
    if 'attributes' in session:
        attributes = session["attributes"]
    intent_slots = {}
    if 'slots' in intent_request['intent']:
        intent_slots = intent_request['intent']['slots']

    if intent_name == "QuizIntent":
        return start_quiz()

    if intent_name == "AnswerIntent":
        return answer(intent_slots, attributes)

    if intent_name == "AMAZON.RepeatIntent":
        raise NotImplementedError("Implement me!")

    if intent_name == "AMAZON.HelpIntent":
        raise NotImplementedError("Implement me!")

    if intent_name == "AMAZON.CancelIntent":
        return cancel()

    if intent_name == "AMAZON.StopIntent":
        return stop()

    else: # Unhandled
        return not_implemented_error()


def on_session_ended(session_ended_request, session):
    """ Called when user ends the session; not when should_end_session=true """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
