from django.urls import path

from . import views

app_name = 'zdrowie'
urlpatterns = [
    path('', views.index_view, name='index'),
    path('wprowadzenie/', views.wprowadzenie_view, name='wprowadzenie'),
    path('choroba/', views.choroba_view, name='choroba'),
    path('historia/', views.historia_view, name='historia'),
    path('modele/', views.modele_view, name='modele'),
    path('psychologia_zdrowia/', views.psychologia_zdrowia_view, name='psychologia_zdrowia'),
    path('paradygmaty/', views.paradygmaty_view, name='paradygmaty'),
    path('koherencja/', views.koherencja_view, name='koherencja'),
    path('podejscia/', views.podejscia_view, name='podejscia'),
    path('stres/', views.stres_view, name='stres'),
    path('stres_zawodowy/', views.stres_zawodowy_view, name='stres_zawodowy'),
    path('zachowania_zdrowotne/', views.zachowania_zdrowotne_view, name='zachowania_zdrowotne'),
    path('styl_zycia/', views.styl_zycia_view, name='styl_zycia'),
    path('opieka_zdrowotna/', views.opieka_zdrowotna_view, name='opieka_zdrowotna'),
    path('profilaktyka/', views.profilaktyka_view, name='profilaktyka'),
    path('ankieta/', views.ankieta_view, name='ankieta'),
    path('rekomendacje/', views.BookListView.as_view(), name='rekomendacje'),
    path('serwis/', views.serwis_view, name='serwis'),
    path('serwis/', views.serwis_view, name='serwis'),
    path('doradca/', views.get_doradca, name='doradca'),
    path('doradca1/', views.doradca1_view, name='doradca1'),
]
