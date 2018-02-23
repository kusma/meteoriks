{% for prod in include.prods %}

# {{ prod.name }}

{% if prod.groups.size > 0 %}
{% assign groups = prod.groups | map: 'name' %}
by {{ groups | array_to_sentence_string }}
{% endif %}

{% if prod.screenshot == null %}
[![{{ prod.name }}](http://via.placeholder.com/400x300?text=No+Screenshot)](http://www.pouet.net/prod.php?which={{prod.id}})
{% else %}
[![{{ prod.name }}]({{ prod.screenshot }})](http://www.pouet.net/prod.php?which={{ prod.id }})
{% endif %}
---
{% endfor %}
