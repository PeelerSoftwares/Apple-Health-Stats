from django.core.management.base import BaseCommand
from faker import Faker
from users.models import AppleHealthStat
from django.contrib.auth import get_user_model
import random
from datetime import timedelta
from django.utils import timezone
import datetime

User = get_user_model()

class Command(BaseCommand):
    help = 'Seed Apple Health Stat objects for walking data'

    def handle(self, *args, **options):
        fake = Faker()
        users = User.objects.all()

        for user in users:
            for i in range(7):  
                created_at_date = timezone.now() - timedelta(days=i)
                print("date is: ", created_at_date)
                step_count = random.randint(0, 7500)  

                AppleHealthStat.objects.create(
                    user=user,
                    dateOfBirth=fake.date_of_birth(),
                    height=random.randint(150, 200),
                    bodyMass=random.randint(50, 100),
                    bodyFatPercentage=random.randint(15, 30),
                    biologicalSex=random.choice(['male', 'female']),
                    activityMoveMode='activeEnergy',
                    stepCount=step_count,
                    basalEnergyBurned=random.randint(1000, 3000),
                    activeEnergyBurned=random.randint(100, 1000),
                    flightsClimbed=random.randint(0, 20),
                    appleExerciseTime=random.randint(0, 180),
                    appleMoveTime=random.randint(0, 180),
                    heartRate=random.randint(60, 100),
                    sleepAnalysis=[
                        #{"date": created_at_date.strftime('%Y-%m-%d 00:00'), "sleep_time": random.randint(7200, 36000)}
                    ],
                    created_at = created_at_date,
                    updated_at = created_at_date,
                )

            for i in range(7):
                created_at_date = timezone.now() - timedelta(days=(i + 7)) 
                print("date is: ", created_at_date)
                step_count = random.randint(3000, 15000)

                AppleHealthStat.objects.create(
                    user=user,
                    dateOfBirth=fake.date_of_birth(),
                    height=random.randint(150, 200),
                    bodyMass=random.randint(50, 100),
                    bodyFatPercentage=random.randint(15, 30),
                    biologicalSex=random.choice(['male', 'female']),
                    activityMoveMode='activeEnergy',
                    stepCount=step_count,
                    basalEnergyBurned=random.randint(1000, 3000),
                    activeEnergyBurned=random.randint(100, 1000),
                    flightsClimbed=random.randint(0, 20),
                    appleExerciseTime=random.randint(0, 180),
                    appleMoveTime=random.randint(0, 180),
                    heartRate=random.randint(60, 100),
                    sleepAnalysis=[
                        #{"date": created_at_date.strftime('%Y-%m-%d 00:00'), "sleep_time": random.randint(7200, 36000)}
                    ],
                    created_at = created_at_date,
                    updated_at = created_at_date,
                )

        
        self.stdout.write(self.style.SUCCESS('Successfully seeded Apple Health Stat objects.'))

