# Apple-Health-Stats
Assignment 3 Results

Task 3 - Implement simple AI logic

Note: As I don’t have paid chat gpt api key, so I have used GROQ which is a free tool to generate AI responses using latest Llama model (llama3-groq-70b-8192-tool-use-preview)

API RESPONSES:

Apple Health Stat API Response:

http://127.0.0.1:8000/api/stats/

{
        "id": 2469,
        "dateOfBirth": "1929-07-09T00:00:00Z",
        "height": 163,
        "bodyMass": 119,
        "bodyFatPercentage": 27,
        "biologicalSex": "female",
        "activityMoveMode": "exercise",
        "stepCount": 4578,
        "basalEnergyBurned": 2103,
        "activeEnergyBurned": 362,
        "flightsClimbed": 5,
        "appleExerciseTime": 3209,
        "appleMoveTime": 947,
        "appleStandHour": null,
        "menstrualFlow": "moderate",
        "HKWorkoutTypeIdentifier": "walking",
        "heartRate": 81,
        "oxygenSaturation": 93,
        "mindfulSession": null,
        "sleepAnalysis": [
            {
                "date": "2024-09-30T11:12:45.252311",
                "sleep_time": 1358
            },
            {
                "date": "2024-09-30T17:43:45.252311",
                "sleep_time": 4720
            },
            {
                "date": "2024-09-30T04:53:45.252311",
                "sleep_time": 6488
            },
            {
                "date": "2024-09-30T18:58:45.252311",
                "sleep_time": 4363
            },
            {
                "date": "2024-09-30T12:00:45.252311",
                "sleep_time": 4914
            },
            {
                "date": "2024-09-30T09:15:45.252311",
                "sleep_time": 1904
            },
            {
                "date": "2024-09-30T10:13:45.252311",
                "sleep_time": 3247
            },
            {
                "date": "2024-09-30T19:13:45.252311",
                "sleep_time": 678
            },
            {
                "date": "2024-09-30T10:17:45.252311",
                "sleep_time": 5693
            },
            {
                "date": "2024-09-30T05:28:45.252311",
                "sleep_time": 2363
            }
        ],
        "created_at": "2024-10-07T00:43:45.263316Z",
        "updated_at": "2024-10-07T00:43:45.263322Z",
        "user": 123
    },



TASK 1: Users with a week of sleep less than 6 hours.

http://127.0.0.1:8000/api/sleep-condition/?format=api

[
    {
        "user": "dianeromero",
        "ai_response": "Dear Dianeromero,\n\nIt appears that you have been sleeping less than 6 hours on some days, such as on 2024-09-30 when you slept for 5.16 hours. We understand that life can be busy, but it's crucial to prioritize your sleep health.\n\nSleeping less than 6 hours regularly can lead to fatigue, mood swings, and even long-term health issues. We recommend aiming for at least 7-8 hours of sleep each night to ensure you feel rested and ready to tackle the day.\n\nTo improve your sleep quality, consider establishing a consistent bedtime routine, avoiding caffeine and heavy meals before bedtime, and creating a comfortable sleeping environment. If you continue to struggle with sleep, it may be helpful to consult with a healthcare professional for further guidance.\n\nRemember, taking care of your sleep is an investment in your overall well-being. Let's work together to ensure you get the restful sleep you deserve.\n\nBest regards,\n[Your Name]"
    }
]



TASK 2: User who have reached 10,000 steps today.

http://127.0.0.1:8000/api/walked-10000-steps/

HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "user": "mustafa786",
        "ai_response": "Great job, Mustafa786! You've taken an impressive 12,000 steps today. That's fantastic progress towards maintaining a healthy lifestyle. Your dedication to staying active is commendable. To keep up the good work, remember to also incorporate rest days into your routine to allow your body to recover. Additionally, consider incorporating different types of exercise to keep your workouts interesting and prevent plateaus. Keep up the great work!"
    }
]



TASK 3: Users who walked 50 percent less this week compared to previous week.

http://127.0.0.1:8000/api/walked-50-percent-less/


HTTP 200 OK
Allow: GET, HEAD, OPTIONS
Content-Type: application/json
Vary: Accept

[
    {
        "user": "mustafa786",
        "ai_response": "Dear Mustafa786,\n\nI hope this message finds you well. I wanted to take a moment to discuss your recent physical activity levels. It's great to see that you've been active and walking regularly, but I noticed a significant decrease in your steps this week compared to the previous one. \n\nLast week, you walked an impressive 65,511 steps, which is fantastic! However, this week, the number has dropped to 32,498 steps, which is about 50% less than the previous week. While it's normal to have fluctuations, maintaining a consistent level of physical activity is crucial for your overall health and well-being.\n\nWalking is an excellent way to stay active, improve your mood, and boost your energy levels. It's also beneficial for your heart health, weight management, and even strengthens your bones and muscles. I would encourage you to try to get back to your previous levels of activity or even set a new goal for yourself.\n\nTo help you increase your steps, consider incorporating more walks into your daily routine. You could try taking a short walk during your lunch break, walking to a coworker's desk instead of sending an email, or simply taking a few extra laps around your house in the evening. Every step counts, and these small changes can add up to make a big difference.\n\nRemember, consistency is key when it comes to physical activity. Setting achievable goals and gradually increasing your activity levels can make it easier to maintain a healthy lifestyle. If you need any assistance or guidance on how to increase your physical activity, I'm here to help.\n\nKeep up the good work, and let's aim to get those steps back up!"
    },
    {
        "user": "dwhite",
        "ai_response": "Hi Dwhite, I've noticed a significant decrease in your weekly steps, from 67,012 steps last week to 20,191 this week. This is a 50% reduction, which could potentially impact your overall health and fitness goals. It's important to maintain a consistent level of physical activity for optimal health benefits. I recommend aiming for at least 10,000 steps per day to get back on track. Would you like some tips on how to increase your daily steps?"
    },
    {
        "user": "oelliott",
        "ai_response": "Hi Oelliott,\n\nI hope this message finds you well. I wanted to take a moment to discuss your recent activity levels. It appears that your step count has decreased by 50% this week compared to the previous week. While it's normal to have fluctuations, maintaining a consistent level of physical activity is important for your overall health.\n\nWalking is an excellent way to stay active and can provide numerous benefits such as improved cardiovascular health, increased strength and flexibility, and even enhanced mental well-being. I would encourage you to try to increase your daily step count to get back on track with your previous week's activity level.\n\nTo help you achieve this goal, consider incorporating more walking into your daily routine. This could be as simple as taking a short walk during your lunch break, walking to a coworker's office instead of sending an email, or taking a few extra laps around the block after dinner. Every step counts and can make a significant difference in your health.\n\nRemember, consistency is key when it comes to maintaining a healthy lifestyle. If you need any additional support or guidance, feel free to reach out. Let's work together to get you back on track and enjoying the many benefits that regular walking can provide.\n\nBest regards,\nYour Healthcare Provider"
    },
    {
        "user": "dianeromero",
        "ai_response": "Hi Dianeromero,\n\nI've noticed that your walking activity has decreased by 50% this week compared to the previous week. It's important to maintain a consistent level of physical activity for overall health and well-being. I recommend aiming for at least 70,000 steps per week, which is approximately 10,000 steps per day. This can help improve your cardiovascular health, boost your mood, and even aid in weight management.\n\nTo increase your steps, consider incorporating more walking into your daily routine. You could try taking a short walk during your lunch break, walking to a coworker's desk instead of sending an email, or simply taking a few extra laps around your house after dinner. Every step counts!\n\nRemember, consistency is key. Let's work together to get you back on track. How does that sound?"
    },
    {
        "user": "nicole79",
        "ai_response": "Hi Nicole79, \n\nI've noticed that your weekly step count has decreased by 50% this week, with a total of 29,766 steps compared to the previous week's 83,118 steps. It's important to maintain a consistent level of physical activity for overall health and well-being.\n\nTo get back on track, I recommend incorporating more walking into your daily routine. Try to take short walks during breaks at work, walk to nearby destinations instead of driving, or even schedule a daily walk with a friend or family member. Every step counts!\n\nAim to gradually increase your daily steps to reach your previous week's average. This will not only help you stay active but also boost your mood and energy levels. Remember, consistency is key, so let's work together to get those steps back up!"
    }
]



