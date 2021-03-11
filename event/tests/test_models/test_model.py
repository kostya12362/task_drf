from django.test import TestCase
from event.tests.factories.users import UserFactory
from event.models import EventType, Event
from django.utils import timezone


class EventModelsTestCase(TestCase):
    def setUp(self):
        UserFactory()
        EventType(name="Workgin in room").save()

    def test_model_EventType(self):
        event_type = EventType(name="Home Workgin")
        event_type.save()
        self.assertEqual(str(event_type), event_type.name)

    def test_model_Event(self):
        event = Event(user_id=1, event_type_id=1, info={"1": "2222"}, timestamp=timezone.now())
        event.save()
        self.assertEqual(str(event), event.event_type.name)
