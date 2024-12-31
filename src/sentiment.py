from logger import logging
from exception import CustomException
from groq import Groq
from dotenv import load_dotenv
import os
import sys
load_dotenv()
api_key=os.getenv("GROQ_API_KEY")

class SentimentAnalysis:
    def __init__(self):
        
        self.client=Groq(api_key=api_key)
        
    def analyse_sentiment(self,user_feedback):
        try:
            prompt=f"""you have to analyze the user feedback{user_feedback} and should perform sentiment analysis
            you have to reply with these 3 sentiments Positive or Negative or Neutral.You'r answer strictly should be in one word.
            Example:
            User feedback : With the car that i bought from you for rent is the worst car that i had driven in my entire life. Such a useless brand
            Your answer : Negative
            """
            response=self.client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                model="llama3-8b-8192",
                
            )
            return response.choices[0].message.content
        
        except Exception as e:
            raise(CustomException(e,sys))
        

'''
if __name__=="__main__":
    analysis=SentimentAnalysis()
    fb="Recession hit Veronique Branquinho, she has to quit her company, such a shame!"
    result=analysis.analyse_sentiment(fb)
    print(result)

'''
