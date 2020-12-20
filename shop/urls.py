from django.urls import path
from shop.views import index, productDetails, signup, sendOtp,login,downloadFree
from shop.classViews import LoginView,SignupView,LogoutView,createPayment,paymentSuccess,downloadProduct,my_orders,ResetPassword
from shop.middlewares.login_required_middleware import login_required
from shop.middlewares.can_not_access_after_login import cantAssesAfterLogin

urlpatterns = [
    path('', index, name="home"),
    path('products/<int:product_id>', productDetails, name="details"),
    path('signup/', cantAssesAfterLogin(SignupView.as_view()), name="signup"),
    path('login/', cantAssesAfterLogin(LoginView.as_view()), name="login"),
    path('reset-password/', ResetPassword.as_view(), name="reset-password"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('free-download/<int:product_id>', downloadFree, name="free-download"),
    path('create-payment/<int:product_id>', login_required(createPayment), name="payment"),
    path('complete-payment/', login_required(paymentSuccess), name="payment-success"),
    path('download/paidproduct/<int:product_id>', login_required(downloadProduct), name="download-product"),
    path('my-orders/', login_required(my_orders), name="my-orders"),
    path('send-otp/', sendOtp, name="sendotp"),
]
