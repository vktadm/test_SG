# shell
import pandas as pd
from django.contrib.auth.models import User

df = pd.read_csv('auth.csv')

for i in df.index:
    user = User.objects.create_user(id=df['patient_id'][i], username=df['login'][i], password=df['password'][i])
    user.save()