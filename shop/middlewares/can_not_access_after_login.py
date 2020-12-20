from django.shortcuts import redirect
def cantAssesAfterLogin(get_response):
    def middleware(request, product_id=None):
        user=request.session.get('user')
        if user:
           return redirect('home')
        else:
            return get_response(request)

    return middleware
