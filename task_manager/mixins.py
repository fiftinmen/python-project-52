class NoColonsFormMixin:
    def __init__(self, request=None, *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.label_suffix = ""
