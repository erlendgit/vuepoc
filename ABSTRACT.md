Hoe werkt het nou precies?
===

Vue kan worden gebruikt om ingewikkelde, geneste, formulieren te maken in Django. De gewone componenten zijn aardig voor platte formulieren. Maar als er herhaling in zit van een object met meerdere velden per regel is het handig om een framework in te schakelen.

### De situatie

We zouden graag gegevens door willen geven van Django aan vue, en de wijzigingen ontvangen via formdata.

Omdat formdata niet zo goed is in geneste structuren zouden we json willen inzetten. Dat kan werken met een hidden input veld als gegevensdrager. Vue leest het uit het hidden input field en schrijft het resultaat daar weer in terug.

### Het probleem

Echter... dat kan niet. Want de structuur wordt bepaald door andere html elementen. Die maken gebruik van v-model. En er kan maar 1 v-model op een data structuur staan.

### Oplossing


* Zet de json bij het laden van de pagina niet in een hidden input field, maar:
  * Direct in de data() method van Vue.
  * Het kan niet in de hidden input, zelfs niet in een data-attribuut, want die is nog niet beschikbaar op het moment van toekennen.
* Gebruik v-model voor de formulier elementen waarmee de bezoeker de data structuur kan manipuleren zoals je dat gewend bent.
  * Sla de `name` property over, je wilt deze niet mee sturen in de formdata.
* Gebruik een computed property om de data structuur on de fly te converteren naar json
* Stel de hidden input zo in dat ie deze computed property volgt met een `:value` binding.