import os

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import ListView
import plotly.graph_objects as go

from .models import Book
from .forms import YourChoice, Doradca
from .filters import BookFilter

def get_doradca(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Doradca(request.POST)
        # check whether it's valid:
        if form.is_valid():
            wiek = form.cleaned_data['wiek']
            plec = form.cleaned_data['plec']
            waga = form.cleaned_data['waga']
            wzrost = form.cleaned_data['wzrost']
            sen = form.cleaned_data['sen']
            sniadanie = form.cleaned_data['sniadanie']
            alkohol = form.cleaned_data['alkohol']
            papierosy = form.cleaned_data['papierosy']
            bmi = round(waga / ((wzrost/100) * (wzrost/100)),2)
            woda = form.cleaned_data['woda']
            cwiczenia = form.cleaned_data['cwiczenia']
            ekrany = form.cleaned_data['ekrany']
            dentysta = form.cleaned_data['dentysta']
            zapotrzebowanie_na_wode = round(int(waga)*0.03,2)
            context = {
                'wiek': wiek,
                'plec': plec,
                'waga': waga,
                'wzrost': wzrost,
                'sen': sen,
                'bmi': bmi,
                'sniadanie': sniadanie,
                'alkohol': alkohol,
                'papierosy': papierosy,
                'woda': woda,
                'zapotrzebowanie_na_wode': zapotrzebowanie_na_wode,
                'cwiczenia': cwiczenia,
                'ekrany': ekrany,
                'dentysta': dentysta,
            }

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'zdrowie/doradca1.html', context)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = Doradca()

    return render(request, 'zdrowie/doradca.html', {'form': form})


def index_view(request):
    return render(request, 'zdrowie/index.html')

def wprowadzenie_view(request):
    return render(request, 'zdrowie/wprowadzenie.html')

def choroba_view(request):
    return render(request, 'zdrowie/choroba.html')

def historia_view(request):
    return render(request, 'zdrowie/historia.html')

def modele_view(request):
    return render(request, 'zdrowie/modele.html')

def doradca1_view(request):
    return render(request, 'zdrowie/doradca1.html')

def psychologia_zdrowia_view(request):
    return render(request, 'zdrowie/psychologia_zdrowia.html')

def paradygmaty_view(request):
    return render(request, 'zdrowie/paradygmaty.html')

def koherencja_view(request):
    return render(request, 'zdrowie/koherencja.html')

def podejscia_view(request):
    return render(request, 'zdrowie/podejscia.html')

def stres_view(request):
    return render(request, 'zdrowie/stres.html')

def stres_zawodowy_view(request):
    return render(request, 'zdrowie/stres_zawodowy.html')

def zachowania_zdrowotne_view(request):
    return render(request, 'zdrowie/zachowania_zdrowotne.html')

def styl_zycia_view(request):
    return render(request, 'zdrowie/styl_zycia.html')

def opieka_zdrowotna_view(request):
    return render(request, 'zdrowie/opieka_zdrowotna.html')

def profilaktyka_view(request):
    return render(request, 'zdrowie/profilaktyka.html')

def serwis_view(request):
    return render(request, 'zdrowie/serwis.html')


# def rekomendacje_view(request):
#     books = Book.objects.all()
#     for book in books:
#         book.image = book.image[book.image.find('/static'):]
#     # books = {
#     #     "Book": data
#     # }
#     return render(request, "zdrowie/rekomendacje.html", {'books':books})

def ankieta_view(request):
    labels1 = ['Nigdy', '1-2', '3-4', '5-7']
    values1 = [6, 16, 25, 145]
    fig1 = go.Figure(data=[go.Pie(labels=labels1, values=values1, sort=False)])
    fig1.update_layout({ 'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', 'title_text': 'Ile dni w tygodniu spożywasz śniadanie?'})
    sniadania = fig1.to_html(full_html=False)

    labels2 = ['1', '2', '3', '4', '5']
    values2 = [3,32,58,62,37]
    fig2 = go.Figure(data=[go.Bar(x=labels2, y=values2, text=values2, textposition='auto')])
    fig2.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)', 'title_text': 'Jak często podjadasz między posiłkami?'})
    podjadanie = fig2.to_html(full_html=False)

    labels3 = ['Tak', 'Nie, moje BMI jest powyżej 25', 'Nie, moje BMI jest poniżej 18']
    values3 = [138, 35, 19]
    fig3 = go.Figure(data=[go.Pie(labels=labels3, values=values3, sort=False)])
    fig3.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                        'title_text': 'Czy Twoja waga jest prawidłowa?'})
    waga = fig3.to_html(full_html=False)

    labels4 = ['Nigdy', 'Raz na miesiąc', 'Raz na tydzień', 'Kilka razy w tygodniu', 'Codziennie']
    values4 = [127, 17, 12, 10, 26]
    fig4 = go.Figure(data=[go.Pie(labels=labels4, values=values4, sort=False)])
    fig4.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                        'title_text': 'Jak często palisz papierosy?'})
    papierosy = fig4.to_html(full_html=False)

    labels5 = ['Nigdy', 'Raz na miesiąc', 'Raz na tydzień', 'Kilka razy w tygodniu', 'Codziennie']
    values5 = [28, 84, 56, 24, 0]
    fig5 = go.Figure(data=[go.Pie(labels=labels5, values=values5, sort=False)])
    fig5.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                        'title_text': 'Jak często pijesz alkohol?'})
    alkohol = fig5.to_html(full_html=False)

    labels6 = ['Nigdy', 'Raz na miesiąc', 'Raz na tydzień', 'Kilka razy w tygodniu', 'Codziennie']
    values6 = [15, 30, 56, 81, 10]
    fig6 = go.Figure(data=[go.Pie(labels=labels6, values=values6, sort=False)])
    fig6.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                        'title_text': 'Jak często podejmujesz aktywność fizyczną?'})
    aktywnosc = fig6.to_html(full_html=False)

    labels7 = ['poniżej 4 godzin', '5-6 godzin', '7-8 godzin', '9-10 godzin', 'powyżej 10 godzin']
    values7 = [1, 51, 119, 20, 1]
    fig7 = go.Figure(data=[go.Pie(labels=labels7, values=values7, sort=False)])
    fig7.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                        'title_text': 'Jak długi jest Twój przeciętny sen?'})
    sen = fig7.to_html(full_html=False)

    labels8 = ['1', '2', '3', '4', '5']
    values8 = [11, 33, 41, 78, 29]
    fig8 = go.Figure(data=[go.Bar(x=labels8, y=values8, text=values8, textposition='auto')])
    fig8.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                        'title_text': 'Jak bardzo dbasz o swoje pozytywne nastawienie do życia?<br><br>Średnia odpowiedzi: 3,42'})
    nastawienie = fig8.to_html(full_html=False)

    labels9 = ['1', '2', '3', '4', '5']
    values9 = [18, 57, 59, 46, 12]
    fig9 = go.Figure(data=[go.Bar(x=labels9, y=values9, text=values9, textposition='auto')])
    fig9.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                        'title_text': 'Jak bardzo dbasz o swoje zdrowie fizyczne?<br><br>Średnia odpowiedzi: 2,88'})
    zdrowie_fizyczne = fig9.to_html(full_html=False)

    labels10 = ['1', '2', '3', '4', '5']
    values10 = [2, 19, 47, 80, 44]
    fig10 = go.Figure(data=[go.Bar(x=labels10, y=values10, text=values10, textposition='auto')])
    fig10.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                        'title_text': 'Jak bardzo dbasz o swoją kondycję umysłową?<br><br>Średnia odpowiedzi: 3,76'})
    kondycja_umyslowa = fig10.to_html(full_html=False)

    labels11 = ['1', '2', '3', '4', '5']
    values11 = [14, 49, 50, 46, 33]
    fig11 = go.Figure(data=[go.Bar(x=labels11, y=values11, text=values11, textposition='auto')])
    fig11.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                         'title_text': 'Jak bardzo dbasz o odpowiednią profilaktykę oraz leczenie?<br><br>Średnia odpowiedzi: 3,18'})
    profilaktyka = fig11.to_html(full_html=False)

    labels12 = ['1', '2', '3', '4', '5']
    values12 = [7, 20, 58, 82, 25]
    fig12 = go.Figure(data=[go.Bar(x=labels12, y=values12, text=values12, textposition='auto')])
    fig12.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                         'title_text': 'Jak bardzo zachowujesz odpowiednią świadomość ekologiczną?<br><br>Średnia odpowiedzi: 3,51'})
    swiadomosc = fig12.to_html(full_html=False)

    labels13 = ['Tak', 'Nie', 'Może']
    values13 = [10, 172, 10]
    fig13 = go.Figure(data=[go.Pie(labels=labels13, values=values13, sort=False)])
    fig13.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                        'title_text': 'Czy uważasz, że podejmujesz ryzykowne zachowania seksualne?'})
    aktywnosc_seksualna = fig13.to_html(full_html=False)

    labels14 = ['Tak', 'Nie']
    values14 = [191, 1]
    fig14 = go.Figure(data=[go.Pie(labels=labels14, values=values14, sort=False)])
    fig14.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                         'title_text': 'Czy zapinasz pasy bezpieczeństwa podczas jazdy samochodem?'})
    pasy = fig14.to_html(full_html=False)

    labels15 = ['Tak', 'Nie']
    values15 = [85, 107]
    fig15 = go.Figure(data=[go.Pie(labels=labels15, values=values15, sort=False)])
    fig15.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                         'title_text': 'Czy regularnie samobadasz własne piersi lub jądra?'})
    samobadanie = fig15.to_html(full_html=False)

    values16 = ['Sposób odżywiania', 'Aktywność fizyczna', 'Umiejętność wypoczywania', 'Tryb życia', 'Czystość środowiska',
                'Jakość kontaktów międzyludzkich', 'Poczucie zadowolenia z życia', 'Radzenie sobie ze stresem',
                'Samopoczucie psychiczne', 'Warunki pracy', 'Stosowanie używek i posiadanie nałogów', 'Warunki atmosferyczne',
                'Dostępność i jakość usług medycznych',
                'Pozytywny stosunek do siebie', 'Uwarunkowania genetyczne', 'Samorealizacja', 'Warunki materialne']
    labels16 = [35, 49, 33, 43, 9, 81, 37, 37, 77, 13, 6, 18, 23, 32, 10, 39, 34]
    fig16 = go.Figure(data=[go.Bar(x=labels16, y=values16, text=labels16, textposition='auto', orientation='h')])
    fig16.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                         'title_text': 'Czynniki pozytywne'})
    pozytywne = fig16.to_html(full_html=False)

    values17 = ['Błędy żywieniowe', 'Brak czasu i umiejętności wypoczywania', 'Nieumiejętność radzenia sobie z problemami',
                'Brak ruchu', 'Nałogi i używki', 'Zanieczyszczenie środowiska', 'Zaniedbywanie siebie', 'Problemy interpersonalne',
                'Słaba odporność psychiczna', 'Warunki atmosferyczne', 'Uciążliwości pracy', 'Złe warunki materialne',
                'Negatywne nastawienie do życia', 'Uwarunkowania genetyczne', 'Złe funkcjonowanie służby zdrowia']
    labels17 = [52, 50, 51, 63, 23, 18, 56, 41, 65, 13, 26, 23, 60, 15, 20]
    fig17 = go.Figure(data=[go.Bar(x=labels17, y=values17, text=labels17, textposition='auto', orientation='h')])
    fig17.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                         'title_text': 'Czynniki negatywne'})
    negatywne = fig17.to_html(full_html=False)

    labels18 = ['Osłabia moje zdrowie', 'Raczej osłabia moje zdrowie', 'Średnio wpływa na moje zdrowie',
                'Raczej umacnia moje zdrowie', 'Umacnia moje zdrowie']
    values18 = [14, 58, 77, 39, 4]
    fig18 = go.Figure(data=[go.Pie(labels=labels18, values=values18, sort=False)])
    fig18.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                         'title_text': 'Jak oceniasz w jaki sposób Twój tryb życia wpływa na Twoje zdrowie?'})
    tryb_zycia = fig18.to_html(full_html=False)

    labels19 = ['1', '2', '3', '4', '5']
    values19 = [27, 62, 69, 26, 8]
    fig19 = go.Figure(data=[go.Bar(x=labels19, y=values19, text=values19, textposition='auto')])
    fig19.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)', 'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                         'title_text': 'Jak oceniasz wpływ pandemii COVID-19 na stan Twojego zdrowia?'})
    covid = fig19.to_html(full_html=False)

    context = {'sniadania': sniadania, 'podjadanie': podjadanie, 'waga': waga, 'papierosy': papierosy,
               'alkohol': alkohol, 'aktywnosc': aktywnosc, 'sen': sen, 'nastawienie': nastawienie,
               'zdrowie_fizyczne': zdrowie_fizyczne, 'kondycja_umyslowa': kondycja_umyslowa,
               'profilaktyka': profilaktyka, 'swiadomosc': swiadomosc, 'aktywnosc_seksualna': aktywnosc_seksualna,
               'pasy': pasy, 'samobadanie': samobadanie, 'pozytywne': pozytywne, 'negatywne': negatywne,
               'tryb_zycia': tryb_zycia, 'covid': covid}

    return render(request, 'zdrowie/ankieta.html', context)


class BookListView(ListView):
    model = Book
    template_name = 'zdrowie/rekomendacje.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = BookFilter(self.request.GET, queryset=self.get_queryset())
        books = Book.objects.all()
        for book in books:
            book.image = book.image[book.image.find('/static'):]
        return context

