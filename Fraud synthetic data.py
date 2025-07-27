from faker import Faker
import random
import pandas as pd
import numpy as np

fake = Faker()
Faker.seed(0)
np.random.seed(0)

n = 10000

universities = ['Harvard', 'MIT', 'Stanford', 'SMIU', 'FAST', 'NED', 'IU']
degrees = ['BSCS', 'BSAI', 'BSE', 'BBA', 'BSIT']
sources = ['Mobile', 'Desktop']

submission_times = [fake.date_time_between(start_date='-30d', end_date='now') for _ in range(n)]
data = {
    'application_id': [i+1 for i in range(n)],
    'applicant_name': [fake.name() for _ in range(n)],
    'email': [fake.email() for _ in range(n)],
    'phone_number': [fake.phone_number() for _ in range(n)],
    'university': [random.choice(universities) for _ in range(n)],
    'degree': [random.choice(degrees) for _ in range(n)],
    'cgpa': [round(random.uniform(2.0, 4.0), 2) for _ in range(n)],
    'submission_time': submission_times,
    'ip_address': [fake.ipv4_public() for _ in range(n)],
    'resume_quality_score': [random.randint(40, 100) for _ in range(n)],
    'application_source': [random.choice(sources) for _ in range(n)],
    'previous_applications': [random.randint(0, 5) for _ in range(n)],
}

df = pd.DataFrame(data)
df.head()
df.to_csv(r'C:\Users\princ\Desktop\fraud_synthetic_data.csv', index=False)