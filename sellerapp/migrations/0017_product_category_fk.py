# Generated for Phase 2 - Product-Category Relationship

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sellerapp', '0017_create_categories_from_products'),
    ]

    operations = [
        # Simply alter the field - existing data will be set to NULL
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='sellerapp.category'),
        ),
    ]