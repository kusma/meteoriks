---
layout: default
---
{% for demo in site.data.prods %}

# {{ demo.name }}

{% if demo.groups.size > 0 %}
{% assign groups = demo.groups | map: 'name' %}
by {{ groups | array_to_sentence_string }}
{% endif %}

{% if demo.screenshot == null %}
[![{{ demo.name }}](http://via.placeholder.com/400x300?text=No+Screenshot)](http://www.pouet.net/prod.php?which={{demo.id}})
{% else %}
[![{{ demo.name }}]({{ demo.screenshot }})](http://www.pouet.net/prod.php?which={{ demo.id }})
{% endif %}
---
{% endfor %}
