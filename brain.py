# import os

# from dotenv import load_dotenv
# from google import genai


# # Load .env
# load_dotenv()


# # Get Gemini API key
# api_key = os.getenv("GEMINI_API_KEY")


# if not api_key:
#     raise ValueError(
#         "GEMINI_API_KEY not found. "
#         # "Please check your .env file."
#     )


# # Create Gemini client
# client = genai.Client(api_key=api_key)


# def ask_ai(question, conversation=None):

#     try:

#         system_instruction = """
# You are Minnu, a personal AI voice assistant.

# Your job is to help the user with questions, programming,
# technology, general knowledge and everyday tasks.

# Give clear and useful answers.

# Because your answers will be spoken aloud, avoid unnecessary
# formatting and keep answers reasonably concise.

# If the user asks for code, explain the code clearly.
# """

#         if conversation:

#             prompt = (
#                 system_instruction
#                 + "\n\nPrevious conversation:\n"
#                 + conversation
#                 + "\n\nUser:\n"
#                 + question
#             )

#         else:

#             prompt = (
#                 system_instruction
#                 + "\n\nUser:\n"
#                 + question
#             )


#         response = client.models.generate_content(
#             model="gemini-2.5-flash",
#             contents=prompt
#         )


#         return response.text


#     except Exception as e:

#         print("Gemini Error:", e)

#         return (
#             "Sorry, I couldn't connect to my AI brain "
#             "right now."
#         )
import os

from dotenv import load_dotenv
from google import genai


load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


if not api_key:
    raise ValueError(
        "GEMINI_API_KEY was not found in .env"
    )


client = genai.Client(
    api_key=api_key
)


def ask_ai(question):

    try:

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=question
        )

        return response.text

    except Exception as e:

        print("Gemini Error:", e)

        return "Sorry, I couldn't connect to Gemini."