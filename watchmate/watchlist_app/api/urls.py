
from django.urls import include, path
# from watchlist_app.api.views import movie_list, movie_details
from watchlist_app.api.views import (WatchListAV, WatchDetailAV, 
                                    StreamPlatformAV, StreamPlatformDetailAV, 
                                    ReviewList, ReviewDetail, ReviewCreate, UserReview, WatchListZ)


urlpatterns = [
    path('list/', WatchListAV.as_view(), name = 'movie_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name = 'movie_details'),
    path('list2/', WatchListZ.as_view(), name = 'watch-list'),
    
    
    path('stream/', StreamPlatformAV.as_view(), name = 'stream_platform'),
    path('stream/<int:pk>/', StreamPlatformDetailAV.as_view(), name = 'stream__details'),

    # path('review/',ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>',ReviewDetail.as_view(), name='review-detail'),
    
    path('<int:pk>/review-create/', ReviewCreate.as_view(), name = 'review-create'),
    path('<int:pk>/reviews/', ReviewList.as_view(), name = 'review_list'),
    path('review/<int:pk>/',ReviewDetail.as_view(), name='review-detail'),
    path('reviews/',UserReview.as_view(), name='user-review-detail'),

]
