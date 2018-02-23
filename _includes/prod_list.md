{% for prod in include.prods %}

# {{ prod.name }}

{% if prod.groups.size > 0 %}
{% assign groups = prod.groups | map: 'name' %}
by {{ groups | array_to_sentence_string }}
{% endif %}

[![{{ prod.name }}]({{ prod.screenshot | default: "http://via.placeholder.com/400x300?text=No+Screenshot" }})](http://www.pouet.net/prod.php?which={{ prod.id }})

{% assign platforms = prod.platforms | first | map: 'name' %}

* Type: {{ prod.types | array_to_sentence_string }}
* Rank: {{ forloop.index }}
* Platform: {{ platforms }}

---
{% endfor %}
