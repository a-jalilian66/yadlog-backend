from modeltranslation.admin import TranslationAdmin
from mptt.admin import DraggableMPTTAdmin


class TranslationDraggableMPTTAdmin(TranslationAdmin, DraggableMPTTAdmin):
    """
    Admin class combining modeltranslation's TranslationAdmin
    with MPTT's DraggableMPTTAdmin for tree-structured models
    that require translated fields.
    """
    pass
