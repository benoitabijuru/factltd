# Generated by Django 5.1.4 on 2024-12-21 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FactWebApp', '0022_image_design_category_alter_services_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='design_category',
        ),
        migrations.AddField(
            model_name='image',
            name='subcategory',
            field=models.CharField(blank=True, choices=[('architecture', 'Architecture'), ('construction-management', 'Construction Management'), ('education', 'Education'), ('research', 'Research'), ('others', 'Others')], default='others', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='description',
            field=models.TextField(default='this services is provided by Fact ltd, which is located in Kigali.'),
        ),
    ]
