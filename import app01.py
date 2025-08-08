import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Learntest.settings')
import django
django.setup()

import app01.models
app01.models.MyAdmin.objects.create(id="admin", user_name="admin", password="9b7bdac3cbd4af86551d5f27d64a5291")
exit()