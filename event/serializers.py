from rest_framework import serializers
from event.models import EventType, Event
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


# class EventTypeSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = EventType
#         fields = ('id', 'name')


class EventSerializers(serializers.ModelSerializer):
    event_type = serializers.CharField(source='event_type.name')

    class Meta:
        model = Event
        fields = ('event_type', 'info', 'timestamp', )

    def create(self, validated_data):
        request = self.context.get("request")
        user = User.objects.get(username=request.user).id
        event_type = EventType.objects.get_or_create(name=validated_data['event_type']['name'])[0].id
        info = validated_data['info']
        timestamp = validated_data['timestamp']
        event = Event.objects.create(
            user_id=user,
            event_type_id=event_type,
            info=info,
            timestamp=timestamp)
        return event


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True, 'required': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        return user