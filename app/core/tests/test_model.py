from django.test import TestCase
from django.contrib.auth import get_user_model


class TestModel(TestCase):

    def test_user_creation_with_email(self):
        """Test User created with email and password"""
        email = "santhosh.r.subramani@gmail.com"
        password = "Sanz_test_123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,  email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        """Test user email is normalized"""
        email = "santhosh.subramani@GMAIL.COM"
        user = get_user_model().objects.create_user(email, 'test12345')

        self.assertEqual(user.email, email.lower())

    def test_user_email_valid(self):
        """Test user email is not empty or null"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_super_user(self):
        """Test create super user"""
        email = "santhosh.r.subramani@gmail.com"
        user = get_user_model().objects.create_superuser(
            email, "Test6768768"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
