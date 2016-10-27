# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greenday_core', '0015_auto_20150422_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_kind',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='kind',
            field=models.IntegerField(verbose_name=((0, b'PROJECTCREATED'), (1, b'PROJECTUPDATED'), (2, b'PROJECTDELETED'), (50, b'PROJECTRESTORED'), (100, b'VIDEOCREATED'), (101, b'VIDEOUPDATED'), (102, b'VIDEODELETED'), (150, b'VIDEOHIGHLIGHTED'), (151, b'VIDEOUNHIGHLIGHTED'), (152, b'VIDEOARCHIVED'), (153, b'VIDEOUNARCHIVED'), (200, b'USERCREATED'), (201, b'USERUPDATED'), (202, b'USERDELETED'), (250, b'USERACCEPTEDNDA'), (251, b'USERINVITEDASPROJECTUSER'), (252, b'PENDINGUSERREMOVED'), (253, b'USERACCEPTEDPROJECTINVITE'), (254, b'USERREJECTEDPROJECTINVITE'), (255, b'USERREMOVED'), (256, b'PROJECTCOLLABORATORONLINE'), (257, b'PROJECTCOLLABORATOROFFLINE'), (300, b'VIDEOCOLLECTIONCREATED'), (301, b'VIDEOCOLLECTIONUPDATED'), (302, b'VIDEOCOLLECTIONDELETED'), (350, b'VIDEOADDEDTOCOLLECTION'), (351, b'VIDEOREMOVEDFROMCOLLECTION'), (450, b'PENDINGUSERINVITEDASPROJECTADMIN'), (451, b'PENDINGUSERINVITEDASPROJECTUSER'), (500, b'PROJECTROOTCOMMENTCREATED'), (501, b'PROJECTCOMMENTUPDATED'), (502, b'PROJECTCOMMENTDELETED'), (600, b'TIMEDVIDEOROOTCOMMENTCREATED'), (601, b'TIMEDVIDEOCOMMENTUPDATED'), (602, b'TIMEDVIDEOCOMMENTDELETED'), (700, b'TIMEDVIDEOREPLYCOMMENTCREATED'), (701, b'TIMEDVIDEOREPLYCOMMENTUPDATED'), (702, b'TIMEDVIDEOREPLYCOMMENTDELETED'), (800, b'PROJECTREPLYCOMMENTCREATED'), (801, b'PROJECTREPLYCOMMENTUPDATED'), (802, b'PROJECTREPLYCOMMENTDELETED'))),
        ),
        migrations.AlterField(
            model_name='event',
            name='object_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='object_kind',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='project_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='timestamp',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='video_id',
            field=models.IntegerField(null=True),
        ),
    ]
