import factory
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    username = factory.Sequence(lambda n: f'{n}')
    is_staff = False
    is_superuser = False
    password = 'secret'

    @factory.lazy_attribute
    def email(self):
        return f'{self.first_name}@test.com'

    class Meta:
        model = User

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        password = kwargs.pop("password", None)
        obj = super(UserFactory, cls)._create(model_class, *args, **kwargs)
        obj.set_password(password)
        obj.save()
        Token.objects.create(user=obj)
        return obj