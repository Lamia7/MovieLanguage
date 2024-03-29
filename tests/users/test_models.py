from django.test import TestCase

from users.models import User


class ModelsTestCase(TestCase):
    def test_user_str(self):
        user = User.objects.create(
            email="user1@gmail.com",
            username="user1",
            password="userpassword1",
        )
        self.assertEqual(str(user), "user1@gmail.com")

    def test_superuser_is_admin(self):
        superuser = User.objects.create_superuser(
            email="superuser1@gmail.com",
            username="superuser1",
            password="userpassword1",
        )
        self.assertIs(superuser.is_admin, True)

    def test_user_not_admin(self):
        user = User.objects.create_user(
            email="user1@gmail.com",
            username="user1",
            password="userpassword1",
        )
        self.assertIs(user.is_admin, False)

    def test_create_user_missing_email(self):
        message = "Users must have an email address"
        with self.assertRaisesMessage(ValueError, message):
            User.objects.create_user(
                email=None,
                username="User1",
                password="userpassword1",
            )
