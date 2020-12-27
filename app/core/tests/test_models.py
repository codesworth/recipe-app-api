from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user succesfully"""
        email = 'test@email.com'
        password = 'testpassword'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(email, user.email)
        self.assertTrue(user.check_password(password), password)

    def test_new_user_email_normalized(self):
        """Test that an email for a new user is normalized"""
        email = 'test@LODY.COM'
        user = get_user_model().objects.create_user(email, '123test')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test new user with invalid email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '1234test')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test@super.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
