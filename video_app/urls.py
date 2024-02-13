from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import (
    CommentListCreateView,
    FavoriteContentViewSet,
    GenreViewSet,
    DirectorViewSet,
    MovieViewSet,
    SeriesViewSet,
    SeasonViewSet,
    EpisodeViewSet,
    CategoryViewSet,
    BannerViewSet,
    SubscriptionPlanView,
    UserSubscriptionViewSet,
    VideoConversionTypeListView,
    ContentTypeListView,
    PandaDocsView,
    MovieFeaturedViewSet
)

router = DefaultRouter()

router.register(r'genres', GenreViewSet, basename="genres")
router.register(r'directors', DirectorViewSet, basename="directors")
router.register(r'movies', MovieViewSet, basename="movies")
router.register(r'series', SeriesViewSet, basename="series_home")
router.register(r'banners', BannerViewSet, basename='banners')
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'plans', SubscriptionPlanView, basename='plans')

series_router = routers.NestedDefaultRouter(router, r'series', lookup='series')
# series/{series_id}/seasons/
series_router.register(r'seasons', SeasonViewSet, basename='series-seasons')

seasons_router = routers.NestedDefaultRouter(
    series_router, r'seasons', lookup='season')

# series/{series_id}/seasons/{season_id}/episodes/
seasons_router.register(r'episodes', EpisodeViewSet,
                        basename='seasons-episodes')
router.register(r'subscriptions', UserSubscriptionViewSet)
router.register(r'user-favorites', FavoriteContentViewSet, basename='user-favorites-home')
router.register(r'video-conversion-types', VideoConversionTypeListView, basename='video-conversion-types')
router.register(r'content-types', ContentTypeListView, basename='content-types')
router.register(r'docs', PandaDocsView, basename='panda-docs')
router.register(r'docs', PandaDocsView, basename='panda-docs')
router.register(r'is_featured_movies', MovieFeaturedViewSet, basename='is_featured')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(series_router.urls)),
    path('comments/', CommentListCreateView.as_view(), name='comment-list'),
    path('', include(seasons_router.urls)),
]
