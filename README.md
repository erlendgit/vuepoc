Hoe werkt het nou precies?
===

Vue kan worden gebruikt om ingewikkelde, geneste, formulieren te maken in Django. De gewone componenten zijn aardig voor platte formulieren. Maar als er herhaling in zit van een object met meerdere velden per regel is het handig om een framework in te schakelen.

Het probleem zit in het doorgeven van gegevens van Django aan vue, en het versturen van de gegevens terug naar Django. De formdata kan ook niet zo heel goed omgaan met geneste gegevens.

Je zou eigenlijk met json heen en weer willen slepen. Een hidden input veld kan de drager zijn van de json data. Vue leest het uit het hidden input field en schrijft het resultaat daar weer in terug.

Echter... dat kan niet. Want de structuur wordt bepaald door andere html elementen. Die maken gebruik van v-model. En er kan maar 1 v-model op een data structuur staan.

Oplossing:

* Zet de json bij het laden van de pagina niet in een hidden input field, maar:
  * Direct in de data() method van Vue.
  * Of in een html data-... property, als je dat fijner vindt.
* Gebruik v-model voor de formulier elementen waarmee de bezoeker de data structuur kan manipuleren zoals je dat gewend bent.
  * Sla de `name` property over, je wilt deze niet mee sturen in de formdata.
* Gebruik een computed property om de data structuur on de fly te converteren naar json
* Stel de hidden input zo in dat ie deze computed property volgt met een `:value` binding.