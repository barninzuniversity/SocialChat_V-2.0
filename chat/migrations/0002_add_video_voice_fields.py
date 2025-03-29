from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),  # Updated to reference the correct dependency
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='video',
            field=models.FileField(blank=True, null=True, upload_to='messages/videos/'),
        ),
        migrations.AddField(
            model_name='message',
            name='voice_message',
            field=models.FileField(blank=True, null=True, upload_to='messages/voice/'),
        ),
    ] 