# Generated for Phase 2 - Migrate existing product categories to Category model

from django.db import migrations


def create_categories_from_products(apps, schema_editor):
    """
    Create Category objects from unique product_category values in existing products.
    """
    Product = apps.get_model('sellerapp', 'product')
    Category = apps.get_model('sellerapp', 'Category')
    
    # Get all unique product_category values
    unique_categories = Product.objects.values_list('product_category', flat=True).distinct()
    
    # Create Category objects for each unique value
    for cat_name in unique_categories:
        if cat_name:  # Skip empty/null values
            # Check if category already exists (case-insensitive)
            if not Category.objects.filter(category_name__iexact=cat_name).exists():
                Category.objects.create(category_name=cat_name.strip())


def reverse_categories(apps, schema_editor):
    """Reverse function - delete created categories"""
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0016_category_management'),
    ]

    operations = [
        migrations.RunPython(create_categories_from_products, reverse_categories),
    ]