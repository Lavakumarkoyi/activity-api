from django.core.management.base import BaseCommand, CommandError
import json
from app.models import *
from django.utils.dateparse import parse_datetime

from datetime import datetime

# import dateutil.parser


class Command(BaseCommand):
    help = 'Load JSON concert data'

    def add_arguments(self, parser):
        parser.add_argument('filename', type=str)

    def handle(self, *args, **options):
        with open(options['filename'], 'r') as f:
            data = json.load(f)

        for member in data['members']:
            CustomUser.objects.create_user(
                id=member['id'], username=member['real_name'], timezone=member['tz'], password='lavakumar')

            for act in member['activity_periods']:
                # print(datetime.strptime(act['start_time'], '%b %d %Y %I:%M%p'))
                activity.objects.create(
                    user_id=member['id'], start_time=datetime.strptime(act['start_time'], '%b %d %Y %I:%M%p'), end_time=datetime.strptime(act['end_time'], '%b %d %Y %I:%M%p'))
