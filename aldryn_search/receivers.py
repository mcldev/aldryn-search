from cms.models.permissionmodels import PagePermission
from cms.models.titlemodels import Title
from cms.signals import post_publish, post_unpublish
from django.db.models.signals import post_save, post_delete
from django.dispatch.dispatcher import receiver

from .signals import add_to_index, remove_from_index


@receiver(post_publish, dispatch_uid='publish_cms_page')
def publish_cms_page(sender, instance, language, **kwargs):
    title = instance.publisher_public.get_title_obj(language)
    add_to_index.send(sender=Title, instance=title, object_action='publish')


@receiver(post_unpublish, dispatch_uid='unpublish_cms_page')
def unpublish_cms_page(sender, instance, language, **kwargs):
    title = instance.publisher_public.get_title_obj(language)
    remove_from_index.send(sender=Title, instance=title, object_action='unpublish')


def _reindex_page_titles(page):
    """Re-index all public Title objects for a given page.

    Fetches fresh Title objects from the database to avoid
    stale cached ForeignKey references on obj.page.
    """
    # Resolve to draft to get publisher_public reliably
    draft_page = page.get_draft_object() if hasattr(page, 'get_draft_object') else page
    public_page = draft_page.publisher_public if draft_page.publisher_is_draft else draft_page
    if not public_page:
        return
    # Use select_related to ensure title.page is a fresh DB fetch
    for title in public_page.title_set.filter(publisher_is_draft=False).select_related('page'):
        title.language_code = title.language
        add_to_index.send(sender=Title, instance=title, object_action='publish')


@receiver(post_save, sender=PagePermission, dispatch_uid='update_search_index_on_page_permission_save')
def update_search_index_on_permission_save(sender, instance, **kwargs):
    """Re-index when a PagePermission (view restriction) is added or changed.

    View restrictions take effect immediately (not part of draft/publish),
    and has_view_restrictions() resolves to the draft page internally,
    so the index will reflect the current state.
    """
    if instance.page:
        _reindex_page_titles(instance.page)


@receiver(post_delete, sender=PagePermission, dispatch_uid='update_search_index_on_page_permission_delete')
def update_search_index_on_permission_delete(sender, instance, **kwargs):
    """Re-index when a PagePermission (view restriction) is removed."""
    if instance.page:
        _reindex_page_titles(instance.page)







