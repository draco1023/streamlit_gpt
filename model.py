import openai

poem = """Write a poem with the following words: 
---
{input}
---
This is the poem: """


def set_openai_key(key):
    """Sets OpenAI key."""
    openai.api_key = key


class GeneralModel:
    def __init__(self):
        print("Model Intilization--->")

    def query(self, prompt, myKwargs={}):
        """
        wrapper for the API to save the prompt and the result
        """

        # arguments to send the API
        kwargs = {
            "temperature": 0.9,
            "max_tokens": 600,
        }

        for kwarg in myKwargs:
            kwargs[kwarg] = myKwargs[kwarg]

        r = openai.ChatCompletion.create(model="gpt-4", messages=[{"role": "system", "content": prompt}], **kwargs)
        return r["choices"][0]["message"]["content"].strip()

    def model_prediction(self, inp, api_key):
        """
        wrapper for the API to save the prompt and the result
        """
        # Setting the OpenAI API key got from the OpenAI dashboard
        set_openai_key(api_key)
        output = self.query(poem.format(input=inp))
        return output
