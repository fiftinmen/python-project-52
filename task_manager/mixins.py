class NoColonsFormMixin:
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.label_suffix = ""


class NoColonsModelFormMixin:
    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.label_suffix = ""
        return form


class NoColonsFilterMixin:

    def form(self):
        self._form = super().form
        self._form.label_suffix = ""
        return self._form
