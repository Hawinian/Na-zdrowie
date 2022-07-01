from django import forms

from .models import Tag

tag_set = Tag.objects.all()


class YourChoice(forms.Form):
    field1 = forms.ModelMultipleChoiceField(queryset=Tag.objects)

class Doradca(forms.Form):
    wiek = forms.IntegerField(max_value=120, min_value=18, label='Wiek:')
    plec = forms.ChoiceField(label='Płeć:', choices=((1, ("mężczyzna")), (2, ("kobieta"))))
    waga = forms.IntegerField(label='Waga:', min_value=30, max_value=400)
    wzrost = forms.IntegerField(label='Wzrost:', min_value=100, max_value=250)
    sen = forms.ChoiceField(label='Jak długo trwa Twój przeciętny sen?', choices=((1, ("mniej niż 4 godziny")),
    (2, ("4-5 godzin")), (3, ("5-6 godzin")),(4,("7-8 godzin")), (5,("9-10 godzin")),(6, ("powyżej 10 godzin"))))
    sniadanie = forms.ChoiceField(label="Ile dni w tygodniu spożywasz śniadanie?", choices=((1, ("Nigdy")),
    (2, ("1-2")), (3, ("3-4")),(4,("5-7"))))
    papierosy = forms.ChoiceField(label="Jak często palisz papierosy?", choices=((1, ("Nigdy")),(2, ("Raz w miesiącu")),
                                                                                 (3, ("Raz w tygodniu")),(4, ("Kilka razy w tygodniu")),(5, ("Codziennie"))))
    alkohol = forms.ChoiceField(label="Jak często pijesz alkohol?",
                                  choices=((1, ("Nigdy")), (2, ("Raz w miesiącu")),
                                           (3, ("Raz w tygodniu")), (4, ("Kilka razy w tygodniu")),
                                           (5, ("Codziennie"))))
    woda = forms.FloatField(label="Ile litrów wody wypijasz dziennie?", min_value=0, max_value=10)
    cwiczenia = forms.ChoiceField(label="Jak często podejmujesz aktywność fizyczną?",
                                  choices=((1, ("Nigdy")), (2, ("Raz w miesiącu")),
                                           (3, ("Raz w tygodniu")), (4, ("Kilka razy w tygodniu")),
                                           (5, ("Codziennie"))))
    ekrany = forms.IntegerField(label="Ile godzin spędzasz przeciętnie przed ekranami każdego dnia?", min_value=0, max_value=24)
    dentysta = forms.ChoiceField(label="Jak długo minęło od Twojej ostatniej wizyty kontrolnej u dentysty?",
                                 choices=((1, ("Więcej niż 5 lat")),
                                          (2, ("3-5 lat")), (3, ("1-3 lata")),
                                          (4, ("Mniej niż pół roku"))))
