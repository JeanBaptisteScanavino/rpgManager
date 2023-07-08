from django.contrib.auth.models import User
from django.test import TestCase


class CreateUser(TestCase):
    def setUp(self) -> None:
        User.objects.create_user("Mario", "Mario@toadworld.com", "PeachIsLove")

    def test_user_is_created(self):
        user = User.objects.get(username="Mario")
        assert user
        assert user.username == "Mario"
        assert user.email == "Mario@toadworld.com"


class UpdateUser(TestCase):
    def setUp(self) -> None:
        User.objects.create_user("Mario", "Mario@toadworld.com", "PeachIsLove")

    def test_user_should_be_update(self):
        user = User.objects.get(username="Mario")
        assert user
        assert user.username == "Mario"
        user.username = "Warrio"
        user.save()

        hacked_user = User.objects.get(username="Warrio")
        assert hacked_user.username == "Warrio"
