from django.core.management.base import BaseCommand
from faker import Faker
from users.models import AppleHealthStat
from django.contrib.auth import get_user_model
import random
from datetime import timedelta
from django.utils import timezone
import datetime

fake = Faker()
User = get_user_model()

class Command(BaseCommand):
    help = 'Seeds Apple Health Stats for users who slept less than 6 hours in total for the week.'

    def handle(self, *args, **options):

        users = User.objects.all()
        today = datetime.datetime.now()
        
        start_of_week = today - timedelta(days=7)
        
        for user in users:
            for i in range(1):  
                date = start_of_week + timedelta(days=i)
                sleep_analysis = [
                    {
                        "date": date.replace(hour=random.randint(0, 23), minute=random.randint(0, 59)).isoformat(),
                        "sleep_time": int(random.uniform(0, 7200))  
                    } for _ in range(random.randint(5, 20))  
                ]

                AppleHealthStat.objects.create(
                    user=user,
                    dateOfBirth=fake.date_of_birth(),
                    height=random.randint(150, 200),
                    bodyMass=random.randint(50, 120),
                    bodyFatPercentage=random.randint(10, 30),
                    biologicalSex=random.choice(['male', 'female', 'other']),
                    activityMoveMode=random.choice(['activeEnergy', 'exercise', 'stand']),
                    stepCount=random.randint(0, 10000),
                    basalEnergyBurned=random.randint(0, 3000),
                    activeEnergyBurned=random.randint(0, 1000),
                    flightsClimbed=random.randint(0, 20),
                    appleExerciseTime=random.randint(0, 3600),
                    appleMoveTime=random.randint(0, 3600),
                    appleStandHour=random.choice([0, 1, 2, None]),
                    menstrualFlow=random.choice(['unspecified', 'light', 'moderate', 'heavy']),
                    HKWorkoutTypeIdentifier=random.choice(['running', 'cycling', 'walking', None]),
                    heartRate=random.randint(60, 100),
                    oxygenSaturation=random.randint(90, 100),
                    mindfulSession=None,
                    sleepAnalysis=sleep_analysis,
                )

    
        

        self.stdout.write(self.style.SUCCESS('Successfully seeded AppleHealthStat data for Sleep Condition API'))
