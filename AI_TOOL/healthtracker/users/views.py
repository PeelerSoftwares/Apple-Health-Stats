from django.shortcuts import render
from rest_framework import generics
from .models import AppleHealthStat
from .serializers import AppleHealthStatSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from django.db.models import Q, F, Sum
from django.contrib.auth import get_user_model
from rest_framework import status
from django.db import models
from openai import OpenAI
import requests
from groq import Groq


User = get_user_model()

api_key = "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"

#to list all Apple health stats
class AppleHealthStatList(generics.ListCreateAPIView):
    queryset = AppleHealthStat.objects.all()
    serializer_class = AppleHealthStatSerializer


#function to get response from chatgpt
def generate_personalized_advice(prompt):

    client = Groq()
    completion = client.chat.completions.create(
        model="llama3-groq-70b-8192-tool-use-preview",
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {
                "role": "user",
                "content": ""
            }
        ],
        temperature=0.5,
        max_tokens=1024,
        top_p=0.65,
        stream=True,
        stop=None,
    )

    message=""

    for chunk in completion:
        message += str(chunk.choices[0].delta.content or "")

    return message


#Users with a week of sleep less than 6 hrs
class SleepConditionAPIView(APIView):

    def get(self, request):

        today = timezone.now()

        start_of_week = today - timedelta(days=7) #if day is monday, than get data from previous monday to current monday

        users_with_low_sleep = []

        users = User.objects.all()

        for user in users:
            sleep_data = AppleHealthStat.objects.filter(
                user=user,
                created_at__gte=start_of_week
            )

            low_sleep_days = []

            for record in sleep_data:
                daily_sleep_time = 0
                sleep_analysis = record.sleepAnalysis
                
                if sleep_analysis:
                    sleep_date = sleep_analysis[0]['date'].split(' ')[0] 

                    for sleep_record in sleep_analysis:
                        daily_sleep_time += sleep_record.get('sleep_time', 0)

                    if daily_sleep_time < 21600:
                            low_sleep_days.append({
                            "date": sleep_date,
                            "sleep in hours": daily_sleep_time / 3600
                        })
            if low_sleep_days:
                message = f"the user named {user.username} is sleeping less than 6 hours for the following days {low_sleep_days}. Give a personalised message for this user instucting him to sleep more"
                print("message is : ", message)
                ai_response = generate_personalized_advice(message)
                users_with_low_sleep.append({
                    "user": user.username,
                    "ai_response": ai_response
                })

        return Response(users_with_low_sleep)

#Users who have reached 10,000 steps today.
class Walked_10000_StepsAPIView(APIView):
    def get(self, request):

        today = timezone.now().date()

        users_with_10000_steps = User.objects.filter(
            apple_health_stat__created_at__date=today,
            apple_health_stat__stepCount__gte=10000
        ).distinct()

        response_data = []
        
        for user in users_with_10000_steps:

            latest_stat = user.apple_health_stat.filter(
                created_at__date=today,
                stepCount__gte=10000
                ).latest('created_at')

            message = f"give me a personalized health care response for user {user.username}. the user has walked {latest_stat.stepCount} steps today which is good. create a personalized message for the user appreciating and advising him based on data."
            print("message is : ", message)
            ai_response = generate_personalized_advice(message)
            response_data.append({
                "user": user.username,
                "ai_response": ai_response
            })

        return Response(response_data)

#Users who walked 50% less this week compared to the previous week.
class LowActivityAPIView(APIView):
    def get(self, request):
        today = timezone.now()
        start_of_current_week = today - timedelta(days=7)
        start_of_previous_week = start_of_current_week - timedelta(days=7)

        users_with_low_activity = []

        users = User.objects.all()

        for user in users:


            previous_week_records = AppleHealthStat.objects.filter(
                user=user,
                created_at__gte=start_of_previous_week,
                created_at__lt=start_of_current_week
            )
            #print(f"Previous Week Records for {user.username}: {previous_week_records.count()}", flush=True)

            current_week_records = AppleHealthStat.objects.filter(
                user=user,
                created_at__gte=start_of_current_week
            )
            #print(f"Current Week Records for {user.username}: {current_week_records.count()}", flush=True)

            current_week_steps = current_week_records.aggregate(total_steps=models.Sum('stepCount'))['total_steps'] or 0
            previous_week_steps = previous_week_records.aggregate(total_steps=models.Sum('stepCount'))['total_steps'] or 0

            #print(f"User: {user.username}, Current Week Steps: {current_week_steps}, Previous Week Steps: {previous_week_steps}")

            if previous_week_steps > 0 and current_week_steps <= previous_week_steps * 0.5:

                message = f"give me a personalized health care response for user {user.username}. the user has walked {current_week_steps} steps in current week which is 50 percent less this week compared to previous week in which user walked {previous_week_steps} steps. create a personalized message for the user advising him to walk more based on data."
                print("message is : ", message)
                ai_response = generate_personalized_advice(message)
                users_with_low_activity.append({
                    "user": user.username,
                    "ai_response": ai_response
                })

        return Response(users_with_low_activity)