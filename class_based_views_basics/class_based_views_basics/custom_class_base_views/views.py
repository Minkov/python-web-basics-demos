from django.http import HttpResponse
from django.shortcuts import render


class BaseView:
    @classmethod
    def as_view(cls):
        def view(request, *args, **kwargs):
            self = cls()

            # dispatch
            if request.method == "GET":
                return self.get(request, *args, **kwargs)
            else:
                return self.post(request, *args, **kwargs)

        return view

# BaseView.as_view() -> cls = BaseView
# IndexView.as_view() -> cls = IndexView

class IndexView(BaseView):
    def get(self, request):
        return HttpResponse("It works with CBVs!")


def index(request):
    return HttpResponse("IT works with FBVs!")
