# Vue POC

Proof of concept voor Vue in Django.

## Opstarten

1. Maak een kopie van .env-example naar .env
2. Installeer de pakketjes met `bin/dev-setup.sh`; zie instructies verderop.
3. Start de server met `bin/manage.py runserver`

### Hoe gebruik je `dev-setup.sh`

```bash
# Merk op dat dit commando begint met een punt en een spatie.
# Op die manier sta je toe dat het script de actieve shell aanpast.
$ . bin/dev-setup.sh
```

Dit commando kan je iedere keer uitvoeren als je een terminal opent. Het script zorgt er voor dat de venv geladen wordt en klaar is om te gebruiken.

Als je een wijziging doet in de .env moet je het setup commando opnieuw uitvoeren zoals hier beschreven.

## Wat je je doen?

Je kunt de `vueforms` django app uitbreiden met formulieren die vue inzetten om ingewikkelde data-structuren aan te passen.
