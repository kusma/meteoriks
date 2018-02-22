---
# You don't need to edit this file, it's empty on purpose.
# Edit theme's home layout instead if you wanna make some changes
# See: https://jekyllrb.com/docs/themes/#overriding-theme-defaults
layout: home
---
{% for demo in site.data.demos %}

# {{ demo.name }}

{% if demo.groups.size > 0 %}
{% assign groups = demo.groups | map: 'name' %}
## by {{ groups | array_to_sentence_string }}
{% endif %}

{% if demo.screenshot == null %}
[![{{ demo.name }}](http://via.placeholder.com/400x300?text=No+Screenshot)](http://www.pouet.net/prod.php?which={{demo.id}})
{% else %}
[![{{ demo.name }}]({{ demo.screenshot }})](http://www.pouet.net/prod.php?which={{ demo.id }})
{% endif %}
---
{% endfor %}
