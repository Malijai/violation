# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms


class ChercheForm(forms.Form):
    recherchetexte = forms.CharField(label='Type the begining of the Criminal Code number: type 140 to find VIOLATION for 140.2(a)', max_length=100)