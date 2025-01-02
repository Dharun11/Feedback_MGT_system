
from src.exception import CustomException
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
            prompt=f"""You are an advanced AI model trained to perform sentiment analysis on user feedback. Your task is to classify the sentiment of the provided feedback into one of three categories: Positive, Negative, or Neutral.

            Follow these rules:

                - Strictly respond with only one word: Positive, Negative, or Neutral.
                - Analyze the tone, context, and wording of the feedback carefully:
                - Positive: Indicates satisfaction, appreciation, or a favorable opinion.
                - Negative: Indicates dissatisfaction, criticism, or an unfavorable opinion.
                - Neutral: Indicates an ambiguous, mixed, or emotionless tone, where no clear positive or negative sentiment is conveyed.
            Handle edge cases:
                Mixed feedback (e.g., both positive and negative points): Prioritize the dominant sentiment.
                Sarcasm or irony: Detect implied sentiment rather than literal meanings.
                Emotionally neutral statements (e.g., purely factual without opinion): Classify as Neutral.
                Short or unclear feedback (e.g., "Okay," "Good," "Bad"): Infer sentiment based on common usage and tone.
                Feedback with strong emotional words (e.g., "amazing," "terrible"): Classify based on the intensity of the words used.
                Example 1: User feedback: "With the car that I bought from you for rent, it is the worst car that I have driven in my entire life. Such a useless brand." Your answer: Negative

                Example 2: User feedback: "The product is decent, but the delivery service was slow." Your answer: Neutral

                Example 3: User feedback: "Absolutely loved the service, the team was so helpful!" Your answer: Positive

                Example 4: User feedback: "The phone is okay, nothing extraordinary." Your answer: Neutral

                Feedback to analyze: {user_feedback}
                Your answer:
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
        


if __name__=="__main__":
    analysis=SentimentAnalysis()
    fb="My bike was put on hold...should have known that.... argh total bummer"
    result=analysis.analyse_sentiment(fb)
    print(result)


