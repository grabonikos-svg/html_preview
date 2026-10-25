# html_preview

Εφαρμογή για Windows που ανοίγει έναν φάκελο, εμφανίζει τα αρχεία `.html` και `.htm` και τα προβάλλει σε ενσωματωμένο browser.

## Εκτέλεση από τον κώδικα

```bat
python -m venv .venv
.venv\Scripts\python.exe -m pip install PySide6
.venv\Scripts\python.exe main.py
```

Η εγκατάσταση του `PySide6` περιλαμβάνει και το Qt WebEngine που χρησιμοποιεί η προεπισκόπηση.

Το εικονικό περιβάλλον και τα αρχεία build δεν περιλαμβάνονται σε αυτό το repository.
