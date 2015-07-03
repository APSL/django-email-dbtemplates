# -*- coding: utf-8 -*-

from dbtemplates.models import EmailTemplate
from modeltranslation.translator import translator, TranslationOptions


class EmailTemplateTrans(TranslationOptions):
    fields = ('subject', 'content', )
translator.register(EmailTemplate, EmailTemplateTrans)
