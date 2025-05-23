from django.test import TestCase
from .models import Category, Image
from django.core.files.uploadedfile import SimpleUploadedFile
from datetime import date

class CategoryModelTest(TestCase):
    def test_str_returns_category_name(self):
        category = Category.objects.create(name="Тварини")
        self.assertEqual(str(category), "Тварини")
        self.assertEqual(Category.objects.count(), 1)

class ImageModelTest(TestCase):
    def setUp(self):
        self.category1 = Category.objects.create(name="Саванна")
        self.category2 = Category.objects.create(name="Джунглі")

    def test_str_returns_image_title(self):
        image_file = SimpleUploadedFile(
            name='lion_photo.jpg',
            content=b'\x47\x49\x46\x38\x39\x61',
            content_type='image/jpeg'
        )
        image = Image.objects.create(
            title="Лев у дикій природі",
            image=image_file,
            created_date=date.today(),
            age_limit=6
        )
        self.assertEqual(str(image), "Лев у дикій природі")

    def test_image_category_relationship(self):
        image_file = SimpleUploadedFile(
            name='lion_photo.jpg',
            content=b'\x47\x49\x46\x38\x39\x61',
            content_type='image/jpeg'
        )
        image = Image.objects.create(
            title="Лев у дикій природі",
            image=image_file,
            created_date=date.today(),
            age_limit=6
        )
        image.categories.set([self.category1, self.category2])

        self.assertEqual(image.categories.count(), 2)
        self.assertEqual(Image.objects.count(), 1)
        self.assertIn(self.category1, image.categories.all())
        self.assertIn(self.category2, image.categories.all())

