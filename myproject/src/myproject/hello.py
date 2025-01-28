from litellm import completion
import os


os.environ["GEMINI_API_KEY"] = "AIzaSyCEkrKztsaUOOzPdAejgvXwKfFzyWFwjw8"



def gemini2():
    response = completion(
        model="gemini/gemini-2.0-flash-exp",
        messages=[{ "content": "Hello, who is founder of Pakistan?", "role" : "user"}]
    )

    print(response)

