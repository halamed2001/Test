from twilio.rest import Client
from django.utils import timezone
from .models import Donneur


def send_sms_reminder():
    donneurs = Donneur.objects.all()
    current_date = timezone.now().date()

    for donneur in donneurs:
        date_Dernier_Don = donneur.date_Dernier_Don
        time_since_last_donation = current_date - date_Dernier_Don

        if time_since_last_donation.days >= 120:
            client = Client('','')
            message = client.messages.create(
                body='',
                from_='',
                to=donneur.tel
            )


def sendsms():
    #tel = Donneur.objects.get('tel')
    acount_sid = 'ACed2aeeac5fddd4b5be248e2bd71cc7f2'
    auth_token = '4aab6949bcfb779601e75b3800a1969'
    client = Client(acount_sid, auth_token)

    message = client.messages \
                    .create(
                        body="",
                        from_='+13614597779',
                        to='46580199'
                    )
    print('message send')
