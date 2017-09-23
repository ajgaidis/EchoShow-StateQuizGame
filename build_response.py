
def build_display_response(url=''):
    """
    Builds the display template for the echo show to display. Restricts user to
    only see a single background image using BodyTemplate6.

    Echo show screen is 1024px x 600px
    For additional image size requirements, see the display interface reference
    """
    return [{
        'type': 'Display.RenderTemplate',
        'template': {
            'type': 'BodyTemplate6',
            'backgroundImage': {
                'contentDescription': '',
                'sources': [
                    {
                        'url': url
                        # 'size':
                        # 'widthPixels':
                        # 'heightPixels':
                    }
                ]
            }
        }
    }]

def build_speechlet_response(title, output, reprompt_text, display_response,
                             should_end_session):
    """ Builds speechlet response and puts display response inside """
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': title,
            'content': output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'directives': display_response,
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    """ Builds the complete response to send back to Alexa """
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
